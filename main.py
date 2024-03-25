from dotenv import load_dotenv
from HelgeChef import HelgeChef
from HealthyChef import HealthyChef
from ScottishChef import ScottishChef

load_dotenv()


def run():
    chef = HelgeChef()
    healthy_chef = HealthyChef()
    scottish_chef = ScottishChef()
    ingredients_input = input("Type some ingredients:\n")
    dish = chef.query(ingredients_input)
    print("\n\n")
    recipe = healthy_chef.query(dish)
    print("\n\n")
    critique = scottish_chef.query(recipe)


if __name__ == "__main__":
    run()
