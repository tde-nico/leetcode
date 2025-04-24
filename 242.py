class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		dicts = dict()
		for s in strs:
			tmp = ''.join(sorted(s))
			dicts[tmp] = dicts.get(tmp, []) + [s]
		return list(dicts.values())
