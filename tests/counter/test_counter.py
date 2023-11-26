from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    word = 'Python'
    result = 1639
    assert count_ocurrences(path, word) == result
