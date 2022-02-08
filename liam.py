import random

#This files handles misc bot commands.

#An array of Liam Neeson quotes to return.
def quote(name):
    
    #Long quotes
    q1 = "I don't know who you are. I don't know what you want. If "\
            "you're looking for ransom, I can tell you I don't have money... but what I do have are"\
            " a very particular set of skills. Skills I have acquired over a very long career. Skills"\
            " that make me a nightmare for people like you. If you let my daughter go now, that will be"\
            " the end of it - I will not look for you, I will not pursue you... but if you don't, I will"\
            " look for you, I will find you... and I will kill you."
    q2 = "When I was young, just your age, I was very poor, I was starving. One day, I stood in front of the window. "\
        "A window full of bread, there was just glass between me... and not being hungry anymore, it was so easy. So I broke "\
        "it and took what I wanted. Then they caught me and put me in chains for almost 19 years. They did things to me... "\
        "and I did things, there in jail. Terrible things. I became an animal. They took my dignity, they took everything from me."

    #Cutsom name quotes
    q3 = "You've been a good apprentice, " + name + ", and you're a much wiser man than I am. I foresee you will become a great Jedi Knight."
    q4 = "We need " + name + " and we need Leo, and we need them now."
    q5 = "I'm not testing you, " + name + ". Life tests you! Every day it brings you new chances for triumph or defeat. And if you pass the test, it doesn't make you a Jedi. It makes you human."
    q6 = "You must own the rain, " + name + ". It must be part of you, an extension of you. If you fight it, it will win."
    q7 = "Next time, " + name + ", we won't play by their rules. We'll invent our own!"
    q8 = "Do not cite the Deep Magic to me, " + name + ". I was there when it was written."
    q9 = "Just because I'm not behind bars doesn't mean I'm not paying for what I did, " + name + "."
    q10 = "Do you know what it feels like to become insane, " + name +"? It's like a war between being told who you are and knowing who you are. Which do you think wins?"
    q11 = "This is right, " + name + ". I stole something, I did. I stole happiness with you. I don't mind paying."
    q12 = "If it's a boy, call him Robert. If a lass, name her after my love, " + name + "."
    q13 = "What passes for honor with me is likely the same as what passes with " + name + ". When my word is given, it is good."

    #Array to store all quotes
    quotes = ["Always remember: the universe has a way of leading you to where you're supposed to be, at the moment you're supposed to be there.",
        "Your anger gives you great power. But if you let it, it will destroy you. As it almost did me.",
        "I gave myself up. I couldn't take wondering when someone was gonna come through the bedroom door.",
        "Give me a minute, I'm good. Give me an hour, I'm great. Give me six months, I'm unbeatable.",
        "Tell her that you love her. You've got nothing to lose and you'll always regret it if you don't.",
        "Don't be such a pessimist.", "My first priority is my daughter.", "No prison in the world is airtight.",
        "I have... acquired a pod in a game of chance. The fastest ever built.", "War is murder! Sheer, bloody murder!",
        "What is it about the dark? What secret does it hold?", "I want peace and quiet. I want it so much I'd die for it.",
        "All men with honor are kings. But not all kings have honor.", "The doctors say my heart sounds like a cement mixer.",
        "There's always a bigger fish.", "The ability to speak does not make you intelligent.", "Always mind your surroundings."
        "You traveled the world... Now you must journey inwards... to what you really fear... it's inside you... there is no turning back.",
        "You must become more than just a man in the mind of your opponent.", "I order you to forgive yourself.",
        "I don't subscribe to coincidence. I believe that no matter how random things might appear, there's still a plan.",
        "If the Witch knew the true meaning of sacrifice, she might have interpreted the deep magic differently. That when a willing victim who has "\
        "committed no treachery, is killed in a traitor's stead, the stone table will crack, and even death itself would turn backwards.",
        "You've got nothin' to lose, and you'll always regret it if you don't!", "My only conclusion... is that it was a Sith lord.",
        "For God's sake, Ringo Starr married a Bond girl!", "You've kept us waiting 700 years. You can have your seven minutes.",
        "When you drive the same road day after day, it's easy to think about the road not taken. I was lucky, I picked a good road early and I stayed on it.",
        "I love it when a plan comes together.", "I wanted a better life for you than the one I chose for myself.",
        "I do favors for people, and in return, they give me gifts. So, what can I do for you?",
        "All you have to know is I'm innocent. Give me two days, I can prove it. I can find out who did it.",
        "For a moment they had me convinced that I was crazy.", "The Queen does not need to know.", "Overkill is underrated.",
        "When a dog has a bone, the last thing you want to do is try and take it from him.", "No quarter will be asked.",
        "Give us the future, we've had enough of your past. Give us back our country, to live in, to grow in, to love.",
        "When you're better, I'll find work for you.", "That's because it's impossible to measure love. And, as you know, without measurements there can be no science.",
        "How about this? How about if I go along? You won't even know I'm there. I'm very good at being invisible.",
        "I see marriage as a life-time partnership between equals.", "Honor is what no man can give you and none can take away. Honor is a man's gift to himself.",
        "We have a weapon more powerful... than any in the whole arsenal of the British Empire! That weapon... is our refusal!",
        "Power is when we have every justification to kill, and we don't.",
        "Sometimes, people move into town to start a new slate, you might be doing more harm than good by prying into their private lives.",
        "The general wisdom is that, in the end, there isn't just one person for each of us.", "I'm learning to live with a lot of things.",
        "Things never happen the same way twice, dear one.", "I found out more in two hours than you did in two weeks. I know who killed Gerald.",
        "Listen. You listen to me. I am trying to help people. My field of study is the science of fear, I try to understand why people act the way they act, why they feel the way they feel.",
        "I told you, it wasn't meant to be like this.", "If you make yourself more than just a man, if you devote yourself to an ideal, and if they can't stop you, then you become something else entirely.",
        "I hate them for making hatred necessary, and I'll do what I can to end it.", "It's like... there's no one else in the world. Like she doesn't need anybody. Can you live your whole life that way, or does it drive you crazy in the end?",
        q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13]

    #Returns quote
    return random.choice(quotes)

#Handles the unit conversion
def convert(message):
    
    #Breaks command into array
    toCon = messageFormat(message)
    
    #Returns error is array isn't the right length
    if len(toCon) != 2:
        return "To convert, type !convert and then an amount and unit. A space is needed between" \
            "the unit and amount.\n**For Example**\n!convert 2 feet"
    
    #Sets up error message
    sender = "I'm sorry. I need a space between the number and unit. "
    sender += "I can do miles, inches, feet, and gallons in freedom units; "
    sender += " liters, cm, m, and km in metric; and fahrenheit and celcius conversion."

    #Returns error is first command isn't a number
    if not toCon[0].isnumeric() and not isFloat(toCon[0]):
        return sender
    
    #Sets amount.
    amount = toCon[0]

    #Sets unit string to lowercase
    toCon[1] = toCon[1].lower()
    
    #Converts feet to meters
    if toCon[1] == "feet" or toCon[1] == "ft":
        return amount + " feet is " + multiCon(amount, 0.3048, True) + " meters."
    
    #Converts meters to feet
    elif toCon[1] == "meter" or toCon[1] == "m" or toCon[1] == "meters":
        return amount + " meters is " + multiCon(amount, 0.3048, False) + " feet."
    
    #Converts gallons to liters
    elif toCon[1] == "gallon" or toCon[1] == "gal" or toCon[1] == "gallons":
        return amount + " gallons is " + multiCon(amount, 3.785412, True) + " liters."
    
    #Converts liters to gallons
    elif toCon[1] == "liter" or toCon[1] == "l" or toCon[1] == "liters":
        return amount + " liters is " + multiCon(amount, 3.785412, False) + " gallons."
    
    #Converts cm to inches
    elif toCon[1] == "cm" or toCon[1] == "centimeter" or toCon[1] == "centimeters":
        return amount + " centimeters is " + multiCon(amount, 0.3937, False) + " inches."
    
    #Converts inches to cm
    elif toCon[1] == "in" or toCon[1] == "inches" or toCon[1] == "inch":
        return amount + " inches is " + multiCon(amount, 0.3937, True) + " centimeters."
    
    #Converts miles to km
    elif toCon[1] == "miles" or toCon[1] == "mile":
        return amount + " miles is " + multiCon(amount, 1.609344, True) + " kilometers."
    
    #Converts km to miles
    elif toCon[1] == "kilometers" or toCon[1] == "km" or toCon[1] == "kilometer":
        return amount + " kilometers is " + multiCon(amount, 1.609344, False) + " miles."

    #Converts C to F
    elif toCon[1] == "celcius" or toCon[1] == "c":
        return amount + " celcius is " + convertC(amount) + " fahrenheit."

    #Converts F to C
    elif toCon[1] == "fahrenheit" or toCon[1] == "f":
        return amount + " fahrenheit is " + convertF(amount) + " celcius."
    else:
        return sender
    
#This converts numbers and such.
def multiCon(amount, conRate, multi):
    if multi:
        return str(round((float(amount) * conRate),2))
    else:
        return str(round((float(amount) / conRate),2))

#This is a specialized section for converting temp.
def convertC(amount):
    return str(round((float(amount) * (9/5)) + 32))
def convertF(amount):
    return str(round(((float(amount) - 32) * (5/9)), 2))

#Splits a message into an array.
def messageFormat(message):
    message = message.lower()
    command = message.split()
    command.pop(0)
    return command

#Returns true if number is a float. False if not.
def isFloat(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False