
var myBtnSignIn = document.getElementById("btn-sign-in"),
    myBtnSignUp = document.getElementById("btn-sign-up"),
    myContainer = document.getElementById("container"),
    mybtnforgetpass = document.getElementById("btn-forget-password") ;

window.onload =  function(){
    this.myBtnSignIn.click() ;    
    this.myOrangeTheme.click() ;
}


myBtnSignIn.onclick = function() {
    myBtnSignIn.style.backgroundColor="orange" ;
    myBtnSignUp.style.backgroundColor="rgba(255,255,255,0.2)" ;
    myContainer.style.transform="translateX(0px)"
}


myBtnSignUp.onclick = function() {
    myBtnSignUp.style.backgroundColor="orange" ;
    myBtnSignIn.style.backgroundColor="rgba(255,255,255,0.2)" ;
    myContainer.style.transform="translateX(-320px)"
}

mybtnforgetpass.onclick = function(){
    myBtnSignIn.style.backgroundColor="rgba(255,255,255,0.2)" ;
    myContainer.style.transform="translateX(320px)"    
}


var myGrayTheme = document.getElementById("gray"),
    myOrangeTheme = document.getElementById("orange"),
    myPinkTheme = document.getElementById("pink") 

function resetColor(){
    myGrayTheme.style.border="none" ;
    myOrangeTheme.style.border="none" ;
    myPinkTheme.style.border="none" ;
}

myGrayTheme.onclick = function() {
    resetColor() ;
    this.style.border="2px solid pink" ;
    document.body.style.backgroundColor="lightgray" ;
    
}

myOrangeTheme.onclick = function() {
    resetColor() ;
    this.style.border="2px solid pink" ;
    document.body.style.backgroundColor="lightsalmon" ;
    
}

myPinkTheme.onclick = function() {
    resetColor() ;
    this.style.border="2px solid pink" ;
    document.body.style.backgroundColor="lightpink" ;
    
}