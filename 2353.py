class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = {}
        self.foods = {}
        for i in range(len(foods)):
            self.foods[foods[i]] = (cuisines[i], ratings[i])
            c = self.cuisines.get(cuisines[i], [])
            heapq.heappush(c, (-ratings[i], foods[i]))
            self.cuisines[cuisines[i]] = c

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.foods[food]
        self.foods[food] = (c, newRating)
        heapq.heappush(self.cuisines[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        c = self.cuisines[cuisine]
        while c:
            nr, f = c[0]
            if self.foods[f][1] == -nr:
                return f
            heapq.heappop(c)
        return ""


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)