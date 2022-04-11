from mysklearn.preprocessing.normalize import find_max


def test_find_max():
    assert find_max([1, 4, 1, 2, 8, 1, 9, 311]) == 311
    assert find_max([32, 17, 55]) == 55

