class Bird:
    def move(self):
        print("I'm moving.")

class FlightBird(Bird):
    def move(self):
        print("I'm flying.")

class FlightlessBird(Bird):
    def move(self):
        print("I'm walking.")

def make_bird_move(bird: Bird):
    bird.move()

if __name__ == "__main__":
    eagle = FlightBird()
    penguin = FlightlessBird()

    make_bird_move(eagle)
    make_bird_move(penguin)