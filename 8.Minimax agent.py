print("Welcome to MoodMate!")
print("Your friendly mood chatbot")
print("Type 'bye' to exit")

while True:
    msg = input("\nYou: ").lower()
    words = msg.split()

    if "hello" in words or "hi" in words or "hey" in words:
        print("Bot: Hey! Great to see you. How is your day going?")

    elif "happy" in words or "excited" in words:
        print("Bot: That's amazing! Keep spreading those positive vibes!")

    elif "sad" in words or "upset" in words:
        print("Bot: It's okay to have bad days. Take a deep breath!")

    elif "bored" in words:
        print("Bot: Try listening to music, learning something new, or taking a walk!")

    elif "exam" in words or "study" in words:
        print("Bot: Focus on one topic at a time. You can do it!")

    elif "joke" in words:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "motivate" in words:
        print("Bot: Small progress every day leads to big achievements!")

    elif "name" in words:
        print("Bot: I am MoodMate, your mini mood companion!")

    elif "bye" in words:
        print("Bot: Goodbye! Take care and stay awesome!")
        break

    else:
        print("Bot: Interesting! Tell me more about it.")