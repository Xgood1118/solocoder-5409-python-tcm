import sys
sys.path.insert(0, '.')

from app.symptom import normalize_symptoms, get_tongue_presets, get_pulse_presets
from app.pattern import get_top_patterns, get_all_patterns
from app.formula import get_formulas_by_pattern
from app.safety import check_all_safety, check_eighteen_incompatibilities, check_nineteen_incompatibilities, check_pregnancy_safety
from app.modifier import compare_formulas, get_modification_suggestions
from app.utils import calculate_dose_factor, convert_dose

def test_symptom():
    print("=" * 50)
    print("测试 1: 症状同义词归一化")
    symptoms = ["没劲儿", "睡不着", "头疼", "乏力"]
    normalized = normalize_symptoms(symptoms)
    print(f"  输入: {symptoms}")
    print(f"  归一化: {normalized}")
    assert "乏力" in normalized and "失眠" in normalized and "头痛" in normalized
    print("  ✓ 通过")

def test_tongue_pulse_presets():
    print("\n" + "=" * 50)
    print("测试 2: 舌象脉象预设")
    tongues = get_tongue_presets()
    pulses = get_pulse_presets()
    print(f"  舌象预设数量: {len(tongues)}")
    print(f"  脉象预设数量: {len(pulses)}")
    assert len(tongues) > 0
    assert len(pulses) > 0
    print("  ✓ 通过")

def test_pattern():
    print("\n" + "=" * 50)
    print("测试 3: 证型判定（加权评分）")
    symptoms = ["乏力", "自汗", "气短", "食欲不振"]
    tongue = "舌淡"
    pulse = "脉弱"
    results = get_top_patterns(symptoms, tongue, pulse, top_n=3)
    print(f"  症状: {symptoms}")
    print(f"  舌象: {tongue}, 脉象: {pulse}")
    print(f"  Top 3 证型:")
    for r in results:
        print(f"    - {r['pattern']}: {r['total_score']} 分 (阈值: {r['threshold']}) {'✓' if r['matched'] else ''}")
        if r.get('boost'):
            print(f"      舌脉组合加分: +{r['boost']['boost']}")
    assert len(results) == 3
    assert results[0]['pattern'] == '气虚'
    assert results[0]['matched'] == True
    print("  ✓ 通过")

def test_formula():
    print("\n" + "=" * 50)
    print("测试 4: 方剂推荐")
    formulas = get_formulas_by_pattern("气虚")
    print(f"  气虚证方剂数量: {len(formulas)}")
    for f in formulas:
        print(f"    - {f['name']} ({f['source']})")
        print(f"      组成: {', '.join(f['herbs'].keys())}")
    assert len(formulas) >= 3
    print("  ✓ 通过")

def test_safety():
    print("\n" + "=" * 50)
    print("测试 5: 禁忌检查")

    herbs1 = ["人参", "藜芦"]
    conflicts1 = check_eighteen_incompatibilities(herbs1)
    print(f"  十八反测试 (人参+藜芦): {len(conflicts1)} 个冲突")
    assert len(conflicts1) > 0

    herbs2 = ["丁香", "郁金"]
    conflicts2 = check_nineteen_incompatibilities(herbs2)
    print(f"  十九畏测试 (丁香+郁金): {len(conflicts2)} 个冲突")
    assert len(conflicts2) > 0

    herbs3 = ["桃仁", "红花", "麝香"]
    preg = check_pregnancy_safety(herbs3)
    print(f"  妊娠禁忌测试 (桃仁+红花+麝香): {len(preg)} 个警告")
    assert len(preg) > 0

    herbs4 = ["人参", "白术", "茯苓"]
    all_safe = check_all_safety(herbs4, is_pregnant=True)
    print(f"  安全组合 (人参+白术+茯苓): 冲突 {len(all_safe['conflicts'])} 个, 警告 {len(all_safe['warnings'])} 个")
    assert len(all_safe['conflicts']) == 0

    print("  ✓ 通过")

def test_dose():
    print("\n" + "=" * 50)
    print("测试 6: 剂量换算")

    gram = convert_dose(3, "钱", "克")
    qian = convert_dose(9.375, "克", "钱")
    print(f"  3钱 = {gram} 克")
    print(f"  9.375克 = {qian} 钱")
    assert abs(gram - 9.375) < 0.01

    factor_child = calculate_dose_factor(age=5)
    factor_adult = calculate_dose_factor(age=30)
    factor_elderly = calculate_dose_factor(age=70)
    print(f"  5岁儿童剂量系数: {factor_child}")
    print(f"  30岁成人剂量系数: {factor_adult}")
    print(f"  70岁老人剂量系数: {factor_elderly}")
    assert factor_child < 1
    assert factor_adult == 1.0
    assert factor_elderly < 1

    print("  ✓ 通过")

def test_modifier():
    print("\n" + "=" * 50)
    print("测试 7: 加减建议与差异对比")

    suggestions = get_modification_suggestions("气虚")
    print(f"  气虚证加减建议数量: {len(suggestions)}")
    for s in suggestions[:3]:
        print(f"    - {s['condition']}: +{s['add']}")
    assert len(suggestions) > 0

    original = {
        "人参": {"dose": 9, "unit": "克"},
        "白术": {"dose": 9, "unit": "克"},
        "茯苓": {"dose": 9, "unit": "克"},
        "炙甘草": {"dose": 6, "unit": "克"},
    }
    modified = {
        "人参": {"dose": 12, "unit": "克"},
        "白术": {"dose": 9, "unit": "克"},
        "黄芪": {"dose": 15, "unit": "克"},
        "炙甘草": {"dose": 6, "unit": "克"},
    }
    diff = compare_formulas(original, modified)
    print(f"\n  方剂差异对比:")
    print(f"    新增药材: {[h['herb'] for h in diff['added']]}")
    print(f"    移除药材: {[h['herb'] for h in diff['removed']]}")
    print(f"    剂量变化: {len(diff['dose_changes'])} 味")
    assert len(diff['added']) == 1
    assert len(diff['removed']) == 1
    assert len(diff['dose_changes']) == 1
    print("  ✓ 通过")

def test_all_patterns():
    print("\n" + "=" * 50)
    print("测试 8: 所有证型覆盖")
    patterns = get_all_patterns()
    print(f"  证型总数: {len(patterns)}")
    for p in patterns:
        print(f"    - {p['name']}: {p['description']}")
    expected = ["气虚", "血虚", "阴虚", "阳虚", "气滞", "血瘀", "痰湿", "湿热"]
    for e in expected:
        assert any(p['name'] == e for p in patterns), f"缺少证型: {e}"
    print("  ✓ 通过")

if __name__ == "__main__":
    try:
        test_symptom()
        test_tongue_pulse_presets()
        test_pattern()
        test_formula()
        test_safety()
        test_dose()
        test_modifier()
        test_all_patterns()

        print("\n" + "=" * 50)
        print("🎉 所有测试通过！")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
