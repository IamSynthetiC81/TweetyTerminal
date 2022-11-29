import json
import random
from datetime import datetime

import logging
import sys

#START OF LOGGING
logger = logging.getLogger("Log_Information")
#Required whole pathing for the file to work (CHANGE)
logging.basicConfig(filename='C:\\Users\\Helioc\\Desktop\\Sxoli\\ERGALEIA\\TweetyTerminal-main\\logme.txt', filemode='w', format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, force= True)
#END OF LOGGING

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
    #Required whole pathing for the file to work (CHANGE)
    with open("C:\\Users\\Helioc\\Desktop\\Sxoli\\ERGALEIA\\TweetyTerminal-main\\output.json","w") as f:
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
    #Required whole pathing for the file to work (CHANGE)
    tweets = loadTweets("C:\\Users\\Helioc\\Desktop\\Sxoli\\ERGALEIA\\TweetyTerminal-main\\input.json")
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
            logger.info("User deleted a tweet. (d)")
            deleteTweet(current,tweets)

        elif a[0] == "h":
            logger.info("User asked for help. (h)")
            printHelp()

        elif a[0] == "g":
            logger.info("User played a game with random tweets. (g)")
            game(tweets,)

        elif a[0] == "q":
            logger.info("User quit Twitter Editor without save. (q)")    
            return True, current
                   
        elif a[0] == "w":
            logger.info("User overwrited tweet to disk. (w)") 
            saveToDisk(tweets)
            

        elif a[0] == "x":
            logger.info("User exited Twitter Editor with save. (x)") 
            saveToDisk(tweets)           
            return True, current

        elif a[0] == "i":
            logger.info("User printed the tweet list. (i)") 
            print(len(tweets))

        elif a[0] == "=":
            logger.info("User printed current tweet ID. (=)") 
            print("Current index: "+str(current))

        elif a[0] == "$":
            logger.info("User read the last tweet in the file. ($)")
            current = len(tweets)-1
            readTweet(current,tweets)
            

        elif a[0] == "-":
            if current==0:
                print("You've reached the top")
                return False, current 
            current-=1
            logger.info("User read one tweet up from their current tweet. (-)") 
            readTweet(current,tweets)
            

        elif a[0] == "+":
            if current==len(tweets)-1:
                print("You've reached the bottom")
                return False, current
            current+=1
            logger.info("User read one tweet down from their current tweet. (+)") 
            readTweet(current,tweets)
            

        elif a[0] == "c":
            logger.info("User created a tweet. (c)") 
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
                logger.info("User read a tweet. (r)") 
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
                logger.info("User updated a tweet. (u)") 
                updateTweet(current,tweets)
                

        else:
            logger.info("User tried an unrecognised command...") 
            print("Command not recognised...")
        return False, current
    

def main(argv): 

    terminalUI()


if __name__ == "__main__":
    main(sys.argv[1:])
