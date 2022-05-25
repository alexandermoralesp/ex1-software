from abc import ABC, abstractmethod
import random


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

class StrategyInterface(ABC):
    @abstractmethod
    def execute():
        print("Abstract method")

class FiveEvenNumbersStrategy(StrategyInterface):
    def __init__(self):
        self.numbers = []

    def execute(self):
        random.seed()
        number = random.randint(0, 100)
        while (number in self.numbers and number % 2 != 0 and len(self.numbers) != 5):
            number = self.numbers.append(random.randint(0, 100))
        self.numbers.append(number)
        return number


class FiveOddNumbersStrategy(StrategyInterface):
    def __init__(self):
        self.numbers = []

    def execute(self):
        random.seed()
        number = random.randint(0, 100)
        while (number in self.numbers and number % 2 == 0 and len(self.numbers) != 5):
            number = random.randint(0, 100)
        self.numbers.append(number)
        return number


class OnePrimeNumberStrategy(StrategyInterface):
    def __init__(self):
        self.number = 0

    def execute(self):
        random.seed()
        number = random.randint(0, 100)
        while (not is_prime(number)):
            number = random.randint(0, 100)
        self.number = number
        return number


class ThreeeNumbersMultipleTenStrategy(StrategyInterface):
    def __init__(self):
        self.numbers = []

    def execute(self):
        random.seed()
        number = random.randint(0, 100)
        while (number in self.numbers and number % 10 != 0 and len(self.numbers) != 3):
            number = random.randint(0, 100)
        self.numbers.append(number)
        return number


class TwoNumbersMultipleTwentyFiveStrategy(StrategyInterface):
    def __init__(self):
        self.numbers = []

    def execute(self):
        random.seed()
        number = random.randint(0, 100)
        while (number in self.numbers and number % 25 != 0 and len(self.numbers) != 2):
            number = random.randint(0, 100)
        self.numbers.append(number)
        return number


class ListenerInterface(ABC):
    @abstractmethod
    def on_event(self, event):
        pass


class Listener(ListenerInterface):
    def __init__(self, current_number):
        self.current_number = current_number

    def on_event(self, number):
        self.current_number = number

class Player:
    def __init__(self):
        self.current_number = 0
    def on_event(self, event):
        self.current_number = event

class Context:
    def __init__(self):
        self.strategy: StrategyInterface = None
        self.player :Player = None

    def do_something(self):
        number = self.strategy.execute()
        self.notify(number)

    def set_strategy(self, strategy: StrategyInterface):
        self.strategy = strategy

    def notify(self, event):
        self.player.on_event(event)

    def set_player(self, player: Player):
        self.player=player 
 
# Singleton
class Game:
    _players = []
    _instances = {}
    def __cal__(self,cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def add_player(self, player: Player, strategy: StrategyInterface):
        context = Context()
        listener = Listener(0)
        context.set_strategy(strategy)
        context.subscribe(listener)
        self.players.append(Player(player, strategy))


if __name__ == "__main__":
    print("Examen Parcial")
    game = Game()
    fiveevennumbersstrategy = FiveEvenNumbersStrategy()
    fiveoddnumbersstrategy = FiveOddNumbersStrategy()
    oneprimenumbersstrategy = OnePrimeNumberStrategy()
    threeenumbersmultipletenstrategy = ThreeeNumbersMultipleTenStrategy()
    twonumbersmultipletwentyfivestrategy = TwoNumbersMultipleTwentyFiveStrategy()
