import json
import random
from datetime import datetime

def loadTweets(path):
    tweets=[]
    with open(path,"r") as f:
        lines = f.readlines()
        for line in lines:
            tweet = json.loads(line)
            tweets.append(tweet)
        f.close()
    return tweets

def deleteTweet(idx,tweets):
    del tweets[idx]

def readTweet(idx,tweets):
    print("Tweet at index "+str(idx)+": "+str(tweets[idx]['text'])+" created at: "+str(tweets[idx]['created_at']))

def createTweet(current,tweets):
    updateTweet(len(tweets),tweets)

def updateTweet(current,tweets):
    date = datetime.now()
    date = str(date)
    text = input("Please type your tweet:\n")
    tweet = {'text':text,'created_at':date}
    tweets.insert(current,tweet)

def saveToDisk(tweets):
    with open("output.json","w") as f:
        tweet = ""
        final = ""
        for i in tweets:
            tweet = json.dumps(i)
            final =final+"\n"+tweet
        f.write(final)
    f.close()

def game(tweets):
    random.seed(datetime.now())
    idx = random.randrange(0,len(tweets)-1)
    print(tweets[idx]['text']) 

def printHelp():
    print("======================================================\nc: Create new tweet\nr <tweet ID>: Read tweet with specified ID\nu <tweet ID>: Update tweet with specified ID\nd: Delete current tweet\ng: Display random tweet for the lulz\n$: Read last tweet\n-: Read one tweet down\n+: Read one tweet down\n=: Print current tweet\nq: Quit\nw: Save to disk\nx: Exit and save\n======================================================")

def terminalUI():
    current = 0
    tweets = loadTweets("input.json")
    print("Welcome to the US political degeneracy cesspool(Twitter)\nType h for help...")
    quit = False 
    a=' '
    while quit==False:
        a=input("--->")
        a = str(a)
        a = a.strip()
        a = a.split(" ")
        quit ,current = menu(current,tweets,a)

def menu(current,tweets,a):

        if a[0] == "d":
            deleteTweet(current,tweets)

        elif a[0] == "h":
            printHelp()

        elif a[0] == "g":
            game(tweets,)

        elif a[0] == "q":
            return True, current
        
        elif a[0] == "w":
            saveToDisk(tweets)

        elif a[0] == "x":
            saveToDisk(tweets)
            return True, current

        elif a[0] == "i":
            print(len(tweets))

        elif a[0] == "=":
            print("Current index: "+str(current))

        elif a[0] == "$":
            current = len(tweets)-1
            readTweet(current,tweets)

        elif a[0] == "-":
            if current==0:
                print("You've reached the top")
                return False, current 
            current-=1
            readTweet(current,tweets)

        elif a[0] == "+":
            if current==len(tweets)-1:
                print("You've reached the bottom")
                return False, current
            current+=1
            readTweet(current,tweets)

        elif a[0] == "c":
            createTweet(current,tweets)
            current = len(tweets)-1

        elif a[0] == "r":   
            try:
                a[1] = int(a[1])
            except:
                print("Incorrect arguments")
                return False, current

            if a[1]<0 or a[1]>len(tweets):
                print("Index out of range")

            else:
                current = a[1]
                readTweet(current,tweets)

        elif a[0] == "u":   
            try:
                a[1] = int(a[1])
            except:
                print("Incorrect arguments")
                return False,current

            if a[1]<0 or a[1]>len(tweets):
                print("Index out of range")

            else:
                current = a[1]
                updateTweet(current,tweets)

        else:
            print("Command not recognised...")
        return False, current

        


def main(argv):
    terminalUI()


if __name__ == "__main__":
    main(sys.argv[1:])