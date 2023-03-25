from flask import Flask,request
from pymongo import MongoClient

app = Flask(__name__)

CONNECTION_STRING ="mongodb+srv://rohanthakur:NXEaPckQIKO39QaT@testcluster.4aecceu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
mydb=client.Attendance                     
mycoll=mydb.webinar_users
mycurrentwebinar = mydb.event_reg

@app.route('/')
def useraddress():
    xyz={
    "address":mycoll["address"]
    }
    return xyz

@app.route("/signup",methods=["POST"])
def add_user():
  response ={}
  enterName = request.form['name']
  enterEmail = request.form['email']
  enterDOB = request.form['dob']
  enterPassword = request.form['password']
  enterMobile = request.form['mobile']
  enterGender = request.form['gender']
  enterState = request.form['state']
  enterDisctict = request.form['disctict']
  enterTaluka = request.form['taluka']
  enterPin = request.form['pin']

  x = mycoll.find_one({"email": enterEmail})

  if(x != None):
    response={
      "recored status":"You already registed please Login",
      "record":x["email"]
    }
    return response
  else:
    userinfo = {
      "name":enterName,
      "email":enterEmail,
      "dob":enterDOB,
      "mobile":{"$numberLong":enterMobile},
      "password":enterPassword,
      "address":{"state":enterState,"disctict":enterDisctict,"taluka":enterTaluka,"pin":enterPin},
      "gender":enterGender
      }
    mycoll.insert_one(userinfo)
    response={
      "recored status":"Instered Sucessfully",
      "record": enterEmail
    }
    return response
   

@app.route("/validate",methods=["POST"])
def validate():
  xyz={}
  enterEmail = request.form['email']
  enterPassword = request.form['password']

  x = mycoll.find_one({"email": enterEmail})

  if(x == None):
    xyz={
    "isvalid":False,
    "response":"You didn't registered with this email"
    }
    return xyz
  else:
    userPassword = x["password"]  
    if(enterPassword == userPassword ):
      xyz={
      "isvalid":True,
      "response":"You Sucessfully Login"
      }
      return xyz
    else:
      xyz={
      "isvalid":False,
      "response":"You Entered incorrect password"
      }
      return xyz


@app.route("/user",methods=["POST"])
def get_user():
  enterEmail = request.form['email']
  x = mycoll.find_one({"email": enterEmail})
  xyz={
    "name":x["name"],
    "email":x["email"],
    "dob":x["dob"],
    "mobile":x["mobile"],
    "password":x["password"],
    "address":x["address"],
    "gender":x["gender"]}
  return xyz


@app.route("/webdetails",methods=["GET"])
def get_form():
  x = mycurrentwebinar.find_one()
  response={
   "posttestLink": x["posttestLink"],
   "pretestLink": x["pretestLink"],
   "webinarLink": x["webinarLink"]
  }
  return response


@app.route("/updatedetails",methods=["POST"])
def update_webinar():
  postLink = request.form['postLink']
  preLink = request.form['preLink']
  webinarLink = request.form['webinarLink']
  
  x = mycurrentwebinar.find_one()
  
  response={
   "posttestLink": x["posttestLink"],
   "pretestLink": x["pretestLink"],
   "webinarLink": x["webinarLink"]
  }
   
  updated={
   "posttestLink": postLink,
   "pretestLink": preLink,
   "webinarLink": webinarLink
  }

  myquery = response
  newvalues = { "$set": updated }
  mycurrentwebinar.update_one(myquery, newvalues)

  return updated


if __name__ == '__main__':
   app.run()
   
from flask import Flask,jsonify,request
from pymongo import MongoClient

app = Flask(__name__)

CONNECTION_STRING ="mongodb+srv://rohanthakur:NXEaPckQIKO39QaT@testcluster.4aecceu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
mydb=client.Teachable                     
mycoll=mydb.webinar_users
mycurrentwebinar = mydb.event_reg

@app.route('/')
def useraddress():
    xyz={
    "address":mycoll["address"]
    }
    return xyz

@app.route("/signup",methods=["POST"])
def add_user():
  response ={}
  enterName = request.form['name']
  enterEmail = request.form['email']
  enterDOB = request.form['dob']
  enterPassword = request.form['password']
  enterMobile = request.form['mobile']
  enterGender = request.form['gender']
  enterState = request.form['state']
  enterDisctict = request.form['disctict']
  enterTaluka = request.form['taluka']
  enterPin = request.form['pin']

  x = mycoll.find_one({"email": enterEmail})

  if(x != None):
    response={
      "recored status":"You already registed please Login",
      "record":x["email"]
    }
    return response
  else:
    userinfo = {
      "name":enterName,
      "email":enterEmail,
      "dob":enterDOB,
      "mobile":{"$numberLong":enterMobile},
      "password":enterPassword,
      "address":{"state":enterState,"disctict":enterDisctict,"taluka":enterTaluka,"pin":enterPin},
      "gender":enterGender
      }
    mycoll.insert_one(userinfo)
    response={
      "recored status":"Instered Sucessfully",
      "record": enterEmail
    }
    return response
   

@app.route("/validate",methods=["POST"])
def validate():
  xyz={}
  enterEmail = request.form['email']
  enterPassword = request.form['password']

  x = mycoll.find_one({"email": enterEmail})

  if(x == None):
    xyz={
    "isvalid":False,
    "response":"You didn't registered with this email"
    }
    return xyz
  else:
    userPassword = x["password"]  
    if(enterPassword == userPassword ):
      xyz={
      "isvalid":True,
      "response":"You Sucessfully Login"
      }
      return xyz
    else:
      xyz={
      "isvalid":False,
      "response":"You Entered incorrect password"
      }
      return xyz


@app.route("/user",methods=["POST"])
def get_user():
  enterEmail = request.form['email']
  x = mycoll.find_one({"email": enterEmail})
  xyz={
    "name":x["name"],
    "email":x["email"],
    "dob":x["dob"],
    "mobile":x["mobile"],
    "password":x["password"],
    "address":x["address"],
    "gender":x["gender"]}
  return xyz


@app.route("/webdetails",methods=["GET"])
def get_form():
  x = mycurrentwebinar.find_one()
  response={
   "posttestLink": x["posttestLink"],
   "pretestLink": x["pretestLink"],
   "webinarLink": x["webinarLink"]
  }
  return response


@app.route("/updatedetails",methods=["POST"])
def update_webinar():
  postLink = request.form['postLink']
  preLink = request.form['preLink']
  webinarLink = request.form['webinarLink']
  
  x = mycurrentwebinar.find_one()
  
  response={
   "posttestLink": x["posttestLink"],
   "pretestLink": x["pretestLink"],
   "webinarLink": x["webinarLink"]
  }
   
  updated={
   "posttestLink": postLink,
   "pretestLink": preLink,
   "webinarLink": webinarLink
  }

  myquery = response
  newvalues = { "$set": updated }
  mycurrentwebinar.update_one(myquery, newvalues)

  return updated


if __name__ == '__main__':
   app.run()

