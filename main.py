from abc import ABC, abstractmethod
import random
from re import S


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
    def execute(self):
        print("Abstract method")

class FiveEvenNumbersStrategy(StrategyInterface):
    def __init__(self):
        self.numbers = []

    def execute(self):
        random.seed()
        number = random.randint(0, 100)
        if (len(self.numbers) == 5): return -1
        while (number in self.numbers or number % 2 != 0):
            number = self.numbers.append(random.randint(0, 100))
        self.numbers.append(number)
        return number


class FiveOddNumbersStrategy(StrategyInterface):
    def __init__(self):
        self.numbers = []

    def execute(self):
        random.seed()
        number = random.randint(0, 100)
        if (len(self.numbers) == 5): return -1
        while (number in self.numbers or number % 2 == 0):
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
        if (len(self.numbers) == 3): return -1
        while (number in self.numbers or number % 10 != 0):
            number = random.randint(0, 100)
        self.numbers.append(number)
        return number


class TwoNumbersMultipleTwentyFiveStrategy(StrategyInterface):
    def __init__(self):
        self.numbers = []

    def execute(self):
        random.seed()
        number = random.randint(0, 100)
        if (len(self.numbers) == 2): return -1
        while (number in self.numbers or number % 25 != 0):
            number = random.randint(0, 100)
        self.numbers.append(number)
        return number
class PlayerInterface(ABC):
    @abstractmethod
    def play(self):
        print("Abstract method")

class Player:
    def __init__(self):
        self.current_number = 0
    def play(self, number):
        self.current_number = number

class Context:
    def __init__(self):
        self.strategy: StrategyInterface = None
        self.player :Player = None

    def do_something(self):
        number = self.strategy.execute()
        self.notify(number)
        return number

    def set_strategy(self, strategy: StrategyInterface):
        self.strategy = strategy

    def notify(self, number):
        self.player.play(number)

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

    def add_player(self,strategy: StrategyInterface):
        context = Context()
        player = Player()
        context.set_strategy(strategy)
        context.set_player(player)
        self._players.append(context)
    
    def start(self):
        finished_players = []
        # TODO: Testing
        # max_number_of_times = 1000
        # i = 0
        # while (i < max_number_of_times):
        #     status = 0
        #     for i in range(len(self._players)):
        #         if (i not in finished_players):
        #             status = self._players[i].do_something()
        #             if (status == 0):
        #                 finished_players.append(i)
        #             if (len(finished_players) == len(self._players)):
        #                 break
        #     i += 1

if __name__ == "__main__":
    print("Examen Parcial")
    game = Game()
    fiveevennumbersstrategy = FiveEvenNumbersStrategy()
    fiveoddnumbersstrategy = FiveOddNumbersStrategy()
    oneprimenumbersstrategy = OnePrimeNumberStrategy()
    threeenumbersmultipletenstrategy = ThreeeNumbersMultipleTenStrategy()
    twonumbersmultipletwentyfivestrategy = TwoNumbersMultipleTwentyFiveStrategy()
    game.add_player(fiveevennumbersstrategy)
    game.add_player(fiveoddnumbersstrategy)
    game.add_player(oneprimenumbersstrategy)
    game.add_player(threeenumbersmultipletenstrategy)
    game.add_player(twonumbersmultipletwentyfivestrategy)
    game.start()
