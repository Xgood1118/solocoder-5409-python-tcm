from typing import Dict, Any, Optional
from .config import QIAN_TO_GRAM, STANDARD_WEIGHT, ADULT_AGE, ELDERLY_AGE


UNIT_NORMALIZE_MAP = {
    "錢": "钱",
    "錢重": "钱",
    "克": "克",
    "公克": "克",
    "g": "克",
    "G": "克",
}


def normalize_unit(unit: str) -> str:
    return UNIT_NORMALIZE_MAP.get(unit, unit)


def qian_to_gram(qian: float) -> float:
    return round(qian * QIAN_TO_GRAM, 2)


def gram_to_qian(gram: float) -> float:
    return round(gram / QIAN_TO_GRAM, 2)


def convert_dose(dose: float, from_unit: str, to_unit: str) -> float:
    from_unit_norm = normalize_unit(from_unit)
    to_unit_norm = normalize_unit(to_unit)
    if from_unit_norm == to_unit_norm:
        return dose
    if from_unit_norm == "钱" and to_unit_norm == "克":
        return qian_to_gram(dose)
    if from_unit_norm == "克" and to_unit_norm == "钱":
        return gram_to_qian(dose)
    return dose


def calculate_dose_factor(
    age: Optional[float] = None,
    weight: Optional[float] = None,
    is_pregnant: bool = False,
    is_lactating: bool = False,
) -> float:
    factor = 1.0

    if age is not None:
        if age < ADULT_AGE:
            if age <= 1:
                factor = 0.15
            elif age <= 3:
                factor = 0.25
            elif age <= 6:
                factor = 0.4
            elif age <= 10:
                factor = 0.5
            else:
                factor = 0.7
        elif age >= ELDERLY_AGE:
            factor = 0.8

    if weight is not None and age is not None and age < ADULT_AGE:
        weight_factor = weight / STANDARD_WEIGHT
        factor = max(factor, weight_factor * 0.8)

    return round(factor, 2)


def adjust_herb_doses(
    herbs: Dict[str, Dict[str, Any]],
    dose_factor: float,
    target_unit: str = "克",
) -> Dict[str, Dict[str, Any]]:
    result = {}
    for herb_name, herb_info in herbs.items():
        original_dose = herb_info.get("dose", 0)
        original_unit = herb_info.get("unit", "克")
        converted_dose = convert_dose(original_dose, original_unit, target_unit)
        adjusted_dose = round(converted_dose * dose_factor, 2)
        result[herb_name] = {
            **herb_info,
            "dose": adjusted_dose,
            "unit": target_unit,
            "original_dose": original_dose,
            "original_unit": original_unit,
        }
    return result
