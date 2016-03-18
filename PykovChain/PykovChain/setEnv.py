import os

def setupEnv():
    with open(".env") as file:
        data = file.readlines()
        for line in data:
            statements = line.split(": ")
            for s in statements:
                print(s.strip())
            os.environ[statements[0].strip()] = statements[1].strip()