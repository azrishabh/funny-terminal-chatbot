
import random
import time
import pyttsx3
from colorama import Fore, Style, init

init(autoreset=True)

engine = pyttsx3.init()
engine.setProperty("rate", 170)

personalities = {
    "funny": "😂 Silly and always joking",
    "roast": "🔥 Savage and roasting you",
    "nice":  "😊 Kind and wholesome",
}

current_personality = "funny"

def load_jokes():
    try:
        with open("jokes.txt", "r", encoding="utf-8") as f:
            return f.read().split("\n")
    except:
        return ["Why did the cookie go to the hospital? Because it felt crumby!"]

jokes = load_jokes()
chat_memory = []

def get_response(personality):
    funny_lines = [
        "Bro, I'm laughing but I don't know why 😂",
        "I'm 99% sure that made no sense.",
        "Hold on… calculating… error 404 💀"
    ]

    roast_lines = [
        "That message lowered both our IQs 💀",
        "Bro, even Google can’t help you!",
        "You type like your keyboard is scared of you 🔥"
    ]

    nice_lines = [
        "Aww that’s sweet 😊",
        "I appreciate you 💛",
        "You're doing great today!"
    ]

    if personality == "funny":
        return random.choice(funny_lines)
    elif personality == "roast":
        return random.choice(roast_lines)
    else:
        return random.choice(nice_lines)

def speak(text):
    engine.say(text)
    engine.runAndWait()

print(Fore.CYAN + "🤖 FUNNY TERMINAL CHATBOT")
print(Fore.YELLOW + "Type 'exit' to quit, 'joke' for a joke, 'mode' to switch personality.\n")

while True:
    user = input(Fore.GREEN + "You: ")

    if user.lower() == "exit":
        goodbye = "Bye! Don't miss me too much 😎"
        print(Fore.MAGENTA + "Bot:", goodbye)
        speak(goodbye)
        break

    elif user.lower() == "joke":
        joke = random.choice(jokes)
        print(Fore.MAGENTA + "Bot 🤣:", joke)
        speak(joke)
        chat_memory.append(("You", user))
        chat_memory.append(("Bot", joke))
        continue

    elif user.lower() == "mode":
        print(Fore.YELLOW + "\nAvailable Modes:")
        for m in personalities:
            print(f" - {m}: {personalities[m]}")

        new_mode = input("\nChoose mode (funny/roast/nice): ").lower()

        if new_mode in personalities:
            current_personality = new_mode
            msg = f"Personality switched to {new_mode}! 🎭"
            print(Fore.CYAN + msg)
            speak(msg)
        else:
            print(Fore.RED + "Invalid mode!")

        continue

    bot_reply = get_response(current_personality)
    print(Fore.MAGENTA + "Bot:", bot_reply)
    speak(bot_reply)

    chat_memory.append(("You", user))
    chat_memory.append(("Bot", bot_reply))
