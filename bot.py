import pathlib, base64, os


path = pathlib.Path(__file__).parent.absolute()
os.chdir(path)

with open("config", "r") as f:
    TOKEN = base64.b64decode(bytes(f.read().strip(), "utf-8")).decode('utf-8')
