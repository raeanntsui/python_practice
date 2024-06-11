line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?\n")
position_in_line = int(position[1])

if position[0] == "A":
    line1[position_in_line - 1] = "X"
elif position[0] == "B":
    line2[position_in_line - 1] = "X"
else:
    line3[position_in_line - 1] = "X"

print(f"{line1}\n{line2}\n{line3}")