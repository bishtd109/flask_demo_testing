from flask import Flask,request
app=Flask(__name__)
@app.route("/check/",methods=['GET'])
def func():

    return "<h1>THIS IS FLASK APPP MADE BYME<h1>"

if __name__ == '__main__':
    app.run();