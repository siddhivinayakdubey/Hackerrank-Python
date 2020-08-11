import random
output=""
machine=""
game_list = []
print("Hello Player. Let's get started right away")
print("rules: ")
print("1. To start every round, you need to input a word (it should be a valid word within any dictionary)")
print("2 The computer will give you the next word according to the last letter of your word and so on")
print("You can quit any time")
print("shall we begin? please reply with y/n")
reply = str(input("shall we begin? please reply with Y for yes or N for no: "))
proceed="y" or "Y"
if reply==proceed:
    for i in range(10):
        print("Welcome to round: " + str(int(i)))


        fobj = open("Dictionary.txt")
        text = fobj.read().strip().split()

        while True:
            print("New word is ", output)
            word = str(input("Please enter a word to start : "))
            if (output != ""):
                if word[0] == output[-1]:
                    if word in game_list:
                        print("You cannot reuse this word again")
                        continue
                    if word == "":
                        continue
                    if word in text:
                        game_list.append(word)
                        for match in text:
                            if match[0]== word[-1] :
                                with open("match.txt", "a") as f:
                                    f.write(match + "\n")
                        break
                    else:
                        print("Your word is not valid since it's not in dictionary, Please retry")
                        continue
                else:
                    print("You need to continue with last alphabet of the previous word")
                    continue
            else:
                if word in game_list:
                    print("You cannot reuse this word again")
                    continue
                if word == "":
                    continue
                if word in text:
                    game_list.append(word)
                    for match in text:
                        if match[0]== word[-1]:
                            with open("match.txt", "a") as f:
                                f.write(match + "\n")
                    break
                else:
                    print("Your word is not valid since it's not in dictionary, Please retry")
                    continue

        fobj.close()

        f = open("match.txt", "r")
        machine = str(random.choice(f.readlines())).strip("\n")
        game_list.append(str(machine))
        print(machine)
        print(game_list)
        output = machine[-1]
        f.close()
        f = open("match.txt", "w")
        f.write("")


else:
    exit(print("Thanks for playing Your score is: "))
