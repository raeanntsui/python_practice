print("Welcome to Treasure Island. Your mission is to find the treasure!")
first_choice = input("You encounter a fork in the path. There is a wizard to your left and an empty road to the right. Type 'left' or 'right' to proceed.\n")

if first_choice == "left":
    second_choice = input("The wizard asks whether you would like a dance battle with him. Do you accept? Please type 'yes' or 'no'.\n")
    if second_choice == "yes":
        third_choice = input("The wizard is amazed by your dance moves. He gives you a magic bean, do you accept? Please type 'yes' or 'no'.\n")
        if third_choice == 'yes':
            fourth_choice = input("You accept the bean and plant it. Do you climb the stalk? Please type 'yes' or 'no'.\n")
            if fourth_choice == 'yes':
                print("Congratulations! You found the treasure! It was at the top of the magic beanstalk! And its a minion :)")
                print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠤⠴⠦⠤⣤⣄⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠋⠉⠀⠀⠀⠀⣠⣾⣿⣯⣿⣿⣿⣭⡙⢶⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⣋⡤⢒⣤⣤⢭⣄⣠⡴⢣⣿⣿⡟⠉⠀⠀⠈⠙⢦⢿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⢁⡴⣹⣿⣿⡿⠿⠿⢶⣌⠛⢿⣿⡏⢠⣾⣿⣦⠀⠀⠈⣿⣿⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⢀⡎⣸⣿⡿⠋⠀⣀⣀⠀⠈⢷⢦⢻⡇⠘⠿⠿⠟⠀⠀⢠⢻⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢀⣿⠁⣿⣿⠀⠀⣿⣿⡿⡇⠀⠘⣿⣅⠹⣄⠀⠀⠀⠀⢠⢋⡿⠛⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⣿⢻⣧⣝⢿⡄⠀⠈⠛⠛⠁⠀⣸⣽⣿⣿⣚⠿⢦⣤⣾⣟⡿⠋⠀⢹⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣦⣿⣟⢦⣻⣄⠀⠀⠀⠀⣠⣷⣯⡿⠋⠋⠛⠛⠋⠉⠁⠀⠀⠀⠈⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠁⠉⠉⠙⠳⢯⣟⣻⣷⣶⣻⡯⠟⠋⠀⠀⠀⠀⢀⡴⠄⠀⠀⠀⠀⠀⢻⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⢦⣀⠀⠀⠀⠀⠈⠙⠋⠙⠷⠤⣤⣤⣤⠤⠴⠚⠁⠀⠀⠀⠀⠀⠀⢀⣼⣷⠀⠀
⠀⠀⢀⣠⣶⣿⣿⣷⣦⣄⠙⣦⣉⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡄⠀
⠀⢰⣿⣿⣁⣨⣿⢿⣯⣽⣧⠀⠉⠳⣄⣽⡷⣦⡀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣤⣶⣴⣶⣾⣿⣿⠋⡄⢹⠀
⣶⣿⣥⣾⣿⣇⣞⣛⣿⣿⣿⠀⠀⠀⠈⠛⢿⣷⣿⣿⡿⠛⢙⣛⣁⣉⣉⣉⣹⣿⣿⣟⣻⣿⣿⣿⣧⢰⣷⣈⡇
⠙⢿⣿⡇⣑⢬⣉⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⣿⢯⡽⠁⠀⢠⠉⠉⠉⠉⠉⠉⣍⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧
⠀⠀⠙⠿⢿⣧⣿⣿⣿⣿⣿⣽⣦⣀⣀⠀⠀⣿⡀⠀⠀⠀⠸⠀⠀⠐⠂⢀⠀⢙⣿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠋
⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣏⡙⢛⡿⠋⠙⠂⠀⠄⠀⠳⠶⠤⢤⣤⣤⠿⢿⣤⣽⠿⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣯⠉⠁⠀⢀⠀⠑⠀⠈⠓⠰⠂⠀⠠⠦⠦⠀⢀⣤⠾⣟⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠿⣿⣿⣿⢿⣟⠀⠀⠀⠀⠙⠻⢶⣤⣤⡄⢰⡄⠀⢶⣴⠟⣷⡀⢚⣿⡟⠀⠀⠀⠀   
⠀⠀⠀⠀⠀⠀⠀⠻⠿⠏⠀⠻⢿⠿⠇⠈⠉⠛⢶⣶⣿⣧⣤⣤⣽⣧⣄⣤⣤⣤⣴⣦⡭⠶⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⡿⠁⠀⢿⣿⣿⣿⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⠃⠀⠀⠻⠿⠿⠿⠿⠗⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀
            """)
            else: 
                print("The wizard is disappointed that you didn't accept his gift. You are vaporized immediately. Game over.")
        else: 
            print("The wizard is disappointed that you didn't accept his gift. You are vaporized immediately. Game over.")
    else:
        print("The wizard is disappointed that you didn't accept his dance off and got offended. You are vaporized immediately. Game over.")
else:
    print("You walk aimlessly and die of dehydration. Game over.")