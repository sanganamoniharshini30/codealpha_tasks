user = input("You: ").lower().split(",")

for i in user:
    i = i.strip()   # removes extra spaces

    if i == "hello":
        print("Bot: Hi!", end="")

    elif i == "how are you":
        print("Bot: I'm Fine, Thanks!",end="")

    elif i == "bye":
        print("Bot: Goodbye!",end="")

    else:
        print("Bot: I don't understand",end="")