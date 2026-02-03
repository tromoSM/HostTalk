window.addEventListener("DOMContentLoaded",function(){
    chat=document.getElementById('chat')
    let notificationA=new Audio(`static/recieved.mp3`)
    let notificationB=new Audio(`static/sent.mp3`)
    const sdihkid=io()
    let usrahh=localStorage.getItem('userID')
    if(!usrahh){
        usrahh=prompt("Enter username to continue")
        localStorage.setItem("userID",usrahh)
    }
 const orgAud=this.window.Audio
  window.Audio=function(...args){
  const audio=new orgAud(...args)
  audio.volume=0.3
  return audio
  }
    sdihkid.emit('join',{name:usrahh})
    sdihkid.on("mainchat",d=>{
        const each$$cov=document.createElement("div")
        const each$$msg=document.createElement("p")
        each$$msg.innerHTML=`${d.msg}`
        if(d.msg.length>=31){
            each$$msg.setAttribute('large','2')
            each$$cov.setAttribute('large','2c')
        }
        if(d.name==usrahh){
            each$$msg.setAttribute('mine','yesvro')
            each$$cov.setAttribute('mine','yescover')
            each$$cov.setAttribute('setmarg','02')
        }
        else{
            let a=document.createElement('p')
            a.innerHTML=d.name
            a.setAttribute('tag','user')
            each$$msg.setAttribute('mine','fuhnaw')
            each$$cov.setAttribute('mine','nocover')
            each$$cov.appendChild(a)
        }
        each$$cov.setAttribute("bubble","cover")
        chat.appendChild(each$$cov)
        each$$cov.appendChild(each$$msg)
        window.scrollTo(0,document.body.scrollHeight);
    })
    window.sendingmyahh=function(){
        const inp=document.querySelector('[dih="yo"]')
       if(inp.value.trim()!==""){
        sdihkid.emit("mainchat",inp.value)
        inp.value=""
        notificationB.play() 
        window.scrollTo(0,document.body.scrollHeight);
       }

    }
    document.querySelector('[dih="yo"]').addEventListener('keydown',function(dih){
        if(dih.key=="Enter"){
            sendingmyahh()
        }
    })

    function focusin(){ document.querySelector('[dih="yo"]').focus()}
    document.querySelector('[oc="p"]').addEventListener('click',focusin)
    window.addEventListener('keydown',focusin)
})
