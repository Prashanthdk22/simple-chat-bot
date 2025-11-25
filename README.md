# simple-chat-bot
I created a simple rule-based chatbot using Python.
It works by taking the user’s input and comparing it with different conditions using if-elif-else statements.
Based on what the user types, the chatbot gives a matching reply.

Step-by-step explanation

I first import the datetime module
This allows the chatbot to show the real time and date.

The program asks the user to enter their name
I store it in a variable so the chatbot can talk personally to the user.

I print a welcome message
This tells the user that they can type “bye” to exit.

The chatbot runs inside a while True loop
This loop makes the chatbot keep asking for input until the user types “bye”.

I convert every user input to lowercase
This helps match the inputs easily, without worrying about uppercase letters.

I use multiple elif conditions
Each condition checks for a group of keywords like:

greetings (hi, hello, hey)

morning / evening messages

how are you

feeling responses (good, sad)

identity questions

jokes

motivation

time and date

small talk like “what are you doing”

thanks

If any condition matches, the chatbot prints the correct reply.

Real time & date
When the user asks for time or date, I use the datetime module to display the current system time and today’s date.

Exit condition
If the user types “bye”, the chatbot prints a goodbye message and exits the loop using break.

Default response
If the input doesn’t match any condition, the chatbot says:
“Sorry, I didn’t understand that.”

Final Summary
My chatbot is a simple, interactive Python program that uses if-else logic to respond to user messages. It can greet, joke, motivate, show real time and date, handle small talk, and exit politely. It behaves like a very basic assistant created using only conditional statements.
