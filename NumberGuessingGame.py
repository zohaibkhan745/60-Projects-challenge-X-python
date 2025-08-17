import random
print("-*-Welcome to NUMBER GUESSING GAME-*-\n-*-To end Game press Ctr + C-*-\n -*-Guess Number between 1 to 5-*-")
while True:
    try:
        x =  int(input("Your Guess : "))
        y = random.randint(1,5)
        if x == y:
            print("You Win num is :", y)
        else:
            print("try again")
    except ValueError:
        print("Please Enter int 1-5")
    except KeyboardInterrupt:
        print("thanks for playing")
        break

    
