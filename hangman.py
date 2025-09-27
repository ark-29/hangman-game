import random

words =[
    #Fruits
    "apple", "banana", "orange", "mango", "grape", "cherry", "lemon", "lime", "peach", "pear",
    "plum", "melon", "kiwi", "papaya", "guava", "apricot", "fig", "date", "coconut", "berry",

    # Animals
    "dog", "cat", "lion", "tiger", "bear", "wolf", "horse", "cow", "goat", "sheep",
    "zebra", "camel", "rabbit", "deer", "fox", "monkey", "panda", "giraffe", "hippo", "donkey",

    # Colors
    "red", "blue", "green", "yellow", "white", "black", "pink", "brown", "gray", "purple",
    "gold", "silver", "orange", "violet", "indigo", "beige", "teal", "maroon", "navy", "cyan",

    # Nature
    "sun", "moon", "star", "sky", "cloud", "rain", "snow", "wind", "storm", "light",
    "tree", "leaf", "flower", "grass", "river", "stone", "fire", "earth", "mountain", "ocean",

    # Vehicles
    "car", "bus", "train", "plane", "boat", "bike", "truck", "jeep", "taxi", "van",
    "ship", "scooter", "cart", "tram", "subway", "cycle", "canoe", "rocket", "motor", "lorry",

    # Objects
    "pen", "book", "bag", "chair", "table", "desk", "board", "paper", "ruler", "clock",
    "phone", "lamp", "bed", "cup", "plate", "bottle", "key", "lock", "door", "window",

    # Sea Life
    "fish", "bird", "frog", "snake", "duck", "hen", "deer", "crab", "shark", "whale",
    "seal", "eel", "lobster", "octopus", "squid", "dolphin", "jellyfish", "stingray", "starfish", "turtle",

    # Clothes
    "hat", "shoe", "dress", "shirt", "pants", "coat", "socks", "belt", "cap", "tie",
    "scarf", "glove", "skirt", "jacket", "boots", "sandal", "shorts", "uniform", "sweater", "hoodie",

    # Food & Drinks
    "milk", "rice", "bread", "cake", "sugar", "salt", "water", "tea", "coffee", "juice",
    "butter", "cheese", "egg", "meat", "fish", "soup", "corn", "honey", "pasta", "pizza",

    # House
    "home", "door", "room", "wall", "floor", "roof", "lamp", "bed", "cup", "plate",
    "garden", "gate", "yard", "stairs", "mirror", "sofa", "shelf", "cushion", "toilet", "bucket",

    # Actions
    "run", "walk", "jump", "sit", "stand", "eat", "drink", "read", "write", "sleep",
    "play", "sing", "dance", "swim", "climb", "think", "talk", "laugh", "cry", "smile"
]
word=random.choice(words)
word_letters=set(word)
guessed_word=""

display=["_"]*len(word)
warning=3
if len(word)>6:
    lives=len(word)
else:
    lives=6
guessed_letters=[]
while lives>0 and "_" in display:
    print("\n")
    guess=input("Enter a character: ")
    if guess.isalpha() and len(guess)==1:
        if guess in word_letters:
            for i in range(len(word)):
                if word[i]==guess:
                    display[i]=guess
                    print(*display)
        else:
            print("\n",f"Oops reamining lives:{lives-1}")
            lives-=1
    else:
        if warning!=1:
            print("Enter a Valid character")
            warning-=1
        else:
            break
while True:
    if lives==0:
        guessed_word=input("Last chance Guess the word: ")
        if guessed_word==word:
            print("You Won! the Word is--->",guessed_word)
            break
        else:
            print("The word is----->  ",word)
            break
    else:
        if "_"not in display:
            print("You Won","\n")
            break

