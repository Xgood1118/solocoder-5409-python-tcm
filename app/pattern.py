from typing import Dict, List, Optional, Tuple
from .config import DEFAULT_PATTERN_THRESHOLD, TOP_N_PATTERNS


PATTERNS: Dict[str, Dict] = {
    "气虚": {
        "description": "元气不足，脏腑功能减退",
        "threshold": DEFAULT_PATTERN_THRESHOLD,
        "symptom_weights": {
            "乏力": 25,
            "气短": 20,
            "自汗": 15,
            "头晕": 10,
            "面色萎黄": 10,
            "食欲不振": 12,
            "便溏": 10,
            "心悸": 8,
            "舌淡": 15,
            "脉弱": 20,
            "脉虚": 15,
            "脉细": 10,
        },
        "tongue_pulse_boost": {
            ("舌淡", "脉弱"): 20,
            ("舌淡", "脉虚"): 18,
            ("舌淡胖有齿痕", "脉弱"): 22,
        },
    },
    "血虚": {
        "description": "血液亏虚，脏腑百脉失养",
        "threshold": DEFAULT_PATTERN_THRESHOLD,
        "symptom_weights": {
            "头晕": 20,
            "心悸": 20,
            "失眠": 15,
            "多梦": 12,
            "面色萎黄": 18,
            "面色苍白": 20,
            "乏力": 15,
            "月经不调": 15,
            "舌淡": 15,
            "舌淡白": 18,
            "脉细": 20,
            "脉细弱": 22,
        },
        "tongue_pulse_boost": {
            ("舌淡白", "脉细"): 20,
            ("舌淡", "脉细弱"): 22,
        },
    },
    "阴虚": {
        "description": "阴液亏损，虚热内生",
        "threshold": DEFAULT_PATTERN_THRESHOLD,
        "symptom_weights": {
            "五心烦热": 25,
            "潮热": 22,
            "盗汗": 20,
            "口干": 18,
            "失眠": 15,
            "多梦": 10,
            "头晕": 12,
            "耳鸣": 15,
            "腰膝酸软": 15,
            "舌红": 18,
            "舌红少苔": 25,
            "脉细数": 25,
            "脉细": 10,
            "脉数": 12,
        },
        "tongue_pulse_boost": {
            ("舌红少苔", "脉细数"): 30,
            ("舌红", "脉细数"): 25,
        },
    },
    "阳虚": {
        "description": "阳气虚衰，温煦失职",
        "threshold": DEFAULT_PATTERN_THRESHOLD,
        "symptom_weights": {
            "畏寒": 25,
            "四肢不温": 22,
            "怕冷": 20,
            "腰膝酸软": 15,
            "乏力": 15,
            "便溏": 12,
            "小便清长": 15,
            "面色苍白": 12,
            "舌淡胖": 20,
            "舌淡胖有齿痕": 25,
            "脉沉迟": 25,
            "脉沉细": 15,
            "脉弱": 12,
        },
        "tongue_pulse_boost": {
            ("舌淡胖有齿痕", "脉沉迟"): 30,
            ("舌淡胖", "脉沉迟"): 25,
        },
    },
    "气滞": {
        "description": "气机郁滞，运行不畅",
        "threshold": DEFAULT_PATTERN_THRESHOLD,
        "symptom_weights": {
            "胁肋胀痛": 25,
            "胸胁胀满": 20,
            "善太息": 18,
            "情绪抑郁": 20,
            "烦躁易怒": 15,
            "胸闷": 18,
            "腹胀": 15,
            "月经不调": 12,
            "痛经": 15,
            "脉弦": 22,
        },
        "tongue_pulse_boost": {
            ("舌淡红", "脉弦"): 15,
        },
    },
    "血瘀": {
        "description": "瘀血内阻，血行不畅",
        "threshold": DEFAULT_PATTERN_THRESHOLD,
        "symptom_weights": {
            "胸胁刺痛": 25,
            "痛有定处": 22,
            "痛经": 18,
            "肌肤甲错": 20,
            "面色晦暗": 18,
            "月经不调": 12,
            "舌紫暗": 22,
            "舌紫暗有瘀点": 28,
            "舌紫暗有瘀斑": 30,
            "脉涩": 25,
            "脉涩结": 28,
        },
        "tongue_pulse_boost": {
            ("舌紫暗有瘀点", "脉涩"): 30,
            ("舌紫暗有瘀斑", "脉涩"): 32,
        },
    },
    "痰湿": {
        "description": "痰湿内蕴，阻滞气机",
        "threshold": DEFAULT_PATTERN_THRESHOLD,
        "symptom_weights": {
            "身体困重": 22,
            "胸闷": 20,
            "痰多": 25,
            "恶心": 15,
            "呕吐": 12,
            "腹胀": 15,
            "食欲不振": 12,
            "便溏": 10,
            "带下量多": 15,
            "舌苔厚腻": 25,
            "舌苔白腻": 22,
            "脉滑": 22,
            "脉濡缓": 15,
        },
        "tongue_pulse_boost": {
            ("舌苔白腻", "脉滑"): 25,
            ("舌苔厚腻", "脉滑"): 28,
        },
    },
    "湿热": {
        "description": "湿热蕴结，气机不畅",
        "threshold": DEFAULT_PATTERN_THRESHOLD,
        "symptom_weights": {
            "口苦": 20,
            "口干": 15,
            "胸闷": 15,
            "腹胀": 12,
            "食欲不振": 10,
            "大便黏腻": 18,
            "带下量多": 15,
            "带下黄稠": 20,
            "舌红": 12,
            "舌红苔黄腻": 28,
            "脉滑数": 25,
            "脉濡数": 20,
        },
        "tongue_pulse_boost": {
            ("舌红苔黄腻", "脉滑数"): 30,
        },
    },
}


def calculate_pattern_scores(
    symptoms: List[str],
    tongue: Optional[str] = None,
    pulse: Optional[str] = None,
    custom_weights: Optional[Dict[str, Dict[str, float]]] = None,
    custom_thresholds: Optional[Dict[str, float]] = None,
) -> List[Dict]:
    all_symptoms = list(dict.fromkeys(symptoms))
    if tongue and tongue not in all_symptoms:
        all_symptoms.append(tongue)
    if pulse and pulse not in all_symptoms:
        all_symptoms.append(pulse)

    results = []

    for pattern_name, pattern_info in PATTERNS.items():
        total_score = 0.0
        matched_symptoms = []
        seen_symptoms = set()

        weights = pattern_info["symptom_weights"].copy()
        if custom_weights and pattern_name in custom_weights:
            weights.update(custom_weights[pattern_name])

        threshold = pattern_info.get("threshold", DEFAULT_PATTERN_THRESHOLD)
        if custom_thresholds and pattern_name in custom_thresholds:
            threshold = custom_thresholds[pattern_name]

        for symptom in all_symptoms:
            if symptom in weights and symptom not in seen_symptoms:
                score = weights[symptom]
                total_score += score
                matched_symptoms.append({
                    "symptom": symptom,
                    "score": score,
                })
                seen_symptoms.add(symptom)

        boost_score = 0.0
        boost_info = None
        if tongue and pulse:
            for (t_key, p_key), boost in pattern_info.get("tongue_pulse_boost", {}).items():
                if t_key == tongue and p_key == pulse:
                    boost_score = boost
                    boost_info = {
                        "tongue": tongue,
                        "pulse": pulse,
                        "boost": boost,
                    }
                    total_score += boost_score
                    break

        results.append({
            "pattern": pattern_name,
            "description": pattern_info["description"],
            "total_score": total_score,
            "threshold": threshold,
            "matched": total_score >= threshold,
            "matched_symptoms": matched_symptoms,
            "boost": boost_info,
        })

    results.sort(key=lambda x: x["total_score"], reverse=True)

    return results


def get_top_patterns(
    symptoms: List[str],
    tongue: Optional[str] = None,
    pulse: Optional[str] = None,
    top_n: int = TOP_N_PATTERNS,
    custom_weights: Optional[Dict[str, Dict[str, float]]] = None,
    custom_thresholds: Optional[Dict[str, float]] = None,
) -> List[Dict]:
    all_results = calculate_pattern_scores(
        symptoms, tongue, pulse, custom_weights, custom_thresholds
    )
    return all_results[:top_n]


def get_all_patterns() -> List[Dict]:
    result = []
    for name, info in PATTERNS.items():
        result.append({
            "name": name,
            "description": info["description"],
            "threshold": info["threshold"],
            "symptom_count": len(info["symptom_weights"]),
        })
    return result


def get_pattern_detail(pattern_name: str) -> Optional[Dict]:
    if pattern_name not in PATTERNS:
        return None
    pattern = PATTERNS[pattern_name]
    return {
        "name": pattern_name,
        "description": pattern["description"],
        "threshold": pattern["threshold"],
        "symptom_weights": pattern["symptom_weights"],
        "tongue_pulse_boost": pattern.get("tongue_pulse_boost", {}),
    }


def update_pattern_weights(pattern_name: str, weights: Dict[str, float]) -> bool:
    if pattern_name not in PATTERNS:
        return False
    PATTERNS[pattern_name]["symptom_weights"].update(weights)
    return True


def update_pattern_threshold(pattern_name: str, threshold: float) -> bool:
    if pattern_name not in PATTERNS:
        return False
    PATTERNS[pattern_name]["threshold"] = threshold
    return True
