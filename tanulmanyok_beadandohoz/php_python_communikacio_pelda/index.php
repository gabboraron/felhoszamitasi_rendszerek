<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>


<?php 
	echo "alma";

	$command = escapeshellcmd('python3 test.py');
	$output = shell_exec($command);
	echo $output;	

?>



</body>
</html>