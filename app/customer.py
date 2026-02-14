from app.car import Car
from decimal import Decimal


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list,
            money: Decimal,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        if isinstance(car, Car):
            self.car = car
        elif isinstance(car, dict):
            self.car = Car(**car)

    def __repr__(self) -> str:
        return (f"Customer(name={self.name}, "
                f"products_cart={self.product_cart}, "
                f"location={self.location}, "
                f"money={self.money}), "
                f"car={self.car}")
