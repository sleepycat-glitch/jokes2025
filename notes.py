# Code Requirements
# Input: Use any valid input source such as a keyboard, mouse, microphone, data stream, or file.
# Output: Must depend on the input provided.
# List Usage:
# Must justify why a list is better than alternatives.
# Examples include picking items, random selections, or using list methods like append.
# Function Requirements:
# Must have a parameter.
# Include sequencing (multiple lines of code).
# Utilize selection (e.g., if/else statements).
# Use iteration (e.g., loops like for or while).
# Take different paths based on parameter values.

# no functions or parameters
# sequencing - yes, multiple lines of code
# different pathways - yes, but not dependent on parameter values


joke = input("Do you want to hear a joke? ")  #input
if joke == "no": #selection
    print("Okay suit yourself!") #output
while joke == "yes": #iteration
    print("Great, Let's Play") #output
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ") #input
    if question == "robbers": #selection
        input("Knock Knock ") #input
        input("Calder") #input
        print("Calder police - I've been robbed!") #output
        joke = input("Do you want to hear another joke or are you finished? ") #input
    elif question == "tanks": #selection
        input("Knock Knock ") #input
        input("Tank ") #input
        input("You are welcome! ") #input
        joke = input("Do you want to hear another joke or are you finished? ") #input
    elif question == "pencils": #selection
        input("Knock Knock ") #input
        input("Broken pencil ") #input
        input("Nevermind, it's pointless! ") #input
        joke = input("Do you want to hear another joke or are you finished? ") #input
if joke == "finished": #selection
    rate = int(input("Please rate our game 1-10! ")) #input
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate") #output
    friend = input("Would you recommend this game to a friend? ") #input

    if friend == "yes" or friend == "maybe": #selection
        print("Thanks, we appreciate it. ") #output
    else: #selection
        print("Sorry you did not enjoy it. ") #output
