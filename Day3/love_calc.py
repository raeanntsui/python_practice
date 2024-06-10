print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n") # What is your name?
name2 = input("What is your lover's name?\n") # What is their name?

true_counter_name1 = 0
true_counter_name2 = 0

love_counter_name1 = 0
love_counter_name2 = 0

for letter in name1:
  if letter in ("t", "r", "u", "e", "T", "R", "U", "E"):
    true_counter_name1 += 1

for letter in name1:
  if letter in ("l", "o", "v", "e", "L", "O", "V", "E"):
    love_counter_name1 += 1

for letter in name2:
  if letter in ("t", "r", "u", "e", "T", "R", "U", "E"):
    true_counter_name2 += 1  

for letter in name2:
  if letter in ("l", "o", "v", "e", "L", "O", "V", "E"):
    love_counter_name2 += 1

true_score = (true_counter_name1 + true_counter_name2)
print(f"True score: {true_score}")
love_score = (love_counter_name1 + love_counter_name2)
print(f"Love score: {love_score}")
true_love_score = str(true_score) + str(love_score)
int_love_score = int(true_love_score)

if int_love_score < 10 or int_love_score > 90:
  print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif 40 <= int_love_score <= 50:
  print(f"Your score is {true_love_score}, you are alright together.")
else:
  print(f"Your score is {true_love_score}.")