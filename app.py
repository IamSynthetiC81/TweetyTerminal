import json
import random
import sys
from datetime import datetime

# Global Path Variable
Path = "tweetdhead300000.json"

# Profiling : Save length of tweets on buffer instead of calling len().
TweetsSize = int(0)

def loadTweets(path=Path) -> list:
    """
    Load tweets from the specified path and return them
    :param path: Path to the json file containing the tweets
    :return:  Returns a list of tweets
    """
    array = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                continue
            tweet = json.loads(line)
            array.append(tweet)
        f.close()

    global TweetsSize
    TweetsSize = len(array)

    return array


tweetArray = loadTweets()               # Global Variable containing tweets


def deleteTweet(idx, tweets=None) -> None:
    """
    Delete the tweet in the specified index
    :param idx: Index of the tweet to be deleted
    :param tweets: List of tweets. By default, '~tweetArray' is used.
    """
    if tweets is None:
        tweets = tweetArray
    del tweets[idx]

    # Profiling : Decrement length.
    global TweetsSize
    TweetsSize -= 1


def readTweet(idx, tweets=None) -> None:
    """
    Prints out the tweet at the specified index.
    :param idx: Index of the tweet
    :param tweets: List of tweets. By default, '~tweetArray' is used.
    """
    if tweets is None:
        tweets = tweetArray

    print("Tweet at index " + str(idx) + ": " + str(tweets[idx]['text']) + " created at: " + str(
        tweets[idx]['created_at']))


def createTweet(string=None, tweets=None) -> None:
    """
    Creates a new tweet and appends it to the list
    :param string: Text of the new tweet. Can be ignored for console input
    :param tweets: List of tweets. By default, '~tweetArray' is used.
    """
    if tweets is None:
        tweets = tweetArray

    date = datetime.now()
    date = str(date)

    if string is None:
        string = input("Please type your tweet:\n")

    tweet = {'text': string, 'created_at': date}
    tweets.append(tweet)

    global TweetsSize
    TweetsSize += 1


def updateTweet(current, text, tweets=None) -> None:
    """
    Updates the indexed tweet with the specified text.
    :param current: Index of the tweet to be altered.
    :param text: String to be placed into the tweet
    :param tweets: List of tweets. By default, '~tweetArray' is used.
    """
    if tweets is None:
        tweets = tweetArray

    date = datetime.now()
    date = str(date)
    tweet = {'text': text, 'created_at': date}

    tweets[current] = tweet


def saveToDisk(path="output.json", tweets=None) -> None:
    """
    Saves the specified list of tweets into the specified path
    :param path: Name and path of the file to be created or saved on.
    :param tweets: List of tweets. By default, '~tweetArray' is used.
    """
    if tweets is None:
        tweets = tweetArray

    with open(path, "w") as f:
        final = ""
        for i in tweets:
            tweet = json.dumps(i)
            final = final + "\n" + tweet
        f.write(final)
    f.close()


def game(tweets) -> None:
    """
    Prints a random tweet from the list
    :param tweets: List of tweets. By default, '~tweetArray' is used.
    """
    random.seed(datetime.now())
    idx = random.randrange(0, TweetsSize - 1)
    print(tweets[idx]['text'])


def printHelp() -> None :
    """
    Helper function to print the menu
    """
    print(
        "======================================================\nc: Create new tweet\nr <tweet ID>: Read tweet with "
        "specified ID\nu <tweet ID>: Update tweet with specified ID\nd: Delete current tweet\ng: Display random tweet "
        "for the lulz\n$: Read last tweet\n-: Read one tweet down\n+: Read one tweet down\n=: Print current tweet\nq: "
        "Quit\nw: Save to disk\nx: Exit and save\n======================================================")


def terminalUI():
    current = 0
    print("Welcome to the US political degeneracy cesspool(Twitter)\nType h for help...")
    quit = False
    a = ' '
    while not quit:
        a = input("--->")
        a = str(a)
        a = a.strip()
        a = a.split(" ")
        quit, current = menu(current, tweetArray, a)


def menu(current, tweets, a):
    if a[0] == "d":  # Delete tweet
        deleteTweet(current, tweets)

    elif a[0] == "h":  # Display Help (man sex)
        printHelp()

    elif a[0] == "g":  # Display random tweet
        game(tweets)

    elif a[0] == "q":  # Quit
        return True, current

    elif a[0] == "w":  # Save To disk
        saveToDisk(tweets)

    elif a[0] == "x":  # Exit and Save
        saveToDisk(tweets)
        return True, current

    elif a[0] == "i":  # ???
        # TODO : Fix this
        print(len(tweets))

    elif a[0] == "=":  # Print Current Tweet
        print("Current index: " + str(current))
        #TODO : Fix this

    elif a[0] == "$":  # Print Last Tweet
        current = TweetsSize - 1
        readTweet(current, tweets)

    elif a[0] == "-":  # Print Previous Tweet
        if current == 0:
            print("You've reached the bottom")
            return False, current
        current -= 1
        readTweet(current, tweets)

    elif a[0] == "+":  # Print Next Tweet
        if current == len(tweets) - 1:
            print("You've reached the top")
            return False, current
        current += 1
        readTweet(current, tweets)

    elif a[0] == "c":  # Create a new Tweet
        createTweet()
        current = TweetsSize - 1

    elif a[0] == "r":  # Read Tweet with specified ID
        try:
            a[1] = int(a[1])
        except:
            print("Incorrect arguments")
            return False, current

        if a[1] < 0 or a[1] > TweetsSize:
            print("Index out of range")

        else:
            current = a[1]
            readTweet(current, tweets)

    elif a[0] == "u":  # Update Tweet with specified ID
        try:
            a[1] = int(a[1])
        except:
            print("Incorrect arguments")
            return False, current

        if a[1] < 0 or a[1] > TweetsSize:
            print("Index out of range")

        else:
            current = a[1]
            updateTweet(current, input("Please type your tweet:\n"))

    else:
        print("Command not recognised...")  # Wrong command nerd
    return False, current


def main(argv):
    terminalUI()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
