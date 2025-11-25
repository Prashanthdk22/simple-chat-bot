import datetime
name = input("Enter your name : ")

print(f"Hello!! {name} i'm your simple rule based chat bot ")
print("type bye to exit ")

while True:
    user = input("you : ").lower()

    if user == "bye":
        print(f"Exiting from chat box!!! \n Have a nice day {name}")  
        break
    elif user in ["hi" ,"hello","hey"]:
        print(f"Hello {name} how are you ")
    elif user in ["good morning","morning","gm"]:
        print(f"Very good morning {name} have a nice day")
    elif user in ["good evening","evening"]:
        print(f"Good evening {name} \n how was your day")
    elif user in ["how are you","how r u","sup"]:
        print(f"I'm good happy to chat with you \n how are you")
    elif user in ["i am fine","i'm fine","good"]:
        print(f"Good to hear that {name}! \n What are you working on now")
    elif user in ["not good","sad"]:
        print(f"Ohh… what happened {name}?\n You can tell me—I’m here with you.")
    elif user in ["what is your name","your name"]:
        print(f"I'm your simple chat bot {name}")
    elif user in ["are you a robot","are you robot"]:
        print(f"no!! {name} \n i'm not a robot i am just a simple chat bot")
    elif user in ["who created you"]:
        print("Prashu created me")
    elif user in ["tell me a joke", "make me laugh"]:
        print("Why did the computer go to the doctor?\n Because it had a virus… and forgot to install antivirus")
    elif user in ["give me motivation","motivate me"]:
        print("You’re not stuck.\n You’re not slow.\n You’re building yourself.")
    elif user in ["date", "today date", "what is today"]:
        today_date = datetime.date.today().strftime("%d-%m-%Y")
        print(f"Today's date is {today_date}")
    elif user in ["time", "what is the time", "time now"]:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The current time is {current_time}")

    elif user in ["what are you doing","wyd"]:
        print("I’m here waiting to chat with you!")
    elif user in ["thanks","tq","thank you"]:
        print(f"I'm happy to help you {name}")

    else:
      print("Sorry, I didn’t understand that.")
