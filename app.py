import flask
import os
import random
import requests
import json
import requests_oauthlib

app = flask.Flask(__name__)

quote="default quote"
imageurl="https://puu.sh/tQ7MF/a670d86ef7.png"


@app.route('/')
def index():
    
    #GETTY IMAGES API REQUEST

    url = "https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&minimum_size=xx_large&phrase=potato"
    my_headers = {"Api-Key": "p8tv85a2dut7fa3vw6juh9fm"}
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    imageurl = json_body["images"][random.randint(0,15)]["display_sizes"][0]["uri"]


    #TWITTER QUOTE API REQUEST
    url = "https://api.twitter.com/1.1/search/tweets.json?q=potato&src=typd"
    oauth = requests_oauthlib.OAuth1(
        #API_Key
        "HmAQZ9EBVNJxPY7Ix9tgyEdGl", 
        #Api_secret
        "kV4m5MQdXLIepcMXtDihkVdidpezTVC9ICS4A2uOIieXzpB272",
        #Access_token
        "774699185442398208-HnzGYRAnayy1fkg2j46rHMVUHK23M97",
        #Access_secret
        "g62tViAWZzMMsk2NOCu0Y2qnUaf07Tojmb6PEphjq0uLR"
    )
    response = requests.get(url, auth=oauth)
    json_body = response.json()
    a = random.randint(0,14)
    quote = json_body["statuses"][a]["text"]
    author = json_body["statuses"][a]["user"]["screen_name"]
    twitterid = str(json_body["statuses"][a]["id"])
    twitterlink = "https://twitter.com/" + author + "/status/" + twitterid 
    
    return flask.render_template("index.html", 
                                arg1=quote,
                                arg2=imageurl,
                                arg3=author,
                                arg4=twitterlink)
    
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0')
)

#https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&sort_order=best&phrase=space
#p8tv85a2dut7fa3vw6juh9fm

#add json to requirements.txt
#add requests_oauthlib to requirements.txt