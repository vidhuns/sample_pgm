import random

print("Enter your name")
name= input("")

print("Hi "+ name + ", I have one number in my mind, can you guess?")
magic_num = random.randint(1, 20)
print(magic_num)

print("########you have only 5 attempts#########")
for guess in range(1, 6):
    print("\nThis is your " + str(guess)+ " attempt")
    print("Can you enter the guessed number?")
    guessed_num = int(input())

    if(guessed_num > magic_num):
        print("The guessed number " + str(guessed_num) + " is too high")
    elif(guessed_num < magic_num):
        print("The guessed number " + str(guessed_num) + " is too low")
    else:
        break

if guessed_num == magic_num:
     print("Hooray ! You guessed the correct number awesome")
else:
    print("#############Sorry, you tried your maximum attempt " + str(guess)+"###########")
    print("So I say for you, the number in my mind is " + str(magic_num))
            
