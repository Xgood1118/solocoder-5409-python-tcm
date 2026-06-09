from typing import Dict, List, Set, Tuple


EIGHTEEN_INCOMPATIBILITIES: List[Dict] = [
    {
        "rule": "本草明言十八反，半蒌贝蔹及攻乌",
        "herb_group_a": ["半夏", "瓜蒌", "瓜蒌皮", "瓜蒌仁", "天花粉", "川贝母", "浙贝母", "伊贝母", "平贝母", "白蔹", "白及"],
        "herb_group_b": ["川乌", "制川乌", "草乌", "制草乌", "附子"],
        "description": "乌头反半夏、瓜蒌、贝母、白蔹、白及",
        "severity": "high",
    },
    {
        "rule": "藻戟遂芫俱战草",
        "herb_group_a": ["海藻", "京大戟", "红大戟", "甘遂", "芫花"],
        "herb_group_b": ["甘草", "炙甘草"],
        "description": "甘草反海藻、大戟、甘遂、芫花",
        "severity": "high",
    },
    {
        "rule": "诸参辛芍叛藜芦",
        "herb_group_a": ["人参", "西洋参", "党参", "太子参", "玄参", "丹参", "苦参", "沙参", "南沙参", "北沙参", "细辛", "赤芍", "白芍"],
        "herb_group_b": ["藜芦"],
        "description": "藜芦反人参、丹参、玄参、沙参、苦参、细辛、芍药",
        "severity": "high",
    },
]


NINETEEN_INCOMPATIBILITIES: List[Dict] = [
    {
        "rule": "硫黄原是火中精，朴硝一见便相争",
        "herb_a": "硫黄",
        "herb_b": "朴硝",
        "description": "硫黄畏朴硝",
        "severity": "medium",
    },
    {
        "rule": "水银莫与砒霜见",
        "herb_a": "水银",
        "herb_b": "砒霜",
        "description": "水银畏砒霜",
        "severity": "high",
    },
    {
        "rule": "狼毒最怕密陀僧",
        "herb_a": "狼毒",
        "herb_b": "密陀僧",
        "description": "狼毒畏密陀僧",
        "severity": "medium",
    },
    {
        "rule": "巴豆性烈最为上，偏与牵牛不顺情",
        "herb_a": "巴豆",
        "herb_b": "牵牛子",
        "description": "巴豆畏牵牛子",
        "severity": "high",
    },
    {
        "rule": "丁香莫与郁金见",
        "herb_a": "丁香",
        "herb_b": "郁金",
        "description": "丁香畏郁金",
        "severity": "medium",
    },
    {
        "rule": "牙硝难合京三棱",
        "herb_a": "牙硝",
        "herb_b": "京三棱",
        "description": "牙硝畏三棱",
        "severity": "medium",
    },
    {
        "rule": "川乌草乌不顺犀",
        "herb_a": "川乌",
        "herb_b": "犀角",
        "description": "川乌、草乌畏犀角",
        "severity": "medium",
    },
    {
        "rule": "人参最怕五灵脂",
        "herb_a": "人参",
        "herb_b": "五灵脂",
        "description": "人参畏五灵脂",
        "severity": "medium",
    },
    {
        "rule": "官桂善能调冷气，若逢石脂便相欺",
        "herb_a": "肉桂",
        "herb_b": "赤石脂",
        "description": "肉桂畏赤石脂",
        "severity": "medium",
    },
]


PREGNANCY_FORBIDDEN: List[Dict] = [
    {"herb": "麝香", "category": "峻烈剧毒", "reason": "开窍醒神，活血通经，催产，孕妇用之易致堕胎"},
    {"herb": "牛黄", "category": "峻烈剧毒", "reason": "开窍豁痰，熄风定惊，性凉，孕妇慎用"},
    {"herb": "雄黄", "category": "峻烈剧毒", "reason": "解毒杀虫，燥湿祛痰，有毒，孕妇禁用"},
    {"herb": "砒石", "category": "峻烈剧毒", "reason": "外用蚀疮去腐，内服劫痰平喘，有剧毒，孕妇禁用"},
    {"herb": "水银", "category": "峻烈剧毒", "reason": "攻毒杀虫，有剧毒，孕妇禁用"},
    {"herb": "轻粉", "category": "峻烈剧毒", "reason": "外用攻毒杀虫，内服逐水通便，有毒，孕妇禁用"},
    {"herb": "斑蝥", "category": "峻烈剧毒", "reason": "攻毒逐瘀，散结消癥，有大毒，孕妇禁用"},
    {"herb": "马钱子", "category": "峻烈剧毒", "reason": "通络止痛，散结消肿，有大毒，孕妇禁用"},
    {"herb": "蟾酥", "category": "峻烈剧毒", "reason": "解毒止痛，开窍醒神，有毒，孕妇慎用"},
    {"herb": "川乌", "category": "峻烈剧毒", "reason": "祛风除湿，温经止痛，有大毒，孕妇禁用"},
    {"herb": "草乌", "category": "峻烈剧毒", "reason": "祛风除湿，温经止痛，有大毒，孕妇禁用"},
    {"herb": "附子", "category": "温里药", "reason": "回阳救逆，补火助阳，有毒，孕妇慎用"},
    {"herb": "肉桂", "category": "温里药", "reason": "补火助阳，引火归元，活血通经，孕妇慎用"},
    {"herb": "干姜", "category": "温里药", "reason": "温中散寒，回阳通脉，孕妇慎用"},
    {"herb": "桃仁", "category": "活血破瘀", "reason": "活血祛瘀，润肠通便，孕妇禁用"},
    {"herb": "红花", "category": "活血破瘀", "reason": "活血通经，散瘀止痛，孕妇禁用"},
    {"herb": "藏红花", "category": "活血破瘀", "reason": "活血化瘀，凉血解毒，孕妇禁用"},
    {"herb": "三棱", "category": "活血破瘀", "reason": "破血行气，消积止痛，孕妇禁用"},
    {"herb": "莪术", "category": "活血破瘀", "reason": "破血行气，消积止痛，孕妇禁用"},
    {"herb": "益母草", "category": "活血破瘀", "reason": "活血调经，利尿消肿，孕妇禁用"},
    {"herb": "牛膝", "category": "活血破瘀", "reason": "逐瘀通经，补肝肾，强筋骨，孕妇禁用"},
    {"herb": "川牛膝", "category": "活血破瘀", "reason": "逐瘀通经，通利关节，孕妇禁用"},
    {"herb": "土鳖虫", "category": "活血破瘀", "reason": "破血逐瘀，续筋接骨，孕妇禁用"},
    {"herb": "水蛭", "category": "活血破瘀", "reason": "破血通经，逐瘀消癥，孕妇禁用"},
    {"herb": "虻虫", "category": "活血破瘀", "reason": "破血逐瘀，消癥散积，孕妇禁用"},
    {"herb": "穿山甲", "category": "活血破瘀", "reason": "活血消癥，通经下乳，孕妇禁用"},
    {"herb": "王不留行", "category": "活血破瘀", "reason": "活血通经，下乳消肿，孕妇慎用"},
    {"herb": "丹参", "category": "活血调经", "reason": "活血祛瘀，通经止痛，孕妇慎用"},
    {"herb": "赤芍", "category": "活血调经", "reason": "清热凉血，散瘀止痛，孕妇慎用"},
    {"herb": "丹皮", "category": "清热凉血", "reason": "清热凉血，活血化瘀，孕妇慎用"},
    {"herb": "牡丹皮", "category": "清热凉血", "reason": "清热凉血，活血化瘀，孕妇慎用"},
    {"herb": "大黄", "category": "泻下药", "reason": "泻下攻积，清热泻火，活血祛瘀，孕妇禁用"},
    {"herb": "芒硝", "category": "泻下药", "reason": "泻下通便，润燥软坚，孕妇慎用"},
    {"herb": "番泻叶", "category": "泻下药", "reason": "泻热行滞，通便，孕妇慎用"},
    {"herb": "甘遂", "category": "峻下逐水", "reason": "泻水逐饮，消肿散结，有毒，孕妇禁用"},
    {"herb": "大戟", "category": "峻下逐水", "reason": "泻水逐饮，消肿散结，有毒，孕妇禁用"},
    {"herb": "芫花", "category": "峻下逐水", "reason": "泻水逐饮，祛痰止咳，有毒，孕妇禁用"},
    {"herb": "牵牛子", "category": "峻下逐水", "reason": "泻水通便，消痰涤饮，有毒，孕妇禁用"},
    {"herb": "巴豆", "category": "峻下逐水", "reason": "峻下冷积，逐水退肿，有大毒，孕妇禁用"},
    {"herb": "麝香", "category": "开窍药", "reason": "开窍醒神，活血通经，催产，孕妇禁用"},
    {"herb": "冰片", "category": "开窍药", "reason": "开窍醒神，清热止痛，孕妇慎用"},
    {"herb": "苏合香", "category": "开窍药", "reason": "开窍醒神，辟秽止痛，孕妇慎用"},
    {"herb": "天南星", "category": "化痰药", "reason": "燥湿化痰，祛风解痉，有毒，孕妇慎用"},
    {"herb": "半夏", "category": "化痰药", "reason": "燥湿化痰，降逆止呕，有毒，孕妇慎用"},
    {"herb": "白附子", "category": "化痰药", "reason": "燥湿化痰，祛风止痉，有毒，孕妇慎用"},
    {"herb": "皂角", "category": "化痰药", "reason": "祛顽痰，通窍开闭，孕妇慎用"},
    {"herb": "常山", "category": "涌吐药", "reason": "涌吐痰涎，截疟，孕妇禁用"},
    {"herb": "藜芦", "category": "涌吐药", "reason": "涌吐风痰，杀虫疗癣，有毒，孕妇禁用"},
    {"herb": "瓜蒂", "category": "涌吐药", "reason": "涌吐痰食，祛湿退黄，孕妇慎用"},
    {"herb": "代赭石", "category": "平肝熄风", "reason": "平肝潜阳，重镇降逆，孕妇慎用"},
    {"herb": "全蝎", "category": "平肝熄风", "reason": "息风镇痉，攻毒散结，有毒，孕妇禁用"},
    {"herb": "蜈蚣", "category": "平肝熄风", "reason": "息风镇痉，攻毒散结，有毒，孕妇禁用"},
    {"herb": "地龙", "category": "平肝熄风", "reason": "清热定惊，通络平喘，孕妇慎用"},
    {"herb": "僵蚕", "category": "平肝熄风", "reason": "息风止痉，祛风止痛，孕妇慎用"},
    {"herb": "藿香", "category": "芳香化湿", "reason": "化湿止呕，发表解暑，孕妇慎用"},
    {"herb": "佩兰", "category": "芳香化湿", "reason": "化湿解暑，孕妇慎用"},
    {"herb": "砂仁", "category": "芳香化湿", "reason": "化湿开胃，温脾止泻，理气安胎，孕妇可用"},
    {"herb": "白豆蔻", "category": "芳香化湿", "reason": "化湿行气，温中止呕，孕妇慎用"},
    {"herb": "苍术", "category": "芳香化湿", "reason": "燥湿健脾，祛风散寒，孕妇慎用"},
    {"herb": "厚朴", "category": "芳香化湿", "reason": "燥湿消痰，下气除满，孕妇慎用"},
    {"herb": "滑石", "category": "利水渗湿", "reason": "利尿通淋，清热解暑，孕妇慎用"},
    {"herb": "木通", "category": "利水渗湿", "reason": "利尿通淋，清心火，通经下乳，孕妇慎用"},
    {"herb": "通草", "category": "利水渗湿", "reason": "清热利尿，通气下乳，孕妇慎用"},
    {"herb": "瞿麦", "category": "利水渗湿", "reason": "利尿通淋，破血通经，孕妇禁用"},
    {"herb": "萹蓄", "category": "利水渗湿", "reason": "利尿通淋，杀虫止痒，孕妇慎用"},
    {"herb": "海金沙", "category": "利水渗湿", "reason": "清利湿热，通淋止痛，孕妇慎用"},
    {"herb": "石韦", "category": "利水渗湿", "reason": "利尿通淋，清肺止咳，孕妇慎用"},
    {"herb": "冬葵子", "category": "利水渗湿", "reason": "利水通淋，下乳润肠，孕妇慎用"},
    {"herb": "车前子", "category": "利水渗湿", "reason": "清热利尿，渗湿通淋，孕妇慎用"},
    {"herb": "薏苡仁", "category": "利水渗湿", "reason": "利水渗湿，健脾止泻，清热排脓，孕妇慎用"},
    {"herb": "泽泻", "category": "利水渗湿", "reason": "利小便，清湿热，孕妇慎用"},
    {"herb": "猪苓", "category": "利水渗湿", "reason": "利水渗湿，孕妇慎用"},
    {"herb": "茯苓", "category": "利水渗湿", "reason": "利水渗湿，健脾宁心，孕妇可用"},
    {"herb": "枳实", "category": "理气药", "reason": "破气消积，化痰散痞，孕妇慎用"},
    {"herb": "枳壳", "category": "理气药", "reason": "理气宽中，行滞消胀，孕妇慎用"},
    {"herb": "青皮", "category": "理气药", "reason": "疏肝破气，消积化滞，孕妇慎用"},
    {"herb": "香附", "category": "理气药", "reason": "疏肝解郁，理气宽中，调经止痛，孕妇慎用"},
    {"herb": "乌药", "category": "理气药", "reason": "行气止痛，温肾散寒，孕妇慎用"},
    {"herb": "佛手", "category": "理气药", "reason": "疏肝理气，和胃止痛，孕妇慎用"},
    {"herb": "薤白", "category": "理气药", "reason": "通阳散结，行气导滞，孕妇慎用"},
    {"herb": "柿蒂", "category": "理气药", "reason": "降逆止呃，孕妇可用"},
    {"herb": "川楝子", "category": "理气药", "reason": "疏肝泄热，行气止痛，有小毒，孕妇慎用"},
    {"herb": "花椒", "category": "温里药", "reason": "温中止痛，杀虫止痒，有小毒，孕妇慎用"},
    {"herb": "胡椒", "category": "温里药", "reason": "温中散寒，下气消痰，孕妇慎用"},
    {"herb": "吴茱萸", "category": "温里药", "reason": "散寒止痛，降逆止呕，助阳止泻，有小毒，孕妇慎用"},
    {"herb": "小茴香", "category": "温里药", "reason": "散寒止痛，理气和胃，孕妇慎用"},
    {"herb": "高良姜", "category": "温里药", "reason": "温胃散寒，消食止痛，孕妇慎用"},
    {"herb": "丁香", "category": "温里药", "reason": "温中降逆，补肾助阳，孕妇慎用"},
    {"herb": "山豆根", "category": "清热药", "reason": "清热解毒，消肿利咽，有毒，孕妇慎用"},
    {"herb": "射干", "category": "清热药", "reason": "清热解毒，消痰利咽，孕妇慎用"},
    {"herb": "鸦胆子", "category": "清热药", "reason": "清热解毒，截疟止痢，有毒，孕妇禁用"},
    {"herb": "红藤", "category": "清热药", "reason": "清热解毒，活血祛风，孕妇慎用"},
    {"herb": "败酱草", "category": "清热药", "reason": "清热解毒，消痈排脓，祛瘀止痛，孕妇慎用"},
    {"herb": "鱼腥草", "category": "清热药", "reason": "清热解毒，消痈排脓，利尿通淋，孕妇慎用"},
    {"herb": "金荞麦", "category": "清热药", "reason": "清热解毒，排脓祛瘀，孕妇慎用"},
    {"herb": "土茯苓", "category": "清热药", "reason": "解毒除湿，通利关节，孕妇慎用"},
    {"herb": "山慈菇", "category": "清热药", "reason": "清热解毒，化痰散结，有小毒，孕妇慎用"},
    {"herb": "熊胆", "category": "清热药", "reason": "清热解毒，息风止痉，清肝明目，孕妇慎用"},
    {"herb": "白鲜皮", "category": "清热药", "reason": "清热燥湿，祛风解毒，孕妇慎用"},
    {"herb": "苦参", "category": "清热药", "reason": "清热燥湿，杀虫利尿，孕妇慎用"},
    {"herb": "紫草", "category": "清热药", "reason": "凉血活血，解毒透疹，孕妇禁用"},
    {"herb": "金银花", "category": "清热药", "reason": "清热解毒，疏散风热，孕妇慎用"},
    {"herb": "连翘", "category": "清热药", "reason": "清热解毒，消肿散结，孕妇慎用"},
    {"herb": "蒲公英", "category": "清热药", "reason": "清热解毒，消肿散结，利尿通淋，孕妇慎用"},
    {"herb": "紫花地丁", "category": "清热药", "reason": "清热解毒，凉血消肿，孕妇慎用"},
    {"herb": "板蓝根", "category": "清热药", "reason": "清热解毒，凉血利咽，孕妇慎用"},
    {"herb": "大青叶", "category": "清热药", "reason": "清热解毒，凉血消斑，孕妇慎用"},
    {"herb": "青黛", "category": "清热药", "reason": "清热解毒，凉血消斑，清肝泻火，孕妇慎用"},
    {"herb": "贯众", "category": "清热药", "reason": "清热解毒，凉血止血，杀虫，有小毒，孕妇禁用"},
    {"herb": "三棵针", "category": "清热药", "reason": "清热燥湿，泻火解毒，孕妇慎用"},
    {"herb": "马尾连", "category": "清热药", "reason": "清热燥湿，泻火解毒，孕妇慎用"},
]


LACTATION_CAUTION: List[Dict] = [
    {"herb": "麦芽", "category": "消食药", "reason": "行气消食，健脾开胃，回乳消胀，哺乳期妇女禁用（有回乳作用）"},
    {"herb": "炒麦芽", "category": "消食药", "reason": "回乳消胀，哺乳期妇女禁用"},
    {"herb": "芒硝", "category": "泻下药", "reason": "泻下通便，润燥软坚，哺乳期慎用"},
    {"herb": "大黄", "category": "泻下药", "reason": "泻下攻积，清热泻火，哺乳期慎用"},
    {"herb": "番泻叶", "category": "泻下药", "reason": "泻热行滞，通便，哺乳期慎用"},
    {"herb": "冰片", "category": "开窍药", "reason": "开窍醒神，清热止痛，哺乳期慎用"},
    {"herb": "麝香", "category": "开窍药", "reason": "开窍醒神，活血通经，哺乳期禁用"},
    {"herb": "雄黄", "category": "峻烈剧毒", "reason": "解毒杀虫，燥湿祛痰，有毒，哺乳期禁用"},
    {"herb": "砒石", "category": "峻烈剧毒", "reason": "外用蚀疮去腐，内服劫痰平喘，有剧毒，哺乳期禁用"},
    {"herb": "水银", "category": "峻烈剧毒", "reason": "攻毒杀虫，有剧毒，哺乳期禁用"},
    {"herb": "轻粉", "category": "峻烈剧毒", "reason": "外用攻毒杀虫，内服逐水通便，有毒，哺乳期禁用"},
    {"herb": "斑蝥", "category": "峻烈剧毒", "reason": "攻毒逐瘀，散结消癥，有大毒，哺乳期禁用"},
    {"herb": "马钱子", "category": "峻烈剧毒", "reason": "通络止痛，散结消肿，有大毒，哺乳期禁用"},
    {"herb": "川乌", "category": "峻烈剧毒", "reason": "祛风除湿，温经止痛，有大毒，哺乳期禁用"},
    {"herb": "草乌", "category": "峻烈剧毒", "reason": "祛风除湿，温经止痛，有大毒，哺乳期禁用"},
    {"herb": "附子", "category": "温里药", "reason": "回阳救逆，补火助阳，有毒，哺乳期慎用"},
    {"herb": "桃仁", "category": "活血破瘀", "reason": "活血祛瘀，润肠通便，哺乳期慎用"},
    {"herb": "红花", "category": "活血破瘀", "reason": "活血通经，散瘀止痛，哺乳期慎用"},
    {"herb": "三棱", "category": "活血破瘀", "reason": "破血行气，消积止痛，哺乳期禁用"},
    {"herb": "莪术", "category": "活血破瘀", "reason": "破血行气，消积止痛，哺乳期禁用"},
    {"herb": "水蛭", "category": "活血破瘀", "reason": "破血通经，逐瘀消癥，哺乳期禁用"},
    {"herb": "虻虫", "category": "活血破瘀", "reason": "破血逐瘀，消癥散积，哺乳期禁用"},
    {"herb": "土鳖虫", "category": "活血破瘀", "reason": "破血逐瘀，续筋接骨，哺乳期禁用"},
    {"herb": "穿山甲", "category": "活血破瘀", "reason": "活血消癥，通经下乳，哺乳期可用（有通乳作用）"},
    {"herb": "王不留行", "category": "活血破瘀", "reason": "活血通经，下乳消肿，哺乳期可用（有通乳作用）"},
    {"herb": "甘遂", "category": "峻下逐水", "reason": "泻水逐饮，消肿散结，有毒，哺乳期禁用"},
    {"herb": "大戟", "category": "峻下逐水", "reason": "泻水逐饮，消肿散结，有毒，哺乳期禁用"},
    {"herb": "芫花", "category": "峻下逐水", "reason": "泻水逐饮，祛痰止咳，有毒，哺乳期禁用"},
    {"herb": "牵牛子", "category": "峻下逐水", "reason": "泻水通便，消痰涤饮，有毒，哺乳期禁用"},
    {"herb": "巴豆", "category": "峻下逐水", "reason": "峻下冷积，逐水退肿，有大毒，哺乳期禁用"},
    {"herb": "藜芦", "category": "涌吐药", "reason": "涌吐风痰，杀虫疗癣，有毒，哺乳期禁用"},
    {"herb": "常山", "category": "涌吐药", "reason": "涌吐痰涎，截疟，哺乳期禁用"},
    {"herb": "全蝎", "category": "平肝熄风", "reason": "息风镇痉，攻毒散结，有毒，哺乳期禁用"},
    {"herb": "蜈蚣", "category": "平肝熄风", "reason": "息风镇痉，攻毒散结，有毒，哺乳期禁用"},
    {"herb": "半夏", "category": "化痰药", "reason": "燥湿化痰，降逆止呕，有毒，哺乳期慎用"},
    {"herb": "天南星", "category": "化痰药", "reason": "燥湿化痰，祛风解痉，有毒，哺乳期慎用"},
    {"herb": "白附子", "category": "化痰药", "reason": "燥湿化痰，祛风止痉，有毒，哺乳期慎用"},
]


def check_eighteen_incompatibilities(herb_list: List[str]) -> List[Dict]:
    conflicts = []
    herb_set = set(herb_list)

    for rule in EIGHTEEN_INCOMPATIBILITIES:
        set_a = set(rule["herb_group_a"])
        set_b = set(rule["herb_group_b"])
        found_a = herb_set & set_a
        found_b = herb_set & set_b

        if found_a and found_b:
            conflicts.append({
                "type": "十八反",
                "rule": rule["rule"],
                "description": rule["description"],
                "herbs_group_a": list(found_a),
                "herbs_group_b": list(found_b),
                "severity": rule["severity"],
            })

    return conflicts


def check_nineteen_incompatibilities(herb_list: List[str]) -> List[Dict]:
    conflicts = []
    herb_set = set(herb_list)

    for rule in NINETEEN_INCOMPATIBILITIES:
        if rule["herb_a"] in herb_set and rule["herb_b"] in herb_set:
            conflicts.append({
                "type": "十九畏",
                "rule": rule["rule"],
                "description": rule["description"],
                "herb_a": rule["herb_a"],
                "herb_b": rule["herb_b"],
                "severity": rule["severity"],
            })

    return conflicts


def check_pregnancy_safety(herb_list: List[str]) -> List[Dict]:
    warnings = []
    herb_set = set(herb_list)

    for item in PREGNANCY_FORBIDDEN:
        if item["herb"] in herb_set:
            status = "禁用" if "禁用" in item["reason"] or "大毒" in item["reason"] or "剧毒" in item["reason"] else "慎用"
            warnings.append({
                "type": "妊娠禁忌",
                "herb": item["herb"],
                "category": item["category"],
                "reason": item["reason"],
                "status": status,
            })

    return warnings


def check_lactation_safety(herb_list: List[str]) -> List[Dict]:
    warnings = []
    herb_set = set(herb_list)

    for item in LACTATION_CAUTION:
        if item["herb"] in herb_set:
            status = "禁用" if "禁用" in item["reason"] or "大毒" in item["reason"] or "剧毒" in item["reason"] else "慎用"
            if "可用" in item["reason"]:
                status = "可用"
            warnings.append({
                "type": "哺乳注意",
                "herb": item["herb"],
                "category": item["category"],
                "reason": item["reason"],
                "status": status,
            })

    return warnings


def check_all_safety(
    herb_list: List[str],
    is_pregnant: bool = False,
    is_lactating: bool = False,
) -> Dict:
    result = {
        "has_conflict": False,
        "conflicts": [],
        "warnings": [],
    }

    eighteen_conflicts = check_eighteen_incompatibilities(herb_list)
    nineteen_conflicts = check_nineteen_incompatibilities(herb_list)

    all_conflicts = eighteen_conflicts + nineteen_conflicts
    if all_conflicts:
        result["has_conflict"] = True
        result["conflicts"] = all_conflicts

    if is_pregnant:
        preg_warnings = check_pregnancy_safety(herb_list)
        if preg_warnings:
            result["warnings"].extend(preg_warnings)

    if is_lactating:
        lact_warnings = check_lactation_safety(herb_list)
        if lact_warnings:
            result["warnings"].extend(lact_warnings)

    return result


def get_pregnancy_forbidden_list() -> List[Dict]:
    return PREGNANCY_FORBIDDEN


def get_lactation_caution_list() -> List[Dict]:
    return LACTATION_CAUTION


def get_eighteen_incompatibilities() -> List[Dict]:
    return EIGHTEEN_INCOMPATIBILITIES


def get_nineteen_incompatibilities() -> List[Dict]:
    return NINETEEN_INCOMPATIBILITIES
