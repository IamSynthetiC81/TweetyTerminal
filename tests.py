import app as uut
import unittest


class test_app_class(unittest.TestCase):

    Path = "tweetdhead300000.json"          # Local Path Variable
    tweets = list                           # Local Tweets Array

    def setUp(self) -> None:
        """
        For each test we read, and load the data from the file. This
        counts as a reset.
        """
        uut.tweetArray = uut.loadTweets(self.Path)
        self.tweets = uut.tweetArray

    def test_loadTweets(self) -> None:
        self.assertNotEqual(self.tweets, 0, "Should not be empty")
        self.assertEqual(len(self.tweets), 299999, "length must be 299999")
        self.assertEqual(str(self.tweets[0]['text']), "If mitt romney say he gunna legalize weed then obama is fucked")
        self.assertEqual(str(self.tweets[1]['text']), "@SuePalmers As a youth who has lived abroad, I share the President's feelings. It changes how you view foreign relations quite a bit.")
        self.assertEqual(str(self.tweets[3]['text']), "Can we please stop pretending that Obama is a good man? He is not. Today proved that. Being a good father alone does not make you a good man")

    def test_update_tweet(self):
        for i,tweet in enumerate(self.tweets):
            string = "Tweet " + str(i)

            uut.updateTweet(int(i), string, self.tweets)

            self.assertNotEqual(string, tweet['text'])
            self.assertEqual (str(self.tweets[int(i)]['text']), string)

    def test_create_tweet(self):
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
            self.assertEqual(uut.tweetArray[uut.TweetsSize - 1]['text'], text)

    def test_save_to_disk(self):
        for i in range(uut.TweetsSize):
            uut.updateTweet(i, "Tweet " + str(i))

        uut.saveToDisk()

        tweets2 = uut.loadTweets("output.json")

        for i in range(uut.TweetsSize):
            self.assertEqual(tweets2[i]['text'], uut.tweetArray[i]['text'])

    def test_delete_tweet(self):
        tweets2 = list.copy(uut.tweetArray)

        self.assertEqual(tweets2[0]['text'], uut.tweetArray[0]['text'])

        for i in range(1, uut.TweetsSize):
            uut.deleteTweet(0)
            self.assertEqual(tweets2[i]['text'], uut.tweetArray[0]['text'])


if __name__ == "__main__":
    unittest.main()

