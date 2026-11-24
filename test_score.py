from marks import total_marks, percentage, grade, required_marks
def test_total_marks():
    assert total_marks([80, 90, 70]) == 240
def test_percentage():
    assert percentage([80, 90, 70]) == 80
def test_grade():
    assert grade(95) == "A+"
    assert grade(85) == "A"
    assert grade(75) == "B"
    assert grade(65) == "C"
    assert grade(55) == "D"
    assert grade(35) == "F"
def test_required_marks():
    assert required_marks(85, [80, 75, 85], 5) == 92.5
def test_required_marks_high_target():
    assert required_marks(95, [50, 60], 5) == 126.0
def test_all_subjects_completed():
    assert required_marks(80, [80, 90, 70], 3) is None
    