from faker import Factory
import random

fake = Factory.create()

genders = ["male", "female"]

with open("popular-names.txt", "w") as f:
    for _ in range(100):
        f.write(
            f"{fake.name()}\t{random.choice(genders)}\t{random.randint(1, 10000)}\t{random.randrange(1990, 2020)}\n"
        )
