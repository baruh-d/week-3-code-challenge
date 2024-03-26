class Customer:
    all_customers = []

    def __init__(self, first_name, last_name):
        self._first_name = None
        self._last_name = None
        self.reviews = []
        self.first_name = first_name
        self.last_name = last_name
        Customer.all_customers.append(self)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._first_name = value
        else:
            raise ValueError("First name must be a string of length 1 to 25")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._last_name = value
        else:
            raise ValueError("Last name must be a string of length 1 to 25")

    def num_negative_reviews(self):
        return sum(1 for review in self.reviews if review.rating <= 2)

    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self.reviews)


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = None
        self.reviews = []
        self.name = name
        Restaurant.all_restaurants.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            raise ValueError("Restaurant name must be a string of length 1 to 25")

    def average_star_rating(self):
        ratings = [review.rating for review in self.reviews]
        if ratings:
            return round(sum(ratings) / len(ratings), 1)
        else:
            return 0.0

    @classmethod
    def top_two_restaurants(cls):
        sorted_restaurants = sorted(
            cls.all_restaurants,
            key=lambda restaurant: restaurant.average_star_rating(),
            reverse=True
        )
        return sorted_restaurants[:2]


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer")
        if not isinstance(restaurant, Restaurant):
            raise TypeError("Restaurant must be an instance of Restaurant")
        if not isinstance(rating, int):
            raise TypeError("Rating must be an integer")
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
