from chatbot import chatbot
from flask import Flask, render_template, request
#import json
from os.path import isfile
from datetime import datetime
file = "log.txt"
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

#@app.route("/save")
#def save_message():
 #   who = request.args.get('sender')
  #  time = str(datetime.now())
   # msg = request.args.get('msg')
   # if not isfile(file):
    #    with open(file,'w') as f:
     #       f.write('{}')
    #with open (file,'r') as f:
     #   convo = json.loads(f.read())
    #convo[time] = {'sender':who,'msg':msg}
    #with open (file,'w') as f:
     #   f.write(json.dumps(convo))
    #return 'Done'

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = str(chatbot.get_response(userText))
    return response


if __name__ == "__main__":
    app.run(debug = True)
