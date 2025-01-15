#Write a program that asks user to enter jokes category and display joke accordingly
name = input("Please enter your name: ")

# Provide a list of options and answers from which the user will have to select from
print("Please select Jokes Category")
jokes_category = {"1": "Funny", "2": "Emotional"}
#print(jokes_catgory)
for key, value in jokes_category.items():
    print(f"{key}: {value}")

choice = input("Please enter your joke Category in Number 1 OR 2: ")

if choice in jokes_category:
    print(f"You selected: {jokes_category[choice]}")
    if jokes_category[choice] == "Funny":
        print("Why was the math book sad? Because it had too many problems.")
    elif jokes_category[choice] == "Emotional":
        print("Why was the pillow crying? Because it was feeling down.")
else:
    print("Invalid Input!. Please try again")
