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

    url = "https://api.gettyimages.com:443/v3/search/images?age_of_people=newborn%2Cbaby&exclude_nudity=true&graphical_styles=photography&license_models=royaltyfree&minimum_size=xx_large&number_of_people=one%2Ctwo%2Cgroup&orientations=Horizontal&page_size=100"
    my_headers = {"Api-Key": os.getenv("gettyapikey")}
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    imageurl = json_body["images"][random.randint(0,99)]["display_sizes"][0]["uri"]


    #TWITTER QUOTE API REQUEST
    url = "https://api.twitter.com/1.1/search/tweets.json?q=from%3ArealDonaldTrump"
    
    oauth = requests_oauthlib.OAuth1(
        os.getenv("twitterapikey"),
        os.getenv("twitterapisecret"),
        os.getenv("twitteraccesstoken"),
        os.getenv("twitteraccesssecret")
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
