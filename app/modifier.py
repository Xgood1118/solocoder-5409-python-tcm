from typing import Dict, List, Optional, Tuple
from collections import Counter, defaultdict
import uuid
import time


CASE_HISTORY: List[Dict] = []


MODIFICATION_SUGGESTIONS: Dict[str, List[Dict]] = {
    "气虚": [
        {"condition": "自汗明显", "add": ["黄芪", "麻黄根", "浮小麦"], "remove": [], "note": "益气固表止汗"},
        {"condition": "食少便溏", "add": ["山药", "莲子肉", "白扁豆"], "remove": [], "note": "健脾止泻"},
        {"condition": "心悸失眠", "add": ["酸枣仁", "远志", "茯神"], "remove": [], "note": "宁心安神"},
        {"condition": "畏寒肢冷", "add": ["附子", "干姜", "肉桂"], "remove": [], "note": "温阳散寒"},
        {"condition": "中气下陷", "add": ["升麻", "柴胡", "黄芪"], "remove": [], "note": "升阳举陷"},
        {"condition": "水肿", "add": ["茯苓", "泽泻", "猪苓"], "remove": [], "note": "利水消肿"},
    ],
    "血虚": [
        {"condition": "出血明显", "add": ["阿胶", "艾叶", "仙鹤草"], "remove": [], "note": "养血止血"},
        {"condition": "失眠多梦", "add": ["酸枣仁", "柏子仁", "龙眼肉"], "remove": [], "note": "养血安神"},
        {"condition": "月经不调", "add": ["香附", "益母草", "丹参"], "remove": [], "note": "活血调经"},
        {"condition": "痛经", "add": ["延胡索", "香附", "川芎"], "remove": [], "note": "活血止痛"},
        {"condition": "兼有气虚", "add": ["人参", "黄芪", "白术"], "remove": [], "note": "补气生血"},
    ],
    "阴虚": [
        {"condition": "骨蒸潮热", "add": ["地骨皮", "银柴胡", "胡黄连"], "remove": [], "note": "清退虚热"},
        {"condition": "盗汗明显", "add": ["浮小麦", "麻黄根", "五味子"], "remove": [], "note": "敛汗固表"},
        {"condition": "口干舌燥", "add": ["麦冬", "天冬", "玉竹"], "remove": [], "note": "生津止渴"},
        {"condition": "视物昏花", "add": ["枸杞子", "菊花", "女贞子"], "remove": [], "note": "养肝明目"},
        {"condition": "遗精滑精", "add": ["金樱子", "芡实", "莲须"], "remove": [], "note": "固精止遗"},
        {"condition": "咳嗽咯血", "add": ["百合", "川贝母", "麦冬"], "remove": [], "note": "润肺止咳"},
    ],
    "阳虚": [
        {"condition": "腰膝冷痛", "add": ["杜仲", "续断", "巴戟天"], "remove": [], "note": "强筋壮骨"},
        {"condition": "阳痿早泄", "add": ["淫羊藿", "巴戟天", "肉苁蓉"], "remove": [], "note": "补肾壮阳"},
        {"condition": "五更泄泻", "add": ["补骨脂", "肉豆蔻", "吴茱萸"], "remove": [], "note": "温肾止泻"},
        {"condition": "水肿明显", "add": ["车前子", "牛膝", "茯苓"], "remove": [], "note": "利水消肿"},
        {"condition": "寒疝腹痛", "add": ["小茴香", "吴茱萸", "乌药"], "remove": [], "note": "暖肝散寒"},
    ],
    "气滞": [
        {"condition": "胁痛明显", "add": ["郁金", "延胡索", "川楝子"], "remove": [], "note": "理气止痛"},
        {"condition": "胃脘胀痛", "add": ["厚朴", "木香", "砂仁"], "remove": [], "note": "理气和胃"},
        {"condition": "嗳气频作", "add": ["旋覆花", "代赭石", "半夏"], "remove": [], "note": "降逆止嗳"},
        {"condition": "乳房胀痛", "add": ["橘叶", "香附", "青皮"], "remove": [], "note": "理气散结"},
        {"condition": "兼有血瘀", "add": ["桃仁", "红花", "当归"], "remove": [], "note": "活血祛瘀"},
    ],
    "血瘀": [
        {"condition": "疼痛剧烈", "add": ["乳香", "没药", "延胡索"], "remove": [], "note": "活血止痛"},
        {"condition": "癥瘕积聚", "add": ["三棱", "莪术", "穿山甲"], "remove": [], "note": "破血消癥"},
        {"condition": "跌打损伤", "add": ["苏木", "自然铜", "血竭"], "remove": [], "note": "活血疗伤"},
        {"condition": "兼有气虚", "add": ["黄芪", "党参", "白术"], "remove": [], "note": "益气活血"},
        {"condition": "兼有寒凝", "add": ["桂枝", "细辛", "附子"], "remove": [], "note": "温经散寒"},
        {"condition": "出血", "add": ["三七", "蒲黄", "茜草"], "remove": [], "note": "活血止血"},
    ],
    "痰湿": [
        {"condition": "咳嗽痰多", "add": ["杏仁", "苏子", "桔梗"], "remove": [], "note": "化痰止咳"},
        {"condition": "眩晕头痛", "add": ["天麻", "白术", "半夏"], "remove": [], "note": "化痰熄风"},
        {"condition": "胸闷喘促", "add": ["葶苈子", "桑白皮", "苏子"], "remove": [], "note": "泻肺平喘"},
        {"condition": "食积不化", "add": ["山楂", "麦芽", "神曲"], "remove": [], "note": "消食化积"},
        {"condition": "兼有热象", "add": ["黄芩", "瓜蒌", "胆南星"], "remove": ["半夏"], "note": "清热化痰"},
    ],
    "湿热": [
        {"condition": "黄疸", "add": ["茵陈", "栀子", "大黄"], "remove": [], "note": "清热利湿退黄"},
        {"condition": "淋浊涩痛", "add": ["石韦", "瞿麦", "萹蓄"], "remove": [], "note": "利尿通淋"},
        {"condition": "带下黄稠", "add": ["黄柏", "车前子", "白果"], "remove": [], "note": "清热止带"},
        {"condition": "湿疹疮疡", "add": ["苦参", "白鲜皮", "地肤子"], "remove": [], "note": "清热燥湿止痒"},
        {"condition": "暑湿", "add": ["藿香", "佩兰", "香薷"], "remove": [], "note": "解暑化湿"},
    ],
}


def get_modification_suggestions(pattern_name: str) -> List[Dict]:
    return MODIFICATION_SUGGESTIONS.get(pattern_name, [])


def compare_formulas(
    original_herbs: Dict[str, Dict],
    modified_herbs: Dict[str, Dict],
) -> Dict:
    original_names = set(original_herbs.keys())
    modified_names = set(modified_herbs.keys())

    added = modified_names - original_names
    removed = original_names - modified_names
    common = original_names & modified_names

    dose_changes = []
    for herb in common:
        orig_dose = original_herbs[herb].get("dose", 0)
        mod_dose = modified_herbs[herb].get("dose", 0)
        orig_unit = original_herbs[herb].get("unit", "克")
        mod_unit = modified_herbs[herb].get("unit", "克")

        if orig_dose != mod_dose or orig_unit != mod_unit:
            dose_changes.append({
                "herb": herb,
                "original_dose": orig_dose,
                "original_unit": orig_unit,
                "modified_dose": mod_dose,
                "modified_unit": mod_unit,
                "change": round(mod_dose - orig_dose, 2),
                "change_percent": round(((mod_dose - orig_dose) / orig_dose * 100) if orig_dose else 0, 1),
            })

    added_details = []
    for herb in added:
        added_details.append({
            "herb": herb,
            "dose": modified_herbs[herb].get("dose", 0),
            "unit": modified_herbs[herb].get("unit", "克"),
            "note": modified_herbs[herb].get("note", ""),
        })

    removed_details = []
    for herb in removed:
        removed_details.append({
            "herb": herb,
            "dose": original_herbs[herb].get("dose", 0),
            "unit": original_herbs[herb].get("unit", "克"),
            "note": original_herbs[herb].get("note", ""),
        })

    return {
        "added": added_details,
        "removed": removed_details,
        "dose_changes": dose_changes,
        "summary": {
            "added_count": len(added),
            "removed_count": len(removed),
            "dose_changed_count": len(dose_changes),
            "total_original": len(original_names),
            "total_modified": len(modified_names),
        },
    }


def add_case_record(
    patient_info: Dict,
    symptoms: List[str],
    tongue: Optional[str],
    pulse: Optional[str],
    patterns: List[Dict],
    selected_formula: Dict,
    original_formula: Dict,
    modified_formula: Dict,
    modification_diff: Dict,
    diagnosis_note: str = "",
    effect_feedback: str = "",
) -> str:
    case_id = str(uuid.uuid4())[:8]
    record = {
        "case_id": case_id,
        "timestamp": int(time.time()),
        "patient": patient_info,
        "symptoms": symptoms,
        "tongue": tongue,
        "pulse": pulse,
        "patterns": patterns,
        "selected_formula": selected_formula,
        "original_formula": original_formula,
        "modified_formula": modified_formula,
        "modification_diff": modification_diff,
        "diagnosis_note": diagnosis_note,
        "effect_feedback": effect_feedback,
    }
    CASE_HISTORY.append(record)
    return case_id


def get_case_record(case_id: str) -> Optional[Dict]:
    for case in CASE_HISTORY:
        if case["case_id"] == case_id:
            return case
    return None


def update_case_feedback(case_id: str, feedback: str) -> bool:
    for case in CASE_HISTORY:
        if case["case_id"] == case_id:
            case["effect_feedback"] = feedback
            return True
    return False


def get_all_cases(limit: int = 100, pattern_filter: Optional[str] = None) -> List[Dict]:
    cases = CASE_HISTORY
    if pattern_filter:
        cases = [
            c for c in cases
            if any(p.get("pattern") == pattern_filter for p in c.get("patterns", []))
        ]
    return sorted(cases, key=lambda x: x["timestamp"], reverse=True)[:limit]


def get_pattern_symptom_frequency(pattern_name: str, top_n: int = 10) -> List[Dict]:
    symptom_counter = Counter()
    case_count = 0

    for case in CASE_HISTORY:
        patterns = case.get("patterns", [])
        if patterns and patterns[0].get("pattern") == pattern_name:
            case_count += 1
            for symptom in case.get("symptoms", []):
                symptom_counter[symptom] += 1

    result = []
    for symptom, count in symptom_counter.most_common(top_n):
        result.append({
            "symptom": symptom,
            "count": count,
            "frequency": round(count / case_count * 100, 1) if case_count else 0,
        })

    return result


def get_top_symptom_combinations(pattern_name: str, top_n: int = 5, combo_size: int = 3) -> List[Dict]:
    combo_counter = Counter()
    case_count = 0

    for case in CASE_HISTORY:
        patterns = case.get("patterns", [])
        if patterns and patterns[0].get("pattern") == pattern_name:
            case_count += 1
            symptoms = sorted(case.get("symptoms", []))
            if len(symptoms) >= combo_size:
                from itertools import combinations
                for combo in combinations(symptoms, combo_size):
                    combo_counter[combo] += 1

    result = []
    for combo, count in combo_counter.most_common(top_n):
        result.append({
            "symptoms": list(combo),
            "count": count,
            "frequency": round(count / case_count * 100, 1) if case_count else 0,
        })

    return result


def get_pattern_statistics() -> List[Dict]:
    pattern_counter = Counter()
    for case in CASE_HISTORY:
        patterns = case.get("patterns", [])
        if patterns:
            pattern_counter[patterns[0].get("pattern", "未知")] += 1

    total = sum(pattern_counter.values())
    result = []
    for pattern, count in pattern_counter.most_common():
        result.append({
            "pattern": pattern,
            "count": count,
            "percentage": round(count / total * 100, 1) if total else 0,
        })

    return result


def get_case_count() -> int:
    return len(CASE_HISTORY)
