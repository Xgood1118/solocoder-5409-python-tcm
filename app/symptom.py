from typing import Dict, List, Optional, Set


SYMPTOM_DICT: Dict[str, Dict] = {
    "乏力": {"category": "全身症状", "description": "自觉疲倦无力"},
    "自汗": {"category": "汗症", "description": "不因劳累活动而自然汗出"},
    "盗汗": {"category": "汗症", "description": "入睡后汗出，醒后汗止"},
    "气短": {"category": "呼吸", "description": "呼吸短促"},
    "心悸": {"category": "心系", "description": "心中悸动不安"},
    "失眠": {"category": "睡眠", "description": "难以入睡或易醒"},
    "多梦": {"category": "睡眠", "description": "睡眠中梦多纷扰"},
    "头晕": {"category": "头面", "description": "头昏目眩"},
    "头痛": {"category": "头面", "description": "头部疼痛"},
    "面色萎黄": {"category": "面色", "description": "面色黄而无光泽"},
    "面色苍白": {"category": "面色", "description": "面色白而无华"},
    "面色晦暗": {"category": "面色", "description": "面色暗而无光"},
    "食欲不振": {"category": "脾胃", "description": "不欲饮食，食量减少"},
    "腹胀": {"category": "脾胃", "description": "腹部胀满不适"},
    "便溏": {"category": "脾胃", "description": "大便稀溏不成形"},
    "便秘": {"category": "脾胃", "description": "大便干结难解"},
    "口干": {"category": "津液", "description": "口中干燥少津"},
    "口苦": {"category": "津液", "description": "口中有苦味"},
    "口渴": {"category": "津液", "description": "口渴欲饮"},
    "五心烦热": {"category": "热证", "description": "手足心热兼心中烦热"},
    "潮热": {"category": "热证", "description": "按时发热或按时热甚"},
    "畏寒": {"category": "寒证", "description": "自觉怕冷，得温则减"},
    "怕冷": {"category": "寒证", "description": "怕冷，加衣被不解"},
    "四肢不温": {"category": "寒证", "description": "手足不温"},
    "腰膝酸软": {"category": "肾系", "description": "腰部酸软无力"},
    "耳鸣": {"category": "肾系", "description": "耳中鸣响"},
    "脱发": {"category": "肾系", "description": "头发脱落"},
    "胁肋胀痛": {"category": "肝系", "description": "胁肋部胀满疼痛"},
    "善太息": {"category": "肝系", "description": "时时叹气"},
    "情绪抑郁": {"category": "情志", "description": "情绪低落抑郁"},
    "烦躁易怒": {"category": "情志", "description": "心烦急躁易怒"},
    "胸胁刺痛": {"category": "血瘀", "description": "胸胁部刺痛固定"},
    "痛有定处": {"category": "血瘀", "description": "疼痛部位固定不移"},
    "肌肤甲错": {"category": "血瘀", "description": "皮肤粗糙如鳞甲"},
    "身体困重": {"category": "湿证", "description": "身体沉重困乏"},
    "胸闷": {"category": "胸肺", "description": "胸中满闷不舒"},
    "痰多": {"category": "痰证", "description": "痰液较多"},
    "恶心": {"category": "脾胃", "description": "胃中不适欲吐"},
    "呕吐": {"category": "脾胃", "description": "胃内容物上逆而出"},
    "带下量多": {"category": "妇科", "description": "白带量多"},
    "月经不调": {"category": "妇科", "description": "月经周期紊乱"},
    "痛经": {"category": "妇科", "description": "经期腹痛"},
}


SYNONYM_MAP: Dict[str, str] = {
    "没劲儿": "乏力",
    "浑身没劲": "乏力",
    "浑身无力": "乏力",
    "疲倦": "乏力",
    "疲乏": "乏力",
    "倦怠": "乏力",
    "睡不着": "失眠",
    "睡不好": "失眠",
    "睡眠差": "失眠",
    "入睡难": "失眠",
    "易醒": "失眠",
    "老做梦": "多梦",
    "梦多": "多梦",
    "头昏": "头晕",
    "眩晕": "头晕",
    "头昏眼花": "头晕",
    "头疼": "头痛",
    "脑袋疼": "头痛",
    "不想吃饭": "食欲不振",
    "没胃口": "食欲不振",
    "食少": "食欲不振",
    "纳差": "食欲不振",
    "肚子胀": "腹胀",
    "肚子痛": "腹痛",
    "拉肚子": "便溏",
    "拉稀": "便溏",
    "大便稀": "便溏",
    "大便干": "便秘",
    "大便干结": "便秘",
    "嘴里干": "口干",
    "口干舌燥": "口干",
    "嘴里苦": "口苦",
    "口渴": "口渴",
    "嗓子干": "口干",
    "心里烦": "烦躁",
    "爱生气": "烦躁易怒",
    "脾气大": "烦躁易怒",
    "爱叹气": "善太息",
    "叹气多": "善太息",
    "腰困": "腰膝酸软",
    "腰酸": "腰膝酸软",
    "腰疼": "腰膝酸软",
    "怕冷": "畏寒",
    "手脚凉": "四肢不温",
    "手脚冰凉": "四肢不温",
    "手脚不温": "四肢不温",
    "身上沉": "身体困重",
    "身体沉重": "身体困重",
    "胸口闷": "胸闷",
    "胸满": "胸闷",
}


TONGUE_PRESETS: List[Dict] = [
    {"name": "舌淡红苔薄白", "tongue_color": "淡红", "tongue_coating": "薄白", "description": "正常舌象"},
    {"name": "舌淡苔白", "tongue_color": "淡", "tongue_coating": "白", "description": "气血不足"},
    {"name": "舌淡胖有齿痕苔白腻", "tongue_color": "淡胖有齿痕", "tongue_coating": "白腻", "description": "脾虚湿盛"},
    {"name": "舌红少苔", "tongue_color": "红", "tongue_coating": "少苔", "description": "阴虚内热"},
    {"name": "舌红苔黄腻", "tongue_color": "红", "tongue_coating": "黄腻", "description": "湿热内蕴"},
    {"name": "舌红苔黄燥", "tongue_color": "红", "tongue_coating": "黄燥", "description": "热盛伤津"},
    {"name": "舌紫暗有瘀点", "tongue_color": "紫暗有瘀点", "tongue_coating": "薄白", "description": "瘀血内阻"},
    {"name": "舌紫暗有瘀斑", "tongue_color": "紫暗有瘀斑", "tongue_coating": "薄白", "description": "瘀血较重"},
    {"name": "舌淡紫苔白滑", "tongue_color": "淡紫", "tongue_coating": "白滑", "description": "阳虚寒凝血瘀"},
    {"name": "舌红绛少苔", "tongue_color": "红绛", "tongue_coating": "少苔", "description": "热入营血"},
    {"name": "舌淡白苔薄白", "tongue_color": "淡白", "tongue_coating": "薄白", "description": "气血两虚"},
    {"name": "舌苔厚腻", "tongue_color": "淡红", "tongue_coating": "厚腻", "description": "痰湿内阻"},
]


PULSE_PRESETS: List[Dict] = [
    {"name": "脉浮", "pulse_type": "浮", "description": "表证"},
    {"name": "脉沉", "pulse_type": "沉", "description": "里证"},
    {"name": "脉迟", "pulse_type": "迟", "description": "寒证"},
    {"name": "脉数", "pulse_type": "数", "description": "热证"},
    {"name": "脉虚", "pulse_type": "虚", "description": "虚证"},
    {"name": "脉实", "pulse_type": "实", "description": "实证"},
    {"name": "脉细", "pulse_type": "细", "description": "气血不足"},
    {"name": "脉弱", "pulse_type": "弱", "description": "气虚"},
    {"name": "脉滑", "pulse_type": "滑", "description": "痰湿、食积"},
    {"name": "脉涩", "pulse_type": "涩", "description": "血瘀"},
    {"name": "脉弦", "pulse_type": "弦", "description": "肝胆病、痛证"},
    {"name": "脉细数", "pulse_type": "细数", "description": "阴虚内热"},
    {"name": "脉沉迟", "pulse_type": "沉迟", "description": "阳虚里寒"},
    {"name": "脉沉细", "pulse_type": "沉细", "description": "气血不足、肾阳虚"},
    {"name": "脉浮数", "pulse_type": "浮数", "description": "表热证"},
    {"name": "脉滑数", "pulse_type": "滑数", "description": "痰热、湿热"},
    {"name": "脉弦滑", "pulse_type": "弦滑", "description": "肝郁痰浊"},
    {"name": "脉涩结", "pulse_type": "涩结", "description": "血瘀气滞"},
    {"name": "脉洪大", "pulse_type": "洪大", "description": "热盛"},
    {"name": "脉濡缓", "pulse_type": "濡缓", "description": "湿证"},
]


def normalize_symptom(symptom_name: str) -> str:
    return SYNONYM_MAP.get(symptom_name, symptom_name)


def normalize_symptoms(symptom_list: List[str]) -> List[str]:
    normalized = set()
    for s in symptom_list:
        s = s.strip()
        if s:
            normalized.add(normalize_symptom(s))
    return sorted(list(normalized))


def get_all_symptoms() -> List[Dict]:
    result = []
    for name, info in SYMPTOM_DICT.items():
        result.append({"name": name, **info})
    return result


def get_tongue_presets() -> List[Dict]:
    return TONGUE_PRESETS


def get_pulse_presets() -> List[Dict]:
    return PULSE_PRESETS


def get_synonyms(symptom_name: str) -> List[str]:
    result = []
    for synonym, canonical in SYNONYM_MAP.items():
        if canonical == symptom_name:
            result.append(synonym)
    return result


def add_synonym(synonym: str, canonical: str) -> bool:
    if canonical not in SYMPTOM_DICT:
        return False
    SYNONYM_MAP[synonym] = canonical
    return True
