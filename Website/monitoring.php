<!DOCTYPE html>
<html>
<head>
	<title>Zorggroep monitor</title>
	<link rel="stylesheet" href="style.css">
	<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Lato">
	<link rel="icon" href="z.ico">
</head>
<body>
	<div class="container">
		<div id="kop">
			<img src="zorggroep_logo.png" style="height: 100px; float: left;">
			<a href="login.html"><button>Logout</button></a>
		</div>

		<div id="system-up">
		<iframe src="http://zorggroep.nl/nagios_dashboard.php" style="width: 80%; border: none; height: 1000px;"></iframe>
		</div>

		<div id="camera">
			<div id="camera2"
			<form name="change">
				<SELECT NAME="options" ONCHANGE="document.getElementById('iframe').src = this.options[this.selectedIndex].value">
					<option value="overview.html">Overview</option>
					<option value="camera1.html">Camera 1</option>
					<option value="camera2.html">Camera 2</option>
				</SELECT>
				<iframe name="iframe" id="iframe" src="overview.html" style="border:none; box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);"></iframe>
				<a href="support.html" target="_blank"><img src="asiancorp_logo.png" style="width: 80px; height: 80px; margin-right: 0px; float: right; margin-top: 440px; cursor: pointer;"></a>
			</div>
		</div>
	</div>
</body>
</html>