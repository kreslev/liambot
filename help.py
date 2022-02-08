#This is a repository of messages.

#Message sent to private messages
def helpMessage():
    message = "I have pinged the admins to let them know you need some help." \
        "\nHere are some emergency numbers in case you need them.\n" \
        "112 is the Police\n115 is the Fire Department\n" \
        "Professor Holt's number is 423-244-5019\n"
    return message

#Unused server message
def serverMessage(name):
    return name + " has requested help from @Jotsam"

#About message
def aboutMessage():
    message = "I am a bot created by Kreslev and T34p075 to create a safety system."\
        "You can get help by including help, sos, or 911 in a message."
    return message

#Pings the bot.
def rollcall(name):
    message = "I am here " + name + ". Always watching... always waiting..."
    return message