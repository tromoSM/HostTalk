window.addEventListener("DOMContentLoaded",function(){
    document.querySelectorAll(`transparent-closer`).forEach(a=>{
        a.addEventListener('click',function(){
            a.closest(`popup-window`).style.display='none'
        })
    })
    refreshselected()
    //checkopt
    let b=localStorage.getItem('app')
    if(b){
        refreshselected()
        if(b=="dark"){
            document.documentElement.setAttribute('dark','true')
        }
        else{
            document.documentElement.setAttribute('dark','fuhnaw') 
        }
    }
    let c=localStorage.getItem('theme')
    if(c){
        refreshselected()
        if(c=="26"){
            document.documentElement.setAttribute('ios','26')
        }
        else if(c=="16"){
            document.documentElement.setAttribute('ios','16')
        }
        else if(c=="6"){
            document.documentElement.setAttribute('ios','6')
        }
    }
    let d=localStorage.getItem('bubble')
    if(d){
           let hw=document.documentElement
            hw.style.setProperty('--sys-d-radius',`${d}px`)
    }
    //no checkin on loader below yo. sybau
    document.querySelectorAll('[action]').forEach(each=>{
        each.setAttribute('selected','none')
      if(each.getAttribute('event')=="input"){
        each.addEventListener('input',function(){
         if(each.getAttribute('range')=="border-radius"){
           let hw=document.documentElement
           localStorage.setItem('bubble',each.value)
            hw.style.setProperty('--sys-d-radius',`${each.value}px`)
         }
        })
      }
      each.addEventListener('click',function(){
        let a=each.getAttribute('action')
        if(a=="darkmode"){
            document.documentElement.setAttribute('dark','true')
            localStorage.setItem('app','dark')
        }
        else if(a=="lightmode"){
            document.documentElement.setAttribute('dark','fuhnaw') 
            localStorage.setItem('app','fuhnaw')
        }
        else if(a=="showset"){
            document.querySelector(`[visible='settings']`).style.display='flex'
        }
        else if(a=="26theme"){
            localStorage.setItem('theme','26')
            document.documentElement.setAttribute('ios','26')
        }
        else if(a=="16theme"){
            localStorage.setItem('theme','16')
            document.documentElement.setAttribute('ios','16')
        }
        else if(a=="6theme"){
            document.documentElement.setAttribute('ios','6')
            localStorage.setItem('theme','6')
        }
        refreshselected()
     })      
    })
   
    function refreshselected(){
        let a=document.documentElement.getAttribute('dark')
        if(a=="true"){
            document.querySelector('[action=darkmode]').setAttribute('selected','app')
            document.querySelector('[action=lightmode]').setAttribute('selected','nah')
        }
        else if(a=='fuhnaw'){
            document.querySelector('[action=lightmode]').setAttribute('selected','app')
            document.querySelector('[action=darkmode]').setAttribute('selected','nah')
        }
        let b=document.documentElement.getAttribute('ios')
        if(b=="6"){
            document.querySelector('[action="26theme"]').setAttribute('selected','nah')
            document.querySelector('[action="16theme"]').setAttribute('selected','nah')
            document.querySelector('[action="6theme"]').setAttribute('selected','app')
        }
        else if(b=="16"){
            document.querySelector('[action="26theme"]').setAttribute('selected','nah')
            document.querySelector('[action="16theme"]').setAttribute('selected','app')
            document.querySelector('[action="6theme"]').setAttribute('selected','nah')
        }
        else if(b=="26"){
            document.querySelector('[action="26theme"]').setAttribute('selected','app')
            document.querySelector('[action="16theme"]').setAttribute('selected','nah')
            document.querySelector('[action="6theme"]').setAttribute('selected','nah')
        }
    }
})
