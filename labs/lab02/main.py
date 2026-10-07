# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header

# CS31 Lab Activity 2
# October 7, 2026
# Sammy Browning
# 

# Create a 5 question quiz
# Decide a theme
# Determine the format whether multiple choise or fill in the blank
# Multiple choice is probably best

# Output a title for the program
print("Sammy's Mini Geography Quiz")
print() # prints an empty line
print("~" * 20) # print a line of 20 squiggles 

# Ask the user for their name and greet them
# Use their name again in your output
print()
username = input("What is your name? ")
print(f"Hello, {username}!")    # this is an f-string format

# Ask if the user would like to take a quiz
print()
start_quiz = input("Wanna see what you know? Y/N ")
if start_quiz.upper() == "Y" or start_quiz == "y" or start_quiz == "Yes" or start_quiz == "yes" or "yeh" or "yuh" or "yis" or "yiss" or "yisss" or "yissss" or "yus" or "yuss" or "yusss":
    print("Sweet! Let's check it out.")

elif start_quiz == "N" or start_quiz == "n":
    print("Aww, we'll try it another time then <3 ")
    # run test

else: # if they type an invalid response, address it
    print("Come again, chief? Do you wanna try some Geography: Y or N?")

#put our quiz questions here all indented
# START OUR QUIZ QUESTIONS

# Set our counter to 0
counter = 0

# Question 1
print("Here's your first one.")
q1 = input("In which country is Alabama located?"   )
if q1 == "U.S.A." or "U.S." or "usa" or "us" or "United States" or "united states" or "Unites States of America" or "united states of america" or "America" or "America":
    # update my counter because they got the answer correct
    counter += 1    # shorthand for counter = counter + 1
    print("See what I mean? You recognized one of our states.")
else:   #INCORRECT
    print("Already pulling my leg, huh? Maybe you want something out of the U.S. Let's try the next one.")

# Question 2
q2 = input("What is the capitol of Japan?"   )
if q2 == "Tokyo" or "tokyo" or "Kyoto" or "kyoto":
    # update my counter because they got the answer correct
    counter += 1    # shorthand for counter = counter + 1
    print(f"So you WERE pulling my leg. Nice job, {username}. Let's jump to another country.")
else:   #INCORRECT
    print("If you guessed Kyoto, I'll give you a point. It USE to be the capitol... for 1000 years. Crazy, right?")

    # Question 3
q3 = input("Which continent would you find the Congo?")
if q3 == "Africa" or "africa":
    # update my counter because they got the answer correct
    counter += 1    # shorthand for counter = counter + 1
    print("Clever clever. You paid attention in Geography. Maybe you'll guess the next one, too.")
else:   #INCORRECT
    print("Okay okay, maybe you don't like Geography. Or maybe you need something other than capitols.")

    # Question 4
    # Use a non-capitol question
q4 == input("Which is bigger: an ocean or a sea?")
if q4.upper () == "an ocean" or "ocean":
    # update my counter because they got the answer correct
    counter += 1    # shorthand for counter = counter + 1
else:   #INCORRECT
    print("Maybe that was a trick question. Perhaps you SEA now...? Ok that was bad. Let's do the last one.")
    
    # Question 5
q5 == input("Is Antartica at the North Pole or the South Pole?")
if q5.upper() == "South Pole":
# update my counter because they got the answer correct
    counter += 1    # shorthand for counter = counter + 1
else:   #INCORRECT
    print("That one was tricky, too. The Arctic is in the North. 'Ant' is the opposite of that so... you guessed it. The South Pole.")

    # Output the score
print("~ ~ ~ ~ ~ NOW A DRUM ROLLLL ~ ~ ~ ~ ~")
print(f"Your final score is: {counter}")

    # Give them feedback on their overall score
if counter == 5:
    print(f"See, {username} I knew you were a Geographer! Too easy.")
elif counter >=3 and counter < 5:
    print(f"You were playing with me at first, {username} but I knew you had it ;)")
elif counter >=2 and counter < 3:
    print(f"Eh, I bet you remembered the answer the moment you got one wrong though. Keep it up, {username}!")
elif counter <= 1:
    print(f"Maybe you don't like Geography or you really like pulling my leg. That's okay! Thanks for playing anyway {username}! :D gg")

        
