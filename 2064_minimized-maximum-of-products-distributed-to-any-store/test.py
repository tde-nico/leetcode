import pytest
from solve import Solution


@pytest.mark.parametrize(
    "n, quantities, output",
    [(6, [11, 6], 3), (7, [15, 10, 10], 5), (1, [100000], 100000)],
)
class TestSolution:
    def test_minimizedMaximum(self, n: int, quantities: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimizedMaximum(
                n,
                quantities,
            )
            == output
        )
