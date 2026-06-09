from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

from .config import PORT, HOST, TOP_N_PATTERNS
from . import symptom as symptom_module
from . import pattern as pattern_module
from . import formula as formula_module
from . import safety as safety_module
from . import modifier as modifier_module
from .utils import calculate_dose_factor, convert_dose

app = FastAPI(
    title="中医辅助辨证开方系统",
    description="基于加权评分算法的中医证型判定与方剂推荐系统",
    version="1.0.0",
)


class DiagnosisRequest(BaseModel):
    symptoms: List[str] = Field(description="患者主诉症状列表")
    tongue: Optional[str] = Field(None, description="舌象描述")
    pulse: Optional[str] = Field(None, description="脉象描述")
    age: Optional[float] = Field(None, description="患者年龄")
    weight: Optional[float] = Field(None, description="患者体重（kg）")
    is_pregnant: bool = Field(False, description="是否孕妇")
    is_lactating: bool = Field(False, description="是否哺乳期")
    dose_unit: str = Field("克", description="剂量单位：克/钱")
    top_n: int = Field(TOP_N_PATTERNS, description="返回证型数量")


class FormulaModifyRequest(BaseModel):
    pattern_name: str
    formula_name: str
    herbs: Dict[str, Dict[str, Any]]
    patient_info: Optional[Dict[str, Any]] = None
    symptoms: Optional[List[str]] = None
    tongue: Optional[str] = None
    pulse: Optional[str] = None
    diagnosis_note: str = ""


class WeightUpdateRequest(BaseModel):
    pattern_name: str
    weights: Dict[str, float]


class ThresholdUpdateRequest(BaseModel):
    pattern_name: str
    threshold: float


class SafetyCheckRequest(BaseModel):
    herbs: List[str]
    is_pregnant: bool = False
    is_lactating: bool = False


class CaseFeedbackRequest(BaseModel):
    case_id: str
    feedback: str


@app.get("/")
async def root():
    return {
        "name": "中医辅助辨证开方系统",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "诊断接口": "/api/diagnose",
            "症状字典": "/api/symptoms",
            "舌象预设": "/api/tongue-presets",
            "脉象预设": "/api/pulse-presets",
            "证型列表": "/api/patterns",
            "方剂库": "/api/formulas",
            "禁忌检查": "/api/safety/check",
            "加减建议": "/api/modifications/{{pattern_name}}",
            "案例记录": "/api/cases",
            "统计分析": "/api/statistics",
        }
    }


@app.get("/api/symptoms")
async def get_symptoms():
    symptoms = symptom_module.get_all_symptoms()
    return {"total": len(symptoms), "symptoms": symptoms}


@app.get("/api/symptoms/synonyms")
async def get_synonyms(symptom: str):
    synonyms = symptom_module.get_synonyms(symptom)
    return {"symptom": symptom, "synonyms": synonyms}


@app.post("/api/symptoms/synonyms")
async def add_synonym(synonym: str, canonical: str):
    success = symptom_module.add_synonym(synonym, canonical)
    if not success:
        raise HTTPException(status_code=404, detail=f"标准症状 '{canonical}' 不存在")
    return {"success": True, "synonym": synonym, "canonical": canonical}


@app.post("/api/symptoms/normalize")
async def normalize_symptoms(symptoms: List[str]):
    normalized = symptom_module.normalize_symptoms(symptoms)
    return {"original": symptoms, "normalized": normalized}


@app.get("/api/tongue-presets")
async def get_tongue_presets():
    presets = symptom_module.get_tongue_presets()
    return {"total": len(presets), "presets": presets}


@app.get("/api/pulse-presets")
async def get_pulse_presets():
    presets = symptom_module.get_pulse_presets()
    return {"total": len(presets), "presets": presets}


@app.get("/api/patterns")
async def get_patterns():
    patterns = pattern_module.get_all_patterns()
    return {"total": len(patterns), "patterns": patterns}


@app.get("/api/patterns/{pattern_name}")
async def get_pattern_detail(pattern_name: str):
    detail = pattern_module.get_pattern_detail(pattern_name)
    if not detail:
        raise HTTPException(status_code=404, detail=f"证型 '{pattern_name}' 不存在")
    return detail


@app.post("/api/patterns/weights")
async def update_pattern_weights(request: WeightUpdateRequest):
    success = pattern_module.update_pattern_weights(request.pattern_name, request.weights)
    if not success:
        raise HTTPException(status_code=404, detail=f"证型 '{request.pattern_name}' 不存在")
    return {"success": True, "pattern": request.pattern_name, "updated_weights": request.weights}


@app.post("/api/patterns/threshold")
async def update_pattern_threshold(request: ThresholdUpdateRequest):
    success = pattern_module.update_pattern_threshold(request.pattern_name, request.threshold)
    if not success:
        raise HTTPException(status_code=404, detail=f"证型 '{request.pattern_name}' 不存在")
    return {"success": True, "pattern": request.pattern_name, "threshold": request.threshold}


@app.get("/api/formulas")
async def get_all_formulas(pattern: Optional[str] = None):
    if pattern:
        formulas = formula_module.get_formulas_by_pattern(pattern)
        return {"pattern": pattern, "total": len(formulas), "formulas": formulas}
    formulas = formula_module.get_all_formulas()
    return {"total": len(formulas), "formulas": formulas}


@app.get("/api/formulas/{pattern_name}/{formula_name}")
async def get_formula_detail(pattern_name: str, formula_name: str):
    detail = formula_module.get_formula_detail(pattern_name, formula_name)
    if not detail:
        raise HTTPException(status_code=404, detail=f"方剂 '{formula_name}' 不存在")
    return detail


@app.post("/api/diagnose")
async def diagnose(request: DiagnosisRequest):
    normalized_symptoms = symptom_module.normalize_symptoms(request.symptoms)

    top_patterns = pattern_module.get_top_patterns(
        symptoms=normalized_symptoms,
        tongue=request.tongue,
        pulse=request.pulse,
        top_n=request.top_n,
    )

    dose_factor = calculate_dose_factor(
        age=request.age,
        weight=request.weight,
        is_pregnant=request.is_pregnant,
        is_lactating=request.is_lactating,
    )

    patterns_with_formulas = []
    for pattern_result in top_patterns:
        pattern_name = pattern_result["pattern"]
        formulas = formula_module.get_formulas_by_pattern(pattern_name)

        adjusted_formulas = []
        for formula in formulas:
            adjusted = formula_module.adjust_formula_dose(
                formula, dose_factor, request.dose_unit
            )

            herb_names = list(adjusted["herbs"].keys())
            safety_result = safety_module.check_all_safety(
                herb_names,
                is_pregnant=request.is_pregnant,
                is_lactating=request.is_lactating,
            )
            adjusted["safety"] = safety_result
            adjusted_formulas.append(adjusted)

        patterns_with_formulas.append({
            **pattern_result,
            "formulas": adjusted_formulas,
            "modification_suggestions": modifier_module.get_modification_suggestions(pattern_name),
        })

    return {
        "request": {
            "symptoms": request.symptoms,
            "normalized_symptoms": normalized_symptoms,
            "tongue": request.tongue,
            "pulse": request.pulse,
            "age": request.age,
            "weight": request.weight,
            "is_pregnant": request.is_pregnant,
            "is_lactating": request.is_lactating,
            "dose_unit": request.dose_unit,
        },
        "dose_factor": dose_factor,
        "top_patterns": patterns_with_formulas,
    }


@app.post("/api/safety/check")
async def safety_check(request: SafetyCheckRequest):
    result = safety_module.check_all_safety(
        request.herbs,
        is_pregnant=request.is_pregnant,
        is_lactating=request.is_lactating,
    )
    return result


@app.get("/api/safety/eighteen-incompatibilities")
async def get_eighteen_incompatibilities():
    return {"rules": safety_module.get_eighteen_incompatibilities()}


@app.get("/api/safety/nineteen-incompatibilities")
async def get_nineteen_incompatibilities():
    return {"rules": safety_module.get_nineteen_incompatibilities()}


@app.get("/api/safety/pregnancy-forbidden")
async def get_pregnancy_forbidden():
    return {"herbs": safety_module.get_pregnancy_forbidden_list()}


@app.get("/api/safety/lactation-caution")
async def get_lactation_caution():
    return {"herbs": safety_module.get_lactation_caution_list()}


@app.get("/api/modifications/{pattern_name}")
async def get_modification_suggestions(pattern_name: str):
    suggestions = modifier_module.get_modification_suggestions(pattern_name)
    if not suggestions:
        raise HTTPException(status_code=404, detail=f"证型 '{pattern_name}' 没有加减建议或不存在")
    return {"pattern": pattern_name, "suggestions": suggestions}


@app.post("/api/formulas/compare")
async def compare_formulas(
    original: Dict[str, Dict[str, Any]],
    modified: Dict[str, Dict[str, Any]],
):
    diff = modifier_module.compare_formulas(original, modified)
    return diff


@app.post("/api/cases")
async def save_case(request: FormulaModifyRequest):
    original_formula = formula_module.get_formula_detail(
        request.pattern_name, request.formula_name
    )
    if not original_formula:
        raise HTTPException(status_code=404, detail=f"方剂 '{request.formula_name}' 不存在")

    modified_formula = {**original_formula, "herbs": request.herbs}
    diff = modifier_module.compare_formulas(
        original_formula["herbs"], request.herbs
    )

    patterns = pattern_module.get_top_patterns(
        symptoms=request.symptoms or [],
        tongue=request.tongue,
        pulse=request.pulse,
    )

    case_id = modifier_module.add_case_record(
        patient_info=request.patient_info or {},
        symptoms=request.symptoms or [],
        tongue=request.tongue,
        pulse=request.pulse,
        patterns=patterns,
        selected_formula={
            "pattern": request.pattern_name,
            "name": request.formula_name,
        },
        original_formula=original_formula,
        modified_formula=modified_formula,
        modification_diff=diff,
        diagnosis_note=request.diagnosis_note,
    )

    return {"case_id": case_id, "diff": diff}


@app.get("/api/cases")
async def get_cases(
    limit: int = 100,
    pattern: Optional[str] = None,
):
    cases = modifier_module.get_all_cases(limit=limit, pattern_filter=pattern)
    return {"total": len(cases), "cases": cases}


@app.get("/api/cases/{case_id}")
async def get_case(case_id: str):
    case = modifier_module.get_case_record(case_id)
    if not case:
        raise HTTPException(status_code=404, detail=f"案例 '{case_id}' 不存在")
    return case


@app.post("/api/cases/feedback")
async def add_case_feedback(request: CaseFeedbackRequest):
    success = modifier_module.update_case_feedback(request.case_id, request.feedback)
    if not success:
        raise HTTPException(status_code=404, detail=f"案例 '{request.case_id}' 不存在")
    return {"success": True, "case_id": request.case_id, "feedback": request.feedback}


@app.get("/api/statistics")
async def get_statistics():
    stats = {
        "total_cases": modifier_module.get_case_count(),
        "pattern_distribution": modifier_module.get_pattern_statistics(),
    }
    return stats


@app.get("/api/statistics/patterns/{pattern_name}")
async def get_pattern_statistics(
    pattern_name: str,
    top_symptoms: int = 10,
    top_combos: int = 5,
    combo_size: int = 3,
):
    symptoms_freq = modifier_module.get_pattern_symptom_frequency(
        pattern_name, top_n=top_symptoms
    )
    top_combinations = modifier_module.get_top_symptom_combinations(
        pattern_name, top_n=top_combos, combo_size=combo_size
    )
    return {
        "pattern": pattern_name,
        "top_symptoms": symptoms_freq,
        "top_symptom_combinations": top_combinations,
    }


@app.get("/api/utils/dose-convert")
async def dose_convert(
    dose: float,
    from_unit: str,
    to_unit: str,
):
    result = convert_dose(dose, from_unit, to_unit)
    return {
        "original_dose": dose,
        "original_unit": from_unit,
        "converted_dose": result,
        "converted_unit": to_unit,
    }


@app.get("/api/utils/dose-factor")
async def get_dose_factor(
    age: Optional[float] = None,
    weight: Optional[float] = None,
    is_pregnant: bool = False,
    is_lactating: bool = False,
):
    factor = calculate_dose_factor(age, weight, is_pregnant, is_lactating)
    return {
        "age": age,
        "weight": weight,
        "is_pregnant": is_pregnant,
        "is_lactating": is_lactating,
        "dose_factor": factor,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
