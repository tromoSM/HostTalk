from flask import Flask,render_template,request,jsonify
from flask_socketio import SocketIO,emit
app=Flask(__name__)
app.config["AUTH"]="local"
s=SocketIO(app,cors_allowed_origins="*")
mainchat=[]
users={}
imimname='group'
@app.route('/',methods=["GET"])
def w():
    print(request.remote_addr)
    return render_template('index.html')
@s.on("mainchat")
def chat(dih):
    dihname=users.get(request.sid,'unknown')
    d={'name':dihname,"msg":dih}
    mainchat.append(d)
    mainchat[:]=mainchat[-10:]
    emit("mainchat",d,broadcast=True)
@s.on("join")
def usrn(dih):
    users[request.sid]=dih['name']    
    for dih in mainchat:
        emit("mainchat",dih)
@s.on("connect")
def on():
    print(f"hello vro {request.sid}")

@s.on("disconnect")
def sybau():
    users.pop(request.sid,None)
    print(f"bye vro {request.sid}")

if __name__=='__main__':
    print('fuh')
    s.run(app,host="0.0.0.0",port=6767,debug=False)