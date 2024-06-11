import random
names = ["Harry", "James", "Jack"]
print(names)
# 🚨 Remember to remove the print statement above when you submit.
# print(f"Length of names: {len(names)}")
name_length = len(names)
random_name_picker = random.randint(0, name_length - 1)
print(f"{names[random_name_picker]} is going to buy the meal today!")