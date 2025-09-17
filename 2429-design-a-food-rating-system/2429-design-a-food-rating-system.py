class FoodRatings:
    # Min heap based approach O(log(n)) time
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodRateMap = dict(zip(foods, ratings))       # food -> rating
        self.foodCuisineMap = dict(zip(foods, cuisines))   # food -> cuisine
        self.cuisineFoodHeap = defaultdict(list)           # cuisine -> heap

        for f, c, r in zip(foods, cuisines, ratings):
            heapq.heappush(self.cuisineFoodHeap[c], (-r, f))
        
    def changeRating(self, food: str, newRating: int) -> None:
        self.foodRateMap[food] = newRating
        cuisine = self.foodCuisineMap[food]
        heapq.heappush(self.cuisineFoodHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineFoodHeap[cuisine]
        # Lazy removal of outdated ratings
        while heap:
            rating, food = heap[0]
            if -rating == self.foodRateMap[food]:
                return food   # correct top
            heapq.heappop(heap)            


    #O(n) APproach works well for big cases but not for very big cases
    # def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    #     self.foods = foods
    #     self.cuisines = cuisines
    #     self.ratings = ratings 
    #     self.foodRateMap = dict(zip(foods,ratings))
    #     self.cuisineFoodMap = defaultdict(list)

    #     for i in range(len(self.cuisines)):
    #         self.cuisineFoodMap[self.cuisines[i]].append(self.foods[i])

    # def changeRating(self, food: str, newRating: int) -> None:
    #     if food in self.foodRateMap:
    #         self.foodRateMap[food] = newRating
    #         foodidx = self.foods.index(food)
    #         self.ratings[foodidx] = newRating

    #     elif food not in self.foodRateMap:
    #         self.foodRateMap[food] = newRating
    #         self.foods.append(food)
    #         self.ratings.append(newRating)


    # def highestRated(self, cuisine: str) -> str:
    #     foodsIncuisine=[]
    #     cuisineFoodRatings = []
        
    #     # if cuisine in  cuisineFoodMap:
        
    #     foodsIncuisine = self.cuisineFoodMap[cuisine]
        
    #     if len(foodsIncuisine) == 1:
    #         return foodsIncuisine[0]

    #     elif len(foodsIncuisine) > 1:
    #         for i in range(len(foodsIncuisine)):
    #             cuisineFoodRatings.append(self.foodRateMap[foodsIncuisine[i]])
            
    #         maxRating = max(cuisineFoodRatings)
    #         candidates = [f for f in foodsIncuisine if self.foodRateMap[f] == maxRating]

    #         return min(candidates)
            
            # if len(cuisineFoodRatings) == len(set(cuisineFoodRatings)):
            #     maxRating = max(cuisineFoodRatings)
            #     maxRatingId = self.ratings.index(maxRating)
            #     return self.foods[maxRatingId]






        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)