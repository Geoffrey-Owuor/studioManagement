<!DOCTYPE html>
<html>
<head>
	<title>Session Manager</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	<link href="https://fonts.googleapis.com/css?family=Quicksand&display=swap" rel="stylesheet">
	<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0">
</head>
<body>
	<div class="container">
		<div class="contact-box">
			<div class="left"></div>
			<div class="right">
				<h2>Manage Your Sessions</h2>
			 <form action="insert_data.py" method="post">
				<input type="text" class="field" placeholder="Your user ID" name="user_id" id="user_id" required>
				<input type="text" class="field" placeholder="Your Username" name="username" id="username" required>
				<input type="text" class="field" placeholder="Your Email" name="email" id="email" required>
				<input type="text" class="field" placeholder="Session(e.g., recording at...)" name="session" id="session" required>
				<input type="text" class="field" placeholder="Date(YY-MM-DD)" name="date" id="date" required>
				<!--<textarea placeholder="More details about your session" class="field"></textarea>-->
				<input class="btn" type="submit" value="Record">
			 </form>
			 <br><br>
			 <a class="btn" href="http://localhost/studio/retrieve_data.php">View Sessions</a>
			</div>
		</div>
	</div>
</body>
</html>