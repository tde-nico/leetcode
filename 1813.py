class Solution:
	def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
		w1 = sentence1.split(' ')
		w2 = sentence2.split(' ')
		if len(w1) < len(w2):
			w1, w2 = w2, w1
		
		s, e = 0, 0
		n1, n2 = len(w1), len(w2)
		
		while s < n2 and w1[s] == w2[s]:
			s += 1
		
		while e < n2 and w1[n1 - e - 1] == w2[n2 - e - 1]:
			e += 1
			
		return s + e >= n2
