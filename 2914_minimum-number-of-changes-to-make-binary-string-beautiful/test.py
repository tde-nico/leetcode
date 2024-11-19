import pytest
from solve import Solution


@pytest.mark.parametrize("s, output", [("1001", 2), ("10", 1), ("0000", 0)])
class TestSolution:
    def test_minChanges(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minChanges(
                s,
            )
            == output
        )
