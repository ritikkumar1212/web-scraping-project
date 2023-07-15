player = input('Enter your name ')
print(f"Welcome {player} to our quiz game.")

play = input("Do you want to start the game. ")
if play.lower() != "yes":
    quit()

print("Ok let's start playing.")
# p for calculating points
p = 0

q1 = input("who is the prime minister of india? ")
if q1.lower() == "narendra modi":
    print("Congratulation! your answer is correct.")
    p = p+1
else:
    print("Oopss! Your answer is incorrect.")

move = input("Press Enter to continue ")

q1 = input("cpu stands for ")
if q1.lower() == "central processing unit":
    print("Congratulation! your answer is correct.")
    p = p + 1
else:
    print("Oopss! Your answer is incorrect.")

move = input("Press Enter to continue ")

q1 = input("RAM stands for ")
if q1.lower() == "random access memory":
    print("Congratulation! your answer is correct.")
    p = p + 1
else:
    print("Oopss! Your answer is incorrect.")

move = input("Press Enter to continue ")

q1 = input("199 - 88 = ")
if q1 == "111":
    print("Congratulation! your answer is correct.")
    p = p + 1
else:
    print("Oopss! Your answer is incorrect.")

move = input("Press Enter to continue ")

print(f"your total correct answer is {p}")




