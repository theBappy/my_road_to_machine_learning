class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} - {self.color} - {self.model}")


class Actor:
    def __init__(self, hero, movie, nationality, is_busy):
        self.hero = hero
        self.movie = movie
        self.nationality = nationality
        self.is_busy = is_busy

    def can_act(self):
        print(f"{self.hero} is a brilliant actor")
    def can_sing(self):
        print(f"{self.hero} can't sing well ")
    def can_dance(self):
        print(f"{self.hero} dance very well")

    