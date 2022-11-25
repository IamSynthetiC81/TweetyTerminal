import app as uut

Path = "tweetdhead300000.json"

tweets = list


def test_loadTweets(path) -> None:
    assert len(tweets) != 0, "Should not be empty"
    assert len(tweets) == 299999, "length must be 299999"
    assert str(tweets[0]['text']) == "If mitt romney say he gunna legalize weed then obama is fucked"
    assert str(tweets[1]['text']) == "@SuePalmers As a youth who has lived abroad, I share the President's feelings. It changes how you view foreign relations quite a bit."
    assert str(tweets[3]['text']) == "Can we please stop pretending that Obama is a good man? He is not. Today proved that. Being a good father alone does not make you a good man"


def test_update_tweet():
    for i in range(len(tweets)):
        string = "Tweet " + str(i)

        uut.updateTweet(int(i), string, tweets)

        assert (str(tweets[int(i)]['text']) == string)


def test_create_tweet():
    tweet_texts = ["I like big butts an´ I can not lie.",
                   "You otha brothas can´t deny.",
                   "That when a girl walks in wit´ a itty bitty waist an´",
                   "A round thing in yo´ face. You get SPRUNG.",
                   "Want to pull up tough, cuz you notice that butt was STUFFED.",
                   "Deep in the jeans she has wearin´.",
                   "I am hooked an´ I cannot stop starin´.",
                   "Oh baby, I want to get wit´ ya,",
                   "And so on, and on, and on ..."
                   ]

    for text in tweet_texts:
        uut.createTweet(text)
        assert uut.tweetArray[uut.TweetsSize - 1]['text'] == text


def test_save_to_disk():
    for i in range(uut.TweetsSize):
        uut.updateTweet(i, "Tweet " + str(i))

    uut.saveToDisk()
    tweets2 = uut.loadTweets()

    for i in range(uut.TweetsSize):
        assert tweets2[i] == uut.tweetArray[i]['text']


def test_delete_tweet():
    tweets2 = list.copy(uut.tweetArray)

    assert tweets2[0]['text'] == uut.tweetArray[0]['text']

    for i in range(1,uut.TweetsSize):
        uut.deleteTweet(0)
        assert tweets2[i]['text'] == uut.tweetArray[0]['text']



if __name__ == "__main__":
    tweets = uut.loadTweets(Path)

    test_loadTweets(Path)
    test_update_tweet()
    test_create_tweet()
    test_delete_tweet()
