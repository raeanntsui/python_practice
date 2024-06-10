import random
print(names)
# 🚨 Remember to remove the print statement above when you submit.
# print(f"Length of names: {len(names)}")
random_name_picker = random.randint(0, len(names))
print(f"{names[random_name_picker]} is going to buy the meal today!")