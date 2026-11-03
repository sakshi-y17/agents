print("Welcome to MoodMate!")
print("Your friendly mood chatbot")
print("Type 'bye' to exit")

while True:
    msg = input("\nYou: ").lower()

    if "hello" in msg or "hi" in msg:
        print("Bot: Hey! Great to see you. How is your day going?")

    elif "happy" in msg or "excited" in msg:
        print("Bot: That's amazing! Keep spreading those positive vibes!")

    elif "sad" in msg or "upset" in msg:
        print("Bot: It's okay to have bad days. Take a deep breath!")

    elif "bored" in msg:
        print("Bot: Try listening to music, learning something new, or taking a walk!")

    elif "exam" in msg or "study" in msg:
        print("Bot: Focus on one topic at a time. You can do it!")

    elif "joke" in msg:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "motivate" in msg:
        print("Bot: Small progress every day leads to big achievements!")

    elif "your name" in msg:
        print("Bot: I am MoodMate, your mini mood companion!")

    elif "bye" in msg:
        print("Bot: Goodbye! Take care and stay awesome!")
        break

    else:
        print("Bot: Interesting! Tell me more about it.")