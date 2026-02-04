window.addEventListener("DOMContentLoaded",function(){
    let temp$$all$$cl=document.querySelector('rightclick')
    document.documentElement.addEventListener("contextmenu",function(dih){
     dih.preventDefault()
     temp$$all$$cl.style.top=`${dih.pageY}px`
     temp$$all$$cl.style.left=`${dih.pageX}px`
     temp$$all$$cl.style.display=`flex`
    })
    document.addEventListener("click",function(dih){
        if(!temp$$all$$cl.contains(dih.target)){
            temp$$all$$cl.style.display="none"
        }
    })
    temp$$all$$cl.querySelectorAll('brochacho').forEach(dih=>{
        dih.addEventListener("click",function(){
        let temp$$all$$op=dih.getAttribute("act")
         if(temp$$all$$op=="settings"){
            document.querySelector(`[action="showset"]`).click()
         } 
         else if(temp$$all$$op=="invite"){
            document.querySelector(`[visible="invite"]`).style.display="flex"
         }
        })
    })
    document.querySelectorAll(`[i]`).forEach(fih=>{
     let temp$$all$$fi=fih.getAttribute('i')
        fetch('/api/ip').then(dih=>dih.json()).then(dihta=>{
     if(temp$$all$$fi=="ip"){
        fih.innerHTML=`http://${dihta.ip}:6767`
     }
     else if(temp$$all$$fi=="ssid"){
        fih.innerHTML=dihta.ssid
     }
        })
    })
})
