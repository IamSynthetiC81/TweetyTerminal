# README for Testing

## Tests

The tests we produced test each function and its core functionality:
- `test_loadTweets()`
- `test_update_tweet()`
- `test_create_tweet()`
- `test_save_to_disk()`
- `test_delete_tweet()`

### SetUp()

We load the data into an array that each test used. This acts as a reset between each test.

### Test_loadTweets()

For this function we assert that all tweets have been loaded, and whether they have been loaded correctly

### test_update_tweet()

We replace each tweets text with the string `Tweet + {index}` and we assert that those changes reflect into the array.

### test_create_tweet()

We create some new tweets and assert that they have been added corectly into the array.

### test_save_to_disk()

We update each tweet with the string `Tweet + {index}` and save it into the disk. We then load the file into another array and assert each tweet has come through correctly.

### test_delete_tweet()
	We keep deleting the first tweet and assert the next one took its place aswell as that the list size was decremented correctly.