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
    while not(question == " "): 
        input("Knock Knock") 
        if question == "robbers": 
            input(joke_list[0]) 
            print(joke_list[1])
            break 
        elif question == "tanks": 
            input(joke_list[2]) 
            print(joke_list[3])
            break
        elif question == "pencils": 
            input(joke_list[4])
            print(joke_list[5])
            break

rating_list = [10]
def rate_calculator(rate):
    try:
        rating_list.append(rate)
        for i in range(len(rating_list)):
            rate += rating_list[i]
            new_rating = rate/ len(rating_list)
        return new_rating
    except ValueError: 
            print("Please input a number.")
            rate = int(input("Please rate our game 1-10! ")) 


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
    print(str(rate_calculator(rate)) + " percent satisfication rate") 
    friend = input("Would you recommend this game to a friend? ") 

    if friend == "yes" or friend == "maybe": 
        print("Thanks, we appreciate it. ") 
    else: 
        print("Sorry you did not enjoy it. ") 
