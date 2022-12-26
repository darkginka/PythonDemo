from pymongo import MongoClient
import pandas as pd
from flask import Flask,request
from flask_cors import CORS
import pandas as pd

CONNECTION_STRING ="mongodb+srv://rohanthakur:NXEaPckQIKO39QaT@testcluster.4aecceu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
mydb=client.Teachable                     
mycontent=mydb.master_table
myusers=mydb.webinar_users
mycurrentwebinar = mydb.event_reg

df_mycontent = pd.DataFrame(list(mycontent.find()))
df_mycontent.to_csv('mycontent.csv')

df_myusers = pd.DataFrame(list(myusers.find()))
df_myusers.to_csv('myusers.csv')

app = Flask(__name__)
CORS(app)

"""run in cmd"""
# $env:FLASK_APP = "apitest.py"
# flask run --host=192.168.0.114
#C:\Users\ADMIN\AppData\Local\Programs\Python\Python38

####### dataset #######
videoLink = pd.read_csv("Content Segregation_Web Page_Videos.csv",encoding='unicode_escape')

####### Methods #######
def get_video(video_name):
	if(video_name not in list(videoLink["ContentName"])):
		return False
	else:
		return videoLink[videoLink.video==video_name]["ContentName"].values[0]

####### API Call #######
@app.route("/test",methods=["GET"])
def get_name():
  return "Rohan"

####### All Content list#######
@app.route("/videos",methods=["GET"])
def get_videos():
  abc ={}
  list_of_video = videoLink['ContentName'].to_list()
  for i in range(0,len(list_of_video)):
    abc[i]=list_of_video[i]
  xyz={"All Content Name":abc}
  return xyz


####### search via content #######
@app.route("/search",methods=["POST"])
def search():
  contentName = request.form['ContentName']
  new_videoDF=videoLink[videoLink["ContentName"]==contentName]
  list_of_video = new_videoDF['VideoLinks'].to_list()
  xyz={"Search Video":list_of_video}
  return xyz


#######search via category #######
@app.route("/multisearch",methods=["POST"])
def multisearch():
  subject = request.form['Subject']
  area = request.form['Area']
  level = request.form['Level']
  new_DF = videoLink[videoLink["Subject"]==subject and videoLink["Area"]==area and videoLink["Level"]==level]
  list_of_video = new_DF['VideoLinks'].to_list()
  xyz={"Search Video":list_of_video}
  return xyz
