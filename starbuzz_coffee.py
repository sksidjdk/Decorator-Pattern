from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self):
        self._description = "Unknown Beverage"

    def get_description(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        pass

class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Espresso"

    def cost(self) -> float:
        return 1.99

class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89

class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99

class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self) -> str:
        pass

class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Milk"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20

class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return self._beverage.cost() + 0.15

class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

def main():
    print("=== 订单 1: 浓缩咖啡 ===")
    beverage1 = Espresso()
    print(f"{beverage1.get_description()} ${beverage1.cost():.2f}")

    print("\n=== 订单 2: 深焙咖啡，双倍摩卡，加奶 ===")
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Milk(beverage2)
    print(f"{beverage2.get_description()} ${beverage2.cost():.2f}")

    print("\n=== 订单 3: 综合咖啡，加豆浆，加摩卡，加奶泡 ===")
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${beverage3.cost():.2f}")

if __name__ == "__main__":
    main()
