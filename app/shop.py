from dataclasses import dataclass
from decimal import Decimal

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list
    products: dict[str, float]

    def customer_purchase(self, customer: Customer) -> None:
        print("\nDate: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_price = Decimal("0")
        for product, value in customer.product_cart.items():
            price = Decimal(str(value)) * Decimal(str(self.products[product]))
            price = int(price) if price == price.to_integral() else price
            print(f"{value} {product}s for {price} dollars")
            total_price += price
        print(f"Total cost is {total_price} dollars\nSee you again!\n")
