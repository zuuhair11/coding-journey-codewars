# Create a function which answers the question 'Are you playing banjo?'.
# If your name starts with the letter 'R' or lower case 'r', you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:

def are_you_playing_banjo(name):
    # Implement me!
    if name[0].lower() == 'r':
        return '{} plays banjo'.format(name)
    return f'{name} does not play banjo'


if __name__ == '__main__':
    print(are_you_playing_banjo('martin'))  # martin does not play banjo
    print(are_you_playing_banjo('Rikke'))   # Rikke plays banjo
