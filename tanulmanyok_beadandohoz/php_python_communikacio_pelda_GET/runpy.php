<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>


<?php 
	$value = $_GET['passValue'];
	echo $value;

	$command = escapeshellcmd("python3 test.py \"$value\" ");
	$output = shell_exec($command);
	echo $output;	

?>



</body>
</html>