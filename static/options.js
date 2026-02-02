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
    //no checkin on loader below yo. sybau
    document.querySelectorAll('[action]').forEach(each=>{
        each.setAttribute('selected','none')
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
    }
})
