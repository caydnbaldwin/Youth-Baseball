from byu_pytest_utils import max_score, test_files, dialog


@max_score(50)
@dialog(
    test_files / "baseball1.dialog.txt",
    "youth_baseball.py"
)
def test_input_output_1(): ...


@max_score(50)
@dialog(
    test_files / "baseball2.dialog.txt",
    "youth_baseball.py"
)
def test_input_output2(): ...