import random

x =[]
smallBag = ["W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B"]

bigBag = ["W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B",
"W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B","W","W","W","W","W","W","W","W","W","W","B","B","B","B","B","B","B","B","B","B"]

print("This is tool for find solution")

def getItemsFromBag(bag,count_balls):
    whiteballs = 0
    blackballs = 0
    for x in range(10000):
        pick = random.choices(bag,k=2)
        if pick[0] == pick[1]:
            if pick[0] == "W" and pick[1] == "W":
                whiteballs = whiteballs + 1
            if pick[0] == "B" and pick[1] == "B":
                blackballs = blackballs + 1
    print(whiteballs/count_balls)
    print(blackballs/count_balls)

getItemsFromBag(smallBag,100)
getItemsFromBag(bigBag,200)

