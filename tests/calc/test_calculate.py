import pytest

from src.calc.calculate import add


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 2),
        (1, 2, 3),
        (11, 22, 33),
        (-1, 1, 0),
    ],
)
def test_add(a: int, b: int, expected: int) -> None:
    actual = add(a, b)
    assert actual == expected
