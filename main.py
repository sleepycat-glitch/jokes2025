# Vanessa Rodriguez and Ayelen Cardenas

# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes
# sequencing - multiple lines of code
# no parameters in code
# no list in code and no function defined
# has different pathways but not dependent on parameters 
# algorithm - does contain sequencing, selection, and iteration

joke_list = ["Calder", "Calder police - I've been robbed!", "Tank", "You are welcome!","Broken pencil", "Nevermind, it's pointless!" ] # list
question = " "
def knock_knock_joke(question): 
    input("Knock Knock") 
    if question == "robbers": 
        input(joke_list[0]) 
        print(joke_list[1]) 
    elif question == "tanks": 
        input(joke_list[2]) 
        print(joke_list[3])
    elif question == "pencils": 
        input(joke_list[4])
        print(joke_list[5])

rating_list = [0]
def rate_calculator(x):
    rating_list.append(x)
    new_rating = sum(rating_list) / len(rating_list)
    return new_rating





joke = input("Do you want to hear a joke? (yes/no):") 
if joke == "no":  
    print("Okay suit yourself!") 
else: 
    print("Great, Let's Play")
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ") 

knock_knock_joke(question)   
joke = input("Do you want to hear another joke or are you finished? (yes/no):") 
while not(joke == "no"):
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ") 
    knock_knock_joke(question)
    joke = input("Do you want to hear another joke or are you finished? (yes/no):")

if joke == "no": 
    rate = int(input("Please rate our game 1-10! ")) 
    print(rate_calculator(rate), "percent satisfication rate") 
    friend = input("Would you recommend this game to a friend? ") 

    if friend == "yes" or friend == "maybe": 
        print("Thanks, we appreciate it. ") 
    else: 
        print("Sorry you did not enjoy it. ") 
