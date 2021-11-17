<?php 

	
	//echo( $_GET['subject']);
	//echo "<br>";
	//echo( $_GET['times']);
	//echo "<br>";

	if ($_GET['times'] == 0) {
		$command = escapeshellcmd('python3 feed.py '. $_GET['subject']);
		$output = json_encode(shell_exec($command));
		echo $output;
	}
	




?>