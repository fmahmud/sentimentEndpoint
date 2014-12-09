from flask import Flask
from flask import request
from textblob import TextBlob

app = Flask(__name__)

inverse_homomorphism = { 		\
	"__question__"	: "?",		\
	"__hashtag__"	: "#",		\
	"__at__"		: "@",		\
	"__dot__"		: ".",		\
	"__semi__"		: ";",		\
	"__new_line__"	: "\n",		\
}

@app.route('/')
def hello_world():
	return 'Sentiment API'

@app.route('/tweet/')
def test_page():
	tweet = request.args.get("item")
	for k, v in inverse_homomorphism.iteritems() :
		tweet = tweet.replace(k, v)
	tweet = tweet.replace("_", " ")
	blob = TextBlob(tweet)
	return str(blob.sentiment.polarity)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
