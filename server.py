from flask import Flask,render_template,request,jsonify
from flask_socketio import SocketIO,emit
import webbrowser
import socket
import subprocess
import platform
ss='Error'
s='Error'
def cityboii():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8',80))
        f=s.getsockname()[0]
    except Exception:
        f='127.0.0.1'
    finally:
        s.close()
    try:
     if(platform.system()=='Windows'):
        ss=subprocess.check_output(['powershell',"-Command","(Get-NetConnectionProfile | Where-object {$_.InterfaceAlias -like '*Wi-Fi*'}).Name"],
        text=True).strip()
     elif(platform.system()=="Linux"):
         ss=subprocess.check_output(['iwgetid',"-r"],text=True).strip()
     elif(platform.system()=='Darwin'):
         ss=subprocess.check_output(['/System/Library/PrivateFrameworks/Apple80211.framework/Version/Current/Resources/airport',"-I"],text=True).split(
             'SSID: '[1].splitlines()[0])
    except Exception as e:
        print(f'Failed to get your ssid | {e}')
        return f'Failed to get your ssid | {e}'
    return f,ss

app=Flask(__name__)
app.config["AUTH"]="local"
s=SocketIO(app,cors_allowed_origins="*")
mainchat=[]
users={}
imimname='group'
@app.route('/',methods=["GET"])
def w():
    global abv
    return render_template('index.html')
@s.on("mainchat")
def chat(dih):
    dihname=users.get(request.sid,'unknown')
    d={'name':dihname,"msg":dih}
    mainchat.append(d)
    mainchat[:]=mainchat[-10:]
    emit("mainchat",d,broadcast=True)
    print(f"│ Notification : {dihname} sent a message ")
@s.on("join")
def usrn(dih):
    users[request.sid]=dih['name']
    print(f"│ User connected : {users.get(request.sid,request.sid)}")
    for dih in mainchat:
        emit("mainchat",dih)
@s.on("disconnect")
def sybau():
    print(f"│ User disconnected : {users.get(request.sid,request.sid)}")
    users.pop(request.sid,None)
if __name__=='__main__':
    print(
        """
        `7MMF'  `7MMF'                   mm       MMP""MM""YMM      `7MM  `7MM      
          MM      MM                     MM       P'   MM   `7        MM    MM     
          MM      MM  ,pW"Wq.  ,pP"Ybd mmMMmm          MM   ,6"Yb.    MM    MM  ,MP'
          MMmmmmmmMM 6W'   `Wb 8I   `"   MM            MM  8)   MM    MM    MM ;Y   
          MM      MM 8M     M8 `YMMMa.   MM            MM   ,pm9MM    MM    MM;Mm   
          MM      MM YA.   ,A9 L.   I8   MM            MM  8M   MM    MM    MM `Mb. 
        .JMML.  .JMML.`Ybmd9'  M9mmmP'   `Mbmo       .JMML.`Moo9^Yo..JMML..JMML. YA.
                                                                            
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                  
""")
    sss,ssss=cityboii()
    print("│ Server : running")
    print(f"│ Local access : http://127.0.0.1:6767/")
    print(f"│ Lan access (other devices/wifi): http://{sss}:6767/")
    print(f"│ Wifi SSID : {ssss}")
    print(" ")
    s.run(app,host="0.0.0.0",port=6767,debug=False)
