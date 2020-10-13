# Bob answers 'Sure.' if you ask him a question.
#
# He answers 'Whoa, chill out!' if you yell at him.
#
# He says 'Fine. Be that way!' if you address him without actually saying
# anything.
#
# He answers 'Whatever.' to anything else.

def hey(message):
    message = message.rstrip()
    if message.endswith("?") and not message.isupper():
        return "Sure."
    elif message.isupper():
        return "Whoa, chill out!"
    elif not message or message.isspace():
        return "Fine. Be that way!"
    else:
        return "Whatever."


