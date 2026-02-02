window.addEventListener("DOMContentLoaded",function(){
    chat=document.getElementById('chat')
    const sdihkid=io()
    let usrahh=localStorage.getItem('userID')
    if(!usrahh){
        usrahh=prompt("Enter username to continue")
        localStorage.setItem("userID",usrahh)
    }
    sdihkid.emit('join',{name:usrahh})
    sdihkid.on("mainchat",d=>{
        const each$$cov=document.createElement("div")
        const each$$msg=document.createElement("p")
        each$$msg.innerHTML=`${d.msg}`
        if(d.msg.length>=62){
            each$$msg.setAttribute('large','message')
        }
        if(d.name==usrahh){
            each$$msg.setAttribute('mine','yesvro')
            each$$cov.setAttribute('setmarg','02')
        }
        else{
            let a=document.createElement('p')
            a.innerHTML=d.name
            a.setAttribute('tag','user')
            notiff$osund=new Audio(`static/pulse.mp3`)
            each$$msg.setAttribute('mine','fuhnaw')
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
