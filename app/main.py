# flake8: noqa: *
from app.calculate import calculate_products, calculate_distance
from app.parser import parser


def shop_trip() -> None:
    config_file = parser("app/config.json")
    fuel_price, customers, shops = config_file
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        best_price = 0
        for shop in shops:
            if best_shop is None:
                best_shop = shop
                best_price = (calculate_products(customer, shop)
                              + calculate_distance(customer, shop, fuel_price))
                print(f"{customer.name}'s trip to the {shop.name} costs {best_price}")
                continue
            new_price = calculate_products(customer, shop) + calculate_distance(customer, shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {new_price}")
            if new_price < best_price:
                best_price = new_price
                best_shop = shop
        if customer.money >= best_price:
            print(f"{customer.name} rides to {best_shop.name}")
            customer.money -= best_price
            best_shop.customer_purchase(customer)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
            continue
        print(f"{customer.name} doesn't have enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
