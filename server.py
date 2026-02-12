from flask import Flask,render_template,request,jsonify
from flask_socketio import SocketIO,emit
import webbrowser
import socket
import subprocess
import threading
import platform
import os
import sys
import shutil

if(platform.system()=="Windows"):
    import pystray
    from PIL import Image
    from pystray import MenuItem as dihtem
    import ctypes
HOSTTALK0INFO0VER=1.0
APPDATAAHH=os.getenv("APPDATA")
APPROOT=os.path.join(APPDATAAHH,"HostTalk")
os.makedirs(APPROOT,exist_ok=True)
def exe():
   if getattr(sys,'frozen',False):
      return sys._MEIPASS
   return os.path.dirname(os.path.abspath(__file__))

temp0dih0server=exe()
def packurbagsahh(dih,seconddih):
 os.makedirs(seconddih,exist_ok=True)
 for dihh in os.listdir(dih):
    sdih=os.path.join(dih,dihh)
    ddih=os.path.join(seconddih,dihh)
    if not os.path.exists(ddih):
       if os.path.isdir(sdih):
          shutil.copytree(sdih,ddih)
       else:
          shutil.copy2(sdih,ddih)

packurbagsahh(os.path.join(temp0dih0server,"static"),
              os.path.join(APPROOT,"static"))
packurbagsahh(os.path.join(temp0dih0server,"templates"),
              os.path.join(APPROOT,"templates"))

if(platform.system()=="Windows"):
        ker=ctypes.WinDLL("kernel32")
        use=ctypes.WinDLL("user32")
        SH=5
        HI=0
        def consolepi():
           return ker.GetConsoleWindow()
        def hideall():
           h=consolepi()
           if(h):
              use.ShowWindow(h,HI)
        def showall():
           h=consolepi()
           if h:
              use.ShowWindow(h,SH)
def traySH(ic,it):
   if platform.system()=="Windows":
      h=consolepi()
      if h:
         use.ShowWindow(h,SH)
def trayQU(ic,it):
   try:
      s.stop()
   except:
      pass
   ic.stop()
   os._exit(0)
def trayIC():
   if platform.system() !="Windows":
      return
   img=Image.open(os.path.join(exe(),'icon.ico'))
   menu=(
      dihtem("show console",traySH),
      dihtem("quit",trayQU)
   )
   icon=pystray.Icon("HostTalk",img,"HostTalk Server",menu)
   icon.run()

ss='Error'
se='Error'
pref0admintoall=True
pref0showall=False
startcommandline=False #remember ur ahh to turn ts to false in production
if startcommandline:
   temp0in0com=input("Press Enter to start server or enter -s to enter command mode...    ")
   if temp0in0com.strip()=="":
     pass
   elif temp0in0com=="-s":
      print('Commands activated.')
      print('Enter "settings" to change settings')
      temp0in0call=input()
      if(temp0in0call.lower().strip()=="settings"):
         print("SETTINGS :\n   1 => Admin permission to any user(bool)\n   2 => Show sensitive information in the server console(bool)")
         temp0in0set=input()
         if(temp0in0set.lower().strip()=="1"):
            input("")
   else:
      print('Unknown command. Starting server')
      pass
def cityboii():
    se=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        se.connect(('8.8.8.8',80))
        f=se.getsockname()[0]
    except Exception:
        f='127.0.0.1'
    finally:
        se.close()
    try:
     if(platform.system()=='Windows'):
        ss=subprocess.check_output(['powershell',"-Command","(Get-NetConnectionProfile | Where-object {$_.InterfaceAlias -like '*Wi-Fi*'}).Name"],
        text=True).strip()
     elif(platform.system()=="Linux"):
         ss=subprocess.check_output(['iwgetid',"-r"],text=True).strip()
     elif(platform.system()=='Darwin'):
         ss=subprocess.check_output(['/System/Library/PrivateFrameworks/Apple80211.framework/Version/Current/Resources/airport',"-I"],text=True).split(
             'SSID: ')[1].splitlines()[0]
    except Exception as e:
        print(f'Failed to get your ssid | {e}')
        return f'Failed to get your ssid | {e}'
    return f,ss

app=Flask(__name__,template_folder=os.path.join(APPROOT,"templates"),static_folder=os.path.join(APPROOT,"static"))
app.config["AUTH"]="local"
s=SocketIO(app,cors_allowed_origins="*")
mainchat=[]
users={}
imimname='group'
@app.route('/',methods=["GET"])
def w():
    return render_template('index.html')
@s.on("mainchat")
def chat(dih):
    dihname=users.get(request.sid,'unknown')
    d={'name':dihname,"msg":dih}
    mainchat.append(d)
    mainchat[:]=mainchat[-10:]
    emit("mainchat",d,broadcast=True)
    if pref0showall==True:
        tempmessageshow=f'"{dih}"'
    else:
        tempmessageshow=""
    print(f"│ Notification : {dihname} sent a message {tempmessageshow} ")
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
@app.route('/api/ip')
def ip():
    ip,ssid=cityboii()
    return jsonify({"ip": ip,
                    "ssid":ssid})
@s.on("shut")
#yo fix ts before uploadin to github
def off():
   if pref0admintoall:
    print(f"│ {users.get(request.sid,request.sid)} shut down the server.")
    s.stop()
   else:
    print(f"│ {users.get(request.sid,request.sid)} tried to shut down the server.")
    print(f"│ Permission denied. {users.get(request.sid,request.sid)} doesnt have the permission to shut down the server down")
    print(f"│ Turn on 'Admin to all' to give permission to {users.get(request.sid,request.sid)} shut down the server down")

if __name__=='__main__':
    if platform.system()=="Windows":    
        if consolepi():
           hideall()
        threading.Thread(target=trayIC,daemon=True).start()

    print(
        f"""
        `7MMF'  `7MMF'                   mm       MMP""MM""YMM      `7MM  `7MM      
          MM      MM                     MM       P'   MM   `7        MM    MM     
          MM      MM  ,pW"Wq.  ,pP"Ybd mmMMmm          MM   ,6"Yb.    MM    MM  ,MP'
          MMmmmmmmMM 6W'   `Wb 8I   `"   MM            MM  8)   MM    MM    MM ;Y   
          MM      MM 8M     M8 `YMMMa.   MM            MM   ,pm9MM    MM    MM;Mm   
          MM      MM YA.   ,A9 L.   I8   MM            MM  8M   MM    MM    MM `Mb. 
        .JMML.  .JMML.`Ybmd9'  M9mmmP'   `Mbmo       .JMML.`Moo9^Yo..JMML..JMML. YA.
                                                                                        {HOSTTALK0INFO0VER}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                  
""")
    sss,ssss=cityboii()
    print("│ Server : running")
    print(f"│ Local access : http://127.0.0.1:6767/")
    print(f"│ Lan access (other devices/wifi): http://{sss}:6767/")
    print(f"│ Wifi SSID : {ssss}")
    print(" ")
    print(f"│ Opening : http://{sss}:6767/")
    webbrowser.open_new_tab(f'http://{sss}:6767/')
    print('')
    s.run(app,host="0.0.0.0",port=6767,debug=False)
