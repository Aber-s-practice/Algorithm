import importlib
import os

SELF_PATH = os.path.dirname(os.path.abspath(__file__))

for each in os.listdir(SELF_PATH):
    if each.startswith("test_") and each.endswith(".py"):
        importlib.import_module("."+".".join(each.split(".")[:-1]), __package__)
