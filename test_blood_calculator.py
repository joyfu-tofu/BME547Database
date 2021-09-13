import pytest


@pytest.mark.parametrize("HDL_value, expected", [
    (65, "Normal"),
    (45, "Borderline Low"),
    (15, "Low"),
    (70, "Normal")])
def test_hdl_analysis(HDL_value, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(HDL_value)
    assert answer == expected

# @pytest.mark.parametrize("in_string, expected", [
# 	("ab", True),
# 	("abs", False),
# 	("123456", False)])
# def test_check_input(in_string, expected):
# 	from blood_calculator import check_input
# 	answer = check_input(in_string)
# 	assert answer == expected
