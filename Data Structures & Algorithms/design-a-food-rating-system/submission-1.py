from collections import defaultdict
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.hashmap_food_to_rating = {}
        self.hashmap_food_to_cuisine = {}
        self.hashmap_c = defaultdict(list)
        for food, cuisine, rating in zip(foods,cuisines,ratings):
            self.hashmap_food_to_rating[food] = rating
            self.hashmap_food_to_cuisine[food] = cuisine
            heapq.heappush(self.hashmap_c[cuisine],(-rating,food))
    def changeRating(self, food: str, newRating: int) -> None:
        self.hashmap_food_to_rating[food] = newRating
        current_c = self.hashmap_food_to_cuisine[food]
        heapq.heappush(self.hashmap_c[current_c],(-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.hashmap_c[cuisine]
        while True:
            neg_rate, food = heap[0]
            if self.hashmap_food_to_rating[food] == -neg_rate:
                return food
            heapq.heappop(heap)
