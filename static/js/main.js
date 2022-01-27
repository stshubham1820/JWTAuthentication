function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');
(function($) {

	"use strict";

	$(".toggle-password").click(function() {

  $(this).toggleClass("fa-eye fa-eye-slash");
  var input = $($(this).attr("toggle"));
  if (input.attr("type") == "password") {
    input.attr("type", "text");
  } else {
    input.attr("type", "password");
  }
});

})(jQuery);
function login(){
  let uname = document.getElementById('uname').value
  let passw = document.getElementById('password-field').value
  //var data = new FormData(document.querySelector('form'))
  let url = 'http://127.0.0.1:8000/api/token/'
  fetch(url,{
    method:'POST',
    headers:{
      'Content-Type': 'application/json',
      'X-CSRFToken':csrftoken,
  },
  body:JSON.stringify({"username":uname,"password":passw}),
  }).then((response)=>{
    console.log("Don'tKnow")
})
}
