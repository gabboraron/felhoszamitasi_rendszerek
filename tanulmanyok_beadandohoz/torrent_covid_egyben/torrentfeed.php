<?php 

	
	//echo( $_GET['subject']);
	//echo "<br>";
	//echo( $_GET['times']);
	//echo "<br>";

	$test = 'tumor';
	//if ($_GET['times'] == 0) {
		$command = escapeshellcmd('python3 academic_search.py '. /*$_GET['subject']*/$test);
		$output = json_encode(shell_exec($command));
		echo $output;
	//}
	




?>