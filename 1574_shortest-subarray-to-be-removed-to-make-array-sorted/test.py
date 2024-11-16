import pytest
from solve import Solution


@pytest.mark.parametrize(
    "arr, output",
    [([1, 2, 3, 10, 4, 2, 3, 5], 3), ([5, 4, 3, 2, 1], 4), ([1, 2, 3], 0)],
)
class TestSolution:
    def test_findLengthOfShortestSubarray(self, arr: List[int], output: int):
        sc = Solution()
        assert (
            sc.findLengthOfShortestSubarray(
                arr,
            )
            == output
        )
