import pytest
from solve import Solution


@pytest.mark.parametrize(
    "a, b, output", [("11", "1", "100"), ("1010", "1011", "10101")]
)
class TestSolution:
    def test_addBinary(self, a: str, b: str, output: str):
        sc = Solution()
        assert (
            sc.addBinary(
                a,
                b,
            )
            == output
        )
