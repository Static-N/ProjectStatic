$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY>20){
            $(".navbar").addClass("sticky");
        }else{
            $(".navbar").removeClass("sticky");
        }
     });
    $('#sin').click(function(){
        $('.sign-in').toggleClass("show-bx");
    });
    
});