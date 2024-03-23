from dotenv import load_dotenv
from HelgeChef import HelgeChef

load_dotenv()


def run():
    chef = HelgeChef()
    ingredients_input = input("Type some ingredients:\n")
    dish = chef.query(ingredients_input)
    print("\n")
    recipe = chef.query(dish)
    print("\n")
    critique = chef.query(recipe)


if __name__ == "__main__":
    run()
