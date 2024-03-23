from dotenv import load_dotenv

load_dotenv()

from HelgeChefGPT import HelgeChef

dish = HelgeChef.query("parmesan cheese")
