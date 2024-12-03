from day2 import count_safe_reports, report_is_safe
import pytest

def test_day2():
    result = count_safe_reports(input="test_input.txt", detect_variance=True)
    assert result == 472 #472 is the correct value

def test_day2_single_item_removed():
    result = count_safe_reports(input="test_input.txt", detect_variance=False, detect_variance_single_element_removed=True)
   # 518 is too low
    assert result == 520 #520 is the correct value

@pytest.mark.parametrize(
"test_input, expected_output", [
   (
       [1,2,3,4],
       True,
   ),
   (
       [1,2,2,4],
       False,
   ),
   (
       [4,3,2,1],
       True,
   ),
],
ids=["increasing_by_1", "increasing_but_staying_the_same", "decreasing_by_1"]
)
def test_report_is_safe(test_input: list[int], expected_output: bool) -> None:
    result = report_is_safe(test_input)
    assert result == expected_output

@pytest.mark.parametrize(
"test_input, expected_output", [
   (
       [1,2,3,4],
       True,
   ),
   (
       [1,2,2,4],
       True,
   ),
   (
       [4,3,2,1],
       True,
   ),
   (
       [3,2,6,1],
       True,
   ),
   (
       [6,1,2,3],
       True,
   ),
   (
       [1,2,3,6],
       True,
   ),
   (
       [6,3,2,1],
       True,
   ),
   (
       [3,2,1,6],
       True,
   ),
   (
       [7,6,2,1],
       False,
   ),
   (
       [17,14,9,13],
       True,
   ),
   (
       [7,6,4,2,1],
       True,
   ),
   (
       [1,2,7,8,9],
       False,
   ),
   (
       [9,7,6,2,1],
       False,
   ),
   (
       [1,3,2,4,5],
       True,
   ),
   (
       [8,6,4,4,1],
       True,
   ),
   (
       [1,3,6,7,9],
       True,
   ),
   (
       [48,46,47,49,51,54,56],
       True,
   ),
],
ids=[
    "safe_increasing_by_1",
    "safe_increasing_but_staying_the_same",
    "safe_decreasing_by_1",
    "safe_one_bad_large_in_decreasing_set",
    "safe_bad_start_increasing",
    "safe_one_bad_end_increasing",
    "safe_one_bad_start_decreasing",
    "safe_e_bad_end_decreasing",
    "unsafe_two_bad_start_decreasing",
    "safe_one_bad_drop_decreasing",
    "safe_without removing any level",
    "unsafe_two_bad_jumps_increasing",
    "unsafe_two_bad_jumps_decreasing",
    "Safe by removing the second level, 3",
    "Safe by removing the third level, 4",
    "Safe without removing any level",
    "safe_bad_first_element"]
)
def test_report_is_safe_when_removing_one(test_input: list[int], expected_output: bool) -> None:
    result = report_is_safe(test_input, True)
    assert result == expected_output
