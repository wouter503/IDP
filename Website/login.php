<?php
   ob_start();
   session_start();
?>
<!DOCTYPE html>
<html>
<head>
<title>Login</title>
<link rel="stylesheet" href="login.css">
<link rel="icon" href="z.ico">
<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Lato">
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
</head>
<body>
<script language="javascript">
$(document).ready(function(){
  $('.login-button').on('click', function(event){
    event.preventDefault();
    console.log('check form');
    id = $('[name="id"]').val();
    pass = $('[name="pass"]').val();
    console.log(id, pass);

    if( id == 'zorggroep' && pass == 'domotica') {
      window.location.replace("monitoring.html");
    } else {
      window.alert('inlog niet correct');
    }
  });
});
</script>
<img src="zorggroep_logo.png" style="height: 100px;">
<h1>Property of Asian Corp.<br>
    In cooperation with Zorggroep</h1>
<div class="login-page">
  <div class="form">
    <form class="register-form">
      <input type="text" placeholder="name"/>
      <input type="password" placeholder="password"/>
      <input type="text" placeholder="email address"/>
      <button>create</button>
      <p class="message">Already registered? <a href="#">Sign In</a></p>
    </form>
    <form class="login-form">
      <input type="text" placeholder="username" name="id"/>
      <input type="password" placeholder="password" name="pass"/>
      <button class="login-button">login</button>
    </form>
  </div>
</div>
</body>
</html>