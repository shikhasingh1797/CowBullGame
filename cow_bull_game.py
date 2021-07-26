import random
print("Welcome to the Cows and Bulls Game!")
end = 0
lis = []
i=0
while len(lis) < 4:
    r = random.randint(0,9)
    if r not in lis :
        lis.append(r)
    i=i+1
print(lis)
i=0
chance=5
while i<5:
    user = int(input("Enter your guess: "))
    st=str(user)
    map1=map(int,st)
    guess=list(map1)
    j=0 
    cow=0
    bull=0
    while j<4:
        if guess[j] == lis[j]:
            bull=bull+1
        if guess[j] in lis:
            if guess[j] != lis[j]:
                cow= cow + 1
        j=j+1
    print(guess)
    print("Cows: "+str(cow)+". Bulls: "+str(bull)+".")
    if guess==lis:
        print("Congractulations , Your guess is correct , you won the game")
        break
    else:
        print("Your guess is wrong .........")
        chance=chance-1
        print("Your remaining chance is=",chance)
    i=i+1
if chance==0:
    print("Sorry , You loss the game")