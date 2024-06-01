import random
print("you have 10 tries to guess number!!")

tries=10
while tries>0:
    random_number = random.randint(1, 30)
    #print(random_number)
    number = int(input("Enter number between 1 to 30: "))
    print(number)
    if random_number==number:
        print("yes your guessed number is correct")
        break
    else:
        tries-=1
if tries==0:
    print("you are out of tries!")
