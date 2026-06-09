from typing import Dict, List, Optional
from .utils import adjust_herb_doses, convert_dose


FORMULARY: Dict[str, List[Dict]] = {
    "气虚": [
        {
            "name": "四君子汤",
            "source": "《太平惠民和剂局方》",
            "category": "补气",
            "herbs": {
                "人参": {"dose": 9, "unit": "克", "note": "君药"},
                "白术": {"dose": 9, "unit": "克", "note": "臣药"},
                "茯苓": {"dose": 9, "unit": "克", "note": "佐药"},
                "炙甘草": {"dose": 6, "unit": "克", "note": "使药"},
            },
            "preparation": "水煎服，每日一剂，分两次温服。",
            "indication": "脾胃气虚证。面色萎白，语声低微，气短乏力，食少便溏，舌淡苔白，脉虚弱。",
            "modifications": [
                "呕吐加半夏、生姜降逆止呕",
                "胸膈痞满加枳壳、陈皮理气宽胸",
                "心悸失眠加酸枣仁、远志宁心安神",
                "畏寒肢冷加附子、干姜温阳散寒",
            ],
        },
        {
            "name": "补中益气汤",
            "source": "《脾胃论》",
            "category": "补气升阳",
            "herbs": {
                "黄芪": {"dose": 18, "unit": "克", "note": "君药"},
                "人参": {"dose": 6, "unit": "克", "note": "臣药"},
                "白术": {"dose": 9, "unit": "克", "note": "臣药"},
                "炙甘草": {"dose": 9, "unit": "克", "note": "佐使药"},
                "当归": {"dose": 3, "unit": "克", "note": "佐药"},
                "陈皮": {"dose": 6, "unit": "克", "note": "佐药"},
                "升麻": {"dose": 3, "unit": "克", "note": "佐药"},
                "柴胡": {"dose": 3, "unit": "克", "note": "佐药"},
            },
            "preparation": "水煎服，每日一剂，空腹稍热服。",
            "indication": "脾虚气陷证。饮食减少，体倦肢软，少气懒言，面色萎黄，大便稀溏，舌淡，脉虚；以及脱肛、子宫脱垂、久泻久痢、崩漏等。",
            "modifications": [
                "下陷较甚加枳壳、葛根增强升提之力",
                "兼有血瘀加丹参、红花活血化瘀",
                "气虚甚者重用人参、黄芪",
                "纳差加焦三仙、砂仁开胃消食",
            ],
        },
        {
            "name": "参苓白术散",
            "source": "《太平惠民和剂局方》",
            "category": "益气健脾渗湿",
            "herbs": {
                "人参": {"dose": 15, "unit": "克", "note": "君药"},
                "白术": {"dose": 15, "unit": "克", "note": "君药"},
                "茯苓": {"dose": 15, "unit": "克", "note": "君药"},
                "山药": {"dose": 15, "unit": "克", "note": "臣药"},
                "莲子肉": {"dose": 9, "unit": "克", "note": "臣药"},
                "白扁豆": {"dose": 12, "unit": "克", "note": "臣药"},
                "薏苡仁": {"dose": 9, "unit": "克", "note": "佐药"},
                "缩砂仁": {"dose": 6, "unit": "克", "note": "佐药"},
                "桔梗": {"dose": 6, "unit": "克", "note": "佐药"},
                "炙甘草": {"dose": 9, "unit": "克", "note": "佐使药"},
            },
            "preparation": "共为细末，每服6克，枣汤调下，每日2-3次。或水煎服。",
            "indication": "脾虚湿盛证。饮食不化，胸脘痞闷，肠鸣泄泻，四肢乏力，形体消瘦，面色萎黄，舌淡苔白腻，脉虚缓。",
            "modifications": [
                "泄泻甚者加肉豆蔻、诃子涩肠止泻",
                "兼有寒象加干姜、附子温中散寒",
                "食欲不振加焦三仙开胃消食",
                "湿重加苍术、厚朴燥湿健脾",
            ],
        },
    ],
    "血虚": [
        {
            "name": "四物汤",
            "source": "《太平惠民和剂局方》",
            "category": "补血调血",
            "herbs": {
                "当归": {"dose": 9, "unit": "克", "note": "君药"},
                "川芎": {"dose": 6, "unit": "克", "note": "佐药"},
                "白芍": {"dose": 9, "unit": "克", "note": "臣药"},
                "熟地黄": {"dose": 12, "unit": "克", "note": "君药"},
            },
            "preparation": "水煎服，每日一剂，分两次温服。",
            "indication": "营血虚滞证。头晕目眩，心悸失眠，面色无华，妇人月经不调，量少或经闭不行，脐腹作痛，舌淡，脉细弦或细涩。",
            "modifications": [
                "兼气虚加人参、黄芪补气生血",
                "兼有血瘀加桃仁、红花活血祛瘀",
                "血虚有热加黄芩、丹皮清热凉血",
                "虚寒明显加桂枝、艾叶温经散寒",
            ],
        },
        {
            "name": "当归补血汤",
            "source": "《内外伤辨惑论》",
            "category": "补气生血",
            "herbs": {
                "黄芪": {"dose": 30, "unit": "克", "note": "君药"},
                "当归": {"dose": 6, "unit": "克", "note": "臣药"},
            },
            "preparation": "水煎服，每日一剂，空腹温服。",
            "indication": "血虚阳浮发热证。肌热面赤，烦渴欲饮，脉洪大而虚，重按无力。亦治妇人经期、产后血虚发热头痛；或疮疡溃后，久不愈合者。",
            "modifications": [
                "妇人经期加香附、益母草调经养血",
                "疮疡久不愈合加金银花、连翘清热解毒",
                "心悸失眠加酸枣仁、远志宁心安神",
                "出血明显加阿胶、艾叶养血止血",
            ],
        },
        {
            "name": "归脾汤",
            "source": "《正体类要》",
            "category": "益气补血健脾养心",
            "herbs": {
                "白术": {"dose": 9, "unit": "克", "note": ""},
                "茯神": {"dose": 9, "unit": "克", "note": ""},
                "黄芪": {"dose": 12, "unit": "克", "note": "君药"},
                "龙眼肉": {"dose": 12, "unit": "克", "note": "君药"},
                "酸枣仁": {"dose": 12, "unit": "克", "note": ""},
                "人参": {"dose": 6, "unit": "克", "note": ""},
                "木香": {"dose": 6, "unit": "克", "note": ""},
                "炙甘草": {"dose": 3, "unit": "克", "note": ""},
                "当归": {"dose": 9, "unit": "克", "note": ""},
                "远志": {"dose": 6, "unit": "克", "note": ""},
            },
            "preparation": "加生姜、大枣，水煎服，每日一剂。",
            "indication": "心脾气血两虚证。心悸怔忡，健忘失眠，盗汗虚热，体倦食少，面色萎黄，舌淡，苔薄白，脉细弱。脾不统血证。便血，皮下紫癜，妇女崩漏，月经超前，量多色淡，或淋漓不止，舌淡，脉细弱。",
            "modifications": [
                "崩漏下血加艾叶炭、阿胶珠养血止血",
                "失眠重者加五味子、夜交藤安神",
                "血虚甚加熟地黄、白芍养血",
                "脾虚甚加重白术、茯苓健脾",
            ],
        },
    ],
    "阴虚": [
        {
            "name": "六味地黄丸",
            "source": "《小儿药证直诀》",
            "category": "滋阴补肾",
            "herbs": {
                "熟地黄": {"dose": 24, "unit": "克", "note": "君药"},
                "山茱萸": {"dose": 12, "unit": "克", "note": "臣药"},
                "干山药": {"dose": 12, "unit": "克", "note": "臣药"},
                "泽泻": {"dose": 9, "unit": "克", "note": "佐药"},
                "牡丹皮": {"dose": 9, "unit": "克", "note": "佐药"},
                "茯苓": {"dose": 9, "unit": "克", "note": "佐药"},
            },
            "preparation": "共为细末，炼蜜为丸，每丸9克，每次1丸，每日2-3次，空腹温水送服。或水煎服。",
            "indication": "肝肾阴虚证。腰膝酸软，头晕目眩，耳鸣耳聋，盗汗，遗精，消渴，骨蒸潮热，手足心热，口燥咽干，牙齿动摇，足跟作痛，小便淋沥，以及小儿囟门不合，舌红少苔，脉沉细数。",
            "modifications": [
                "虚火甚者加知母、黄柏清热降火（知柏地黄丸）",
                "肺阴虚加麦冬、五味子养阴敛肺（麦味地黄丸）",
                "肝阴虚加枸杞、菊花养肝明目（杞菊地黄丸）",
                "视物昏花加当归、白芍养肝明目",
            ],
        },
        {
            "name": "知柏地黄丸",
            "source": "《医宗金鉴》",
            "category": "滋阴降火",
            "herbs": {
                "知母": {"dose": 6, "unit": "克", "note": ""},
                "黄柏": {"dose": 6, "unit": "克", "note": ""},
                "熟地黄": {"dose": 24, "unit": "克", "note": "君药"},
                "山茱萸": {"dose": 12, "unit": "克", "note": ""},
                "干山药": {"dose": 12, "unit": "克", "note": ""},
                "泽泻": {"dose": 9, "unit": "克", "note": ""},
                "牡丹皮": {"dose": 9, "unit": "克", "note": ""},
                "茯苓": {"dose": 9, "unit": "克", "note": ""},
            },
            "preparation": "共为细末，炼蜜为丸，每服9克，每日2次，空腹温水送服。或水煎服。",
            "indication": "肝肾阴虚，虚火上炎证。头目昏眩，耳鸣耳聋，虚火牙痛，五心烦热，腰膝酸痛，血淋尿痛，遗精梦泄，骨蒸潮热，盗汗颧红，咽干口燥，舌质红，脉细数。",
            "modifications": [
                "盗汗甚者加浮小麦、麻黄根敛汗",
                "遗精甚者加金樱子、芡实固精",
                "骨蒸潮热加地骨皮、银柴胡清虚热",
                "口干舌燥加麦冬、玉竹生津止渴",
            ],
        },
        {
            "name": "一贯煎",
            "source": "《续名医类案》",
            "category": "滋阴疏肝",
            "herbs": {
                "北沙参": {"dose": 9, "unit": "克", "note": ""},
                "麦冬": {"dose": 9, "unit": "克", "note": ""},
                "当归身": {"dose": 9, "unit": "克", "note": ""},
                "生地黄": {"dose": 30, "unit": "克", "note": "君药"},
                "枸杞子": {"dose": 12, "unit": "克", "note": ""},
                "川楝子": {"dose": 5, "unit": "克", "note": "佐药"},
            },
            "preparation": "水煎服，每日一剂，分两次温服。",
            "indication": "肝肾阴虚，肝气郁滞证。胸脘胁痛，吞酸吐苦，咽干口燥，舌红少津，脉细弱或虚弦。亦治疝气瘕聚。",
            "modifications": [
                "口苦干燥加黄连、天花粉清热生津",
                "胁痛甚加白芍、甘草柔肝缓急",
                "失眠多梦加酸枣仁、合欢皮安神",
                "大便秘结加瓜蒌仁、火麻仁润肠通便",
            ],
        },
    ],
    "阳虚": [
        {
            "name": "肾气丸",
            "source": "《金匮要略》",
            "category": "补肾助阳",
            "herbs": {
                "干地黄": {"dose": 24, "unit": "克", "note": "君药"},
                "山药": {"dose": 12, "unit": "克", "note": ""},
                "山茱萸": {"dose": 12, "unit": "克", "note": ""},
                "泽泻": {"dose": 9, "unit": "克", "note": ""},
                "茯苓": {"dose": 9, "unit": "克", "note": ""},
                "牡丹皮": {"dose": 9, "unit": "克", "note": ""},
                "桂枝": {"dose": 3, "unit": "克", "note": "臣药"},
                "附子": {"dose": 3, "unit": "克", "note": "臣药"},
            },
            "preparation": "共为细末，炼蜜为丸，每服6-9克，每日2次，酒或温水送服。或水煎服。",
            "indication": "肾阳不足证。腰痛脚软，身半以下常有冷感，少腹拘急，小便不利，或小便反多，入夜尤甚，阳痿早泄，舌淡而胖，脉虚弱，尺部沉细或沉弱而迟，以及痰饮、水肿、消渴、脚气、转胞等。",
            "modifications": [
                "阳痿早泄加淫羊藿、巴戟天补肾壮阳",
                "水肿明显加车前子、牛膝利水消肿（济生肾气丸）",
                "腰膝冷痛甚者加杜仲、续断强筋壮骨",
                "五更泄泻加肉豆蔻、补骨脂温肾止泻",
            ],
        },
        {
            "name": "右归丸",
            "source": "《景岳全书》",
            "category": "温补肾阳填精益髓",
            "herbs": {
                "熟地黄": {"dose": 24, "unit": "克", "note": "君药"},
                "山药": {"dose": 12, "unit": "克", "note": ""},
                "山茱萸": {"dose": 9, "unit": "克", "note": ""},
                "枸杞子": {"dose": 12, "unit": "克", "note": ""},
                "菟丝子": {"dose": 12, "unit": "克", "note": ""},
                "鹿角胶": {"dose": 12, "unit": "克", "note": "君药"},
                "杜仲": {"dose": 12, "unit": "克", "note": ""},
                "肉桂": {"dose": 6, "unit": "克", "note": ""},
                "当归": {"dose": 9, "unit": "克", "note": ""},
                "制附子": {"dose": 6, "unit": "克", "note": ""},
            },
            "preparation": "共为细末，炼蜜为丸，每丸9克，每次1丸，每日2-3次，淡盐水送服。或水煎服。",
            "indication": "肾阳不足，命门火衰证。年老或久病气衰神疲，畏寒肢冷，腰膝软弱，阳痿遗精，或阳衰无子，或饮食减少，大便不实，或小便自遗，舌淡苔白，脉沉而迟。",
            "modifications": [
                "阳虚精滑或带浊便溏加补骨脂、金樱子固精止遗",
                "飧泄肾泄不止加五味子、肉豆蔻涩肠止泻",
                "腹痛不止加吴茱萸、小茴香温中止痛",
                "腰膝酸痛加怀牛膝、桑寄生强筋健骨",
            ],
        },
        {
            "name": "四逆汤",
            "source": "《伤寒论》",
            "category": "回阳救逆",
            "herbs": {
                "附子": {"dose": 15, "unit": "克", "note": "君药"},
                "干姜": {"dose": 9, "unit": "克", "note": "臣药"},
                "炙甘草": {"dose": 6, "unit": "克", "note": "佐使药"},
            },
            "preparation": "水煎服，附子先煎30-60分钟，每日一剂，分两次温服。",
            "indication": "少阴病，心肾阳衰寒厥证。四肢厥逆，恶寒蜷卧，神衰欲寐，面色苍白，腹痛下利，呕吐不渴，舌苔白滑，脉微细。",
            "modifications": [
                "兼气虚加人参益气固脱（四逆加人参汤）",
                "阴盛格阳加葱白宣通阳气（白通汤）",
                "阳气暴脱加重附子、干姜用量",
                "寒凝经脉加桂枝、细辛温经散寒",
            ],
        },
    ],
    "气滞": [
        {
            "name": "柴胡疏肝散",
            "source": "《证治准绳》",
            "category": "疏肝行气活血止痛",
            "herbs": {
                "柴胡": {"dose": 6, "unit": "克", "note": "君药"},
                "香附": {"dose": 6, "unit": "克", "note": "臣药"},
                "川芎": {"dose": 6, "unit": "克", "note": "臣药"},
                "陈皮": {"dose": 6, "unit": "克", "note": "佐药"},
                "枳壳": {"dose": 5, "unit": "克", "note": "佐药"},
                "芍药": {"dose": 5, "unit": "克", "note": "佐药"},
                "炙甘草": {"dose": 3, "unit": "克", "note": "佐使药"},
            },
            "preparation": "水煎服，每日一剂，分两次温服。",
            "indication": "肝气郁滞证。胁肋疼痛，胸闷喜太息，情志抑郁或易怒，或嗳气，脘腹胀满，脉弦。",
            "modifications": [
                "胁痛甚者加郁金、延胡索增强止痛",
                "肝郁化火加栀子、丹皮清肝泻火",
                "兼有血瘀加当归、红花活血祛瘀",
                "胃脘胀痛加厚朴、木香理气和胃",
            ],
        },
        {
            "name": "逍遥散",
            "source": "《太平惠民和剂局方》",
            "category": "疏肝解郁养血健脾",
            "herbs": {
                "柴胡": {"dose": 9, "unit": "克", "note": "君药"},
                "当归": {"dose": 9, "unit": "克", "note": "臣药"},
                "白芍": {"dose": 9, "unit": "克", "note": "臣药"},
                "白术": {"dose": 9, "unit": "克", "note": "佐药"},
                "茯苓": {"dose": 9, "unit": "克", "note": "佐药"},
                "炙甘草": {"dose": 5, "unit": "克", "note": "佐使药"},
                "薄荷": {"dose": 3, "unit": "克", "note": "佐药"},
                "生姜": {"dose": 3, "unit": "克", "note": "佐药"},
            },
            "preparation": "共为粗末，每服6-9克，水煎热服，每日2-3次。或水煎服，每日一剂。",
            "indication": "肝郁血虚脾弱证。两胁作痛，头痛目眩，口燥咽干，神疲食少，或月经不调，乳房胀痛，脉弦而虚者。",
            "modifications": [
                "肝郁化火加牡丹皮、栀子清热凉血（丹栀逍遥散）",
                "血虚甚者加生地黄、熟地黄养血（黑逍遥散）",
                "乳房胀痛加橘叶、香附理气止痛",
                "月经不调加益母草、丹参调经",
            ],
        },
        {
            "name": "越鞠丸",
            "source": "《丹溪心法》",
            "category": "行气解郁",
            "herbs": {
                "香附": {"dose": 10, "unit": "克", "note": "君药（气郁）"},
                "川芎": {"dose": 10, "unit": "克", "note": "血郁"},
                "苍术": {"dose": 10, "unit": "克", "note": "湿郁"},
                "栀子": {"dose": 10, "unit": "克", "note": "火郁"},
                "神曲": {"dose": 10, "unit": "克", "note": "食郁"},
            },
            "preparation": "共为细末，水泛为丸，每服6-9克，每日2次，温水送服。或水煎服。",
            "indication": "六郁证。胸膈痞闷，脘腹胀痛，嗳腐吞酸，恶心呕吐，饮食不消，舌苔腻，脉弦。",
            "modifications": [
                "气郁甚者加木香、枳壳增强行气",
                "湿郁甚者加茯苓、泽泻利湿",
                "血郁甚者加桃仁、红花活血",
                "食郁甚者加麦芽、山楂消食",
            ],
        },
    ],
    "血瘀": [
        {
            "name": "血府逐瘀汤",
            "source": "《医林改错》",
            "category": "活血化瘀行气止痛",
            "herbs": {
                "桃仁": {"dose": 12, "unit": "克", "note": "君药"},
                "红花": {"dose": 9, "unit": "克", "note": "君药"},
                "当归": {"dose": 9, "unit": "克", "note": "臣药"},
                "生地黄": {"dose": 9, "unit": "克", "note": "臣药"},
                "川芎": {"dose": 5, "unit": "克", "note": "佐药"},
                "赤芍": {"dose": 6, "unit": "克", "note": "佐药"},
                "牛膝": {"dose": 9, "unit": "克", "note": "佐药"},
                "桔梗": {"dose": 5, "unit": "克", "note": "佐药"},
                "柴胡": {"dose": 3, "unit": "克", "note": "佐药"},
                "枳壳": {"dose": 6, "unit": "克", "note": "佐药"},
                "甘草": {"dose": 3, "unit": "克", "note": "使药"},
            },
            "preparation": "水煎服，每日一剂，分两次温服。",
            "indication": "胸中血瘀证。胸痛，头痛，日久不愈，痛如针刺而有定处，或呃逆日久不止，或饮水即呛，干呕，或内热瞀闷，或心悸怔忡，失眠多梦，急躁易怒，入暮潮热，唇暗或两目暗黑，舌质暗红，或舌有瘀斑、瘀点，脉涩或弦紧。",
            "modifications": [
                "瘀痛甚者加乳香、没药活血止痛",
                "气滞甚者加香附、青皮理气止痛",
                "寒凝血瘀加桂枝、附子温阳散寒",
                "气虚血瘀加黄芪、党参益气活血",
            ],
        },
        {
            "name": "桃核承气汤",
            "source": "《伤寒论》",
            "category": "逐瘀泻热",
            "herbs": {
                "桃仁": {"dose": 12, "unit": "克", "note": "君药"},
                "大黄": {"dose": 12, "unit": "克", "note": "君药"},
                "桂枝": {"dose": 6, "unit": "克", "note": "臣药"},
                "芒硝": {"dose": 6, "unit": "克", "note": "佐药"},
                "炙甘草": {"dose": 6, "unit": "克", "note": "佐使药"},
            },
            "preparation": "水煎服，每日一剂，分两次饭前服。芒硝冲服。",
            "indication": "下焦蓄血证。少腹急结，小便自利，神志如狂，甚则烦躁谵语，至夜发热；以及血瘀经闭，痛经，脉沉实而涩者。",
            "modifications": [
                "妇人血瘀经闭加当归、红花养血活血",
                "痛经甚者加延胡索、香附理气止痛",
                "跌打损伤瘀痛加当归、川芎、苏木活血消肿",
                "瘀热甚者加赤芍、丹皮清热凉血",
            ],
        },
        {
            "name": "补阳还五汤",
            "source": "《医林改错》",
            "category": "补气活血通络",
            "herbs": {
                "黄芪": {"dose": 120, "unit": "克", "note": "君药"},
                "当归尾": {"dose": 6, "unit": "克", "note": "臣药"},
                "赤芍": {"dose": 5, "unit": "克", "note": "佐药"},
                "地龙": {"dose": 3, "unit": "克", "note": "佐药"},
                "川芎": {"dose": 3, "unit": "克", "note": "佐药"},
                "红花": {"dose": 3, "unit": "克", "note": "佐药"},
                "桃仁": {"dose": 3, "unit": "克", "note": "佐药"},
            },
            "preparation": "水煎服，每日一剂，分两次温服。",
            "indication": "中风之气虚血瘀证。半身不遂，口眼歪斜，语言謇涩，口角流涎，小便频数或遗尿失禁，舌暗淡，苔白，脉缓无力。",
            "modifications": [
                "初得半身不遂加防风祛风散邪",
                "语言不利加石菖蒲、远志开窍化痰",
                "口眼歪斜加白附子、僵蚕祛风通络",
                "偏寒加附子、肉桂温阳散寒",
            ],
        },
    ],
    "痰湿": [
        {
            "name": "二陈汤",
            "source": "《太平惠民和剂局方》",
            "category": "燥湿化痰理气和中",
            "herbs": {
                "半夏": {"dose": 15, "unit": "克", "note": "君药"},
                "橘红": {"dose": 15, "unit": "克", "note": "臣药"},
                "白茯苓": {"dose": 9, "unit": "克", "note": "佐药"},
                "炙甘草": {"dose": 5, "unit": "克", "note": "佐使药"},
            },
            "preparation": "共为粗末，每服12克，加生姜7片、乌梅1个，水煎热服，每日2-3次。",
            "indication": "湿痰证。咳嗽痰多，色白易咯，恶心呕吐，胸膈痞闷，肢体困重，或头眩心悸，舌苔白滑或腻，脉滑。",
            "modifications": [
                "痰湿重者加苍术、厚朴燥湿化痰",
                "咳嗽甚者加杏仁、苏子降气止咳",
                "寒痰加干姜、细辛温肺化饮",
                "脾虚加党参、白术健脾益气",
            ],
        },
        {
            "name": "平胃散",
            "source": "《太平惠民和剂局方》",
            "category": "燥湿运脾行气和胃",
            "herbs": {
                "苍术": {"dose": 12, "unit": "克", "note": "君药"},
                "厚朴": {"dose": 9, "unit": "克", "note": "臣药"},
                "陈皮": {"dose": 9, "unit": "克", "note": "佐药"},
                "炙甘草": {"dose": 4, "unit": "克", "note": "佐使药"},
            },
            "preparation": "共为细末，每服4-6克，姜枣煎汤送下，每日3次；或水煎服，加生姜2片、大枣2枚。",
            "indication": "湿滞脾胃证。脘腹胀满，不思饮食，口淡无味，恶心呕吐，嗳气吞酸，肢体沉重，怠惰嗜卧，常多自利，舌苔白腻而厚，脉缓。",
            "modifications": [
                "湿盛加茯苓、泽泻利水渗湿",
                "兼有食滞加山楂、麦芽消食化滞",
                "寒甚加干姜、肉桂温中散寒",
                "脾虚加党参、白术补脾益气",
            ],
        },
        {
            "name": "参苓白术散",
            "source": "《太平惠民和剂局方》",
            "category": "益气健脾渗湿止泻",
            "herbs": {
                "人参": {"dose": 15, "unit": "克", "note": "君药"},
                "白术": {"dose": 15, "unit": "克", "note": "君药"},
                "茯苓": {"dose": 15, "unit": "克", "note": "君药"},
                "山药": {"dose": 15, "unit": "克", "note": "臣药"},
                "莲子肉": {"dose": 9, "unit": "克", "note": "臣药"},
                "白扁豆": {"dose": 12, "unit": "克", "note": "臣药"},
                "薏苡仁": {"dose": 9, "unit": "克", "note": "佐药"},
                "缩砂仁": {"dose": 6, "unit": "克", "note": "佐药"},
                "桔梗": {"dose": 6, "unit": "克", "note": "佐药"},
                "炙甘草": {"dose": 9, "unit": "克", "note": "佐使药"},
            },
            "preparation": "共为细末，每服6克，枣汤调下，每日2-3次。或水煎服。",
            "indication": "脾虚湿盛证。饮食不化，胸脘痞闷，肠鸣泄泻，四肢乏力，形体消瘦，面色萎黄，舌淡苔白腻，脉虚缓。",
            "modifications": [
                "泄泻甚者加肉豆蔻、诃子涩肠止泻",
                "兼有寒象加干姜、附子温中散寒",
                "食欲不振加焦三仙开胃消食",
                "湿重加苍术、厚朴燥湿健脾",
            ],
        },
    ],
    "湿热": [
        {
            "name": "龙胆泻肝汤",
            "source": "《医方集解》",
            "category": "清泻肝胆实火清利肝经湿热",
            "herbs": {
                "龙胆草": {"dose": 6, "unit": "克", "note": "君药"},
                "黄芩": {"dose": 9, "unit": "克", "note": "臣药"},
                "栀子": {"dose": 9, "unit": "克", "note": "臣药"},
                "泽泻": {"dose": 12, "unit": "克", "note": "佐药"},
                "木通": {"dose": 6, "unit": "克", "note": "佐药"},
                "车前子": {"dose": 9, "unit": "克", "note": "佐药"},
                "当归": {"dose": 3, "unit": "克", "note": "佐药"},
                "生地黄": {"dose": 9, "unit": "克", "note": "佐药"},
                "柴胡": {"dose": 6, "unit": "克", "note": "佐药"},
                "生甘草": {"dose": 6, "unit": "克", "note": "佐使药"},
            },
            "preparation": "水煎服，每日一剂，分两次温服。",
            "indication": "肝胆实火上炎证。头痛目赤，胁痛，口苦，耳聋、耳肿，舌红苔黄，脉弦数有力。肝经湿热下注证。阴肿，阴痒，筋痿，阴汗，小便淋浊，或妇女带下黄臭等，舌红苔黄腻，脉弦数有力。",
            "modifications": [
                "肝火上炎重者加夏枯草、菊花清肝泻火",
                "湿盛加薏苡仁、滑石利湿泄浊",
                "黄疸加茵陈、大黄利湿退黄",
                "小便淋涩痛甚加石韦、瞿麦利尿通淋",
            ],
        },
        {
            "name": "茵陈蒿汤",
            "source": "《伤寒论》",
            "category": "清热利湿退黄",
            "herbs": {
                "茵陈": {"dose": 18, "unit": "克", "note": "君药"},
                "栀子": {"dose": 12, "unit": "克", "note": "臣药"},
                "大黄": {"dose": 6, "unit": "克", "note": "佐药"},
            },
            "preparation": "水煎服，每日一剂，分三次服。",
            "indication": "湿热黄疸证。一身面目俱黄，黄色鲜明，发热，无汗或但头汗出，口渴欲饮，恶心呕吐，腹微满，小便短赤，大便不爽或秘结，舌红苔黄腻，脉沉数或滑数有力。",
            "modifications": [
                "湿重于热加茯苓、猪苓、泽泻利水渗湿",
                "热重于湿加黄柏、龙胆草清热燥湿",
                "胁痛加柴胡、川楝子疏肝止痛",
                "呕吐加半夏、竹茹降逆止呕",
            ],
        },
        {
            "name": "八正散",
            "source": "《太平惠民和剂局方》",
            "category": "清热泻火利水通淋",
            "herbs": {
                "车前子": {"dose": 9, "unit": "克", "note": ""},
                "瞿麦": {"dose": 9, "unit": "克", "note": ""},
                "萹蓄": {"dose": 9, "unit": "克", "note": ""},
                "滑石": {"dose": 9, "unit": "克", "note": ""},
                "山栀子仁": {"dose": 9, "unit": "克", "note": ""},
                "炙甘草": {"dose": 9, "unit": "克", "note": ""},
                "木通": {"dose": 9, "unit": "克", "note": ""},
                "大黄": {"dose": 9, "unit": "克", "note": ""},
            },
            "preparation": "共为散，每服6-10克，灯心煎汤送服，每日2-3次；或水煎服，加灯心草。",
            "indication": "湿热淋证。尿频尿急，溺时涩痛，淋沥不畅，尿色浑赤，甚则癃闭不通，小腹急满，口燥咽干，舌苔黄腻，脉滑数。",
            "modifications": [
                "血淋加小蓟、白茅根凉血止血",
                "石淋加金钱草、海金沙、鸡内金排石通淋",
                "膏淋加萆薢、菖蒲分清化浊",
                "热毒甚加金银花、蒲公英清热解毒",
            ],
        },
    ],
}


def get_formulas_by_pattern(pattern_name: str) -> List[Dict]:
    return FORMULARY.get(pattern_name, [])


def get_formula_detail(pattern_name: str, formula_name: str) -> Optional[Dict]:
    formulas = FORMULARY.get(pattern_name, [])
    for f in formulas:
        if f["name"] == formula_name:
            return f
    return None


def get_all_formulas() -> List[Dict]:
    result = []
    for pattern_name, formulas in FORMULARY.items():
        for f in formulas:
            result.append({
                "pattern": pattern_name,
                "name": f["name"],
                "source": f["source"],
                "category": f.get("category", ""),
            })
    return result


def adjust_formula_dose(
    formula: Dict,
    dose_factor: float,
    target_unit: str = "克",
) -> Dict:
    adjusted_herbs = adjust_herb_doses(formula["herbs"], dose_factor, target_unit)
    return {
        **formula,
        "herbs": adjusted_herbs,
        "dose_factor": dose_factor,
        "target_unit": target_unit,
    }


def convert_formula_unit(formula: Dict, target_unit: str = "克") -> Dict:
    converted_herbs = {}
    for herb_name, herb_info in formula["herbs"].items():
        original_dose = herb_info.get("dose", 0)
        original_unit = herb_info.get("unit", "克")
        converted = convert_dose(original_dose, original_unit, target_unit)
        converted_herbs[herb_name] = {
            **herb_info,
            "dose": converted,
            "unit": target_unit,
        }
    return {
        **formula,
        "herbs": converted_herbs,
    }
