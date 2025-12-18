from utils.math_utils import efficiency_score


def test_efficiency_score():
    score = efficiency_score(10, 2000)
    assert score > 0
