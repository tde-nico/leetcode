import bisect

class Solution:
	def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
		items.sort()
		max_beauty_at_price = []
		current_max_beauty = 0
		for price, beauty in items:
			current_max_beauty = max(current_max_beauty, beauty)
			max_beauty_at_price.append((price, current_max_beauty))
		
		sorted_queries = sorted((q, i) for i, q in enumerate(queries))
		res = [0] * len(queries)
		for query, original_index in sorted_queries:
			idx = bisect.bisect_right(max_beauty_at_price, (query, float('inf'))) - 1
			if idx >= 0:
				res[original_index] = max_beauty_at_price[idx][1]
		
		return res
		