<?php 

	
	//echo( $_GET['subject']);
	//echo "<br>";
	//echo( $_GET['times']);
	//echo "<br>";

	$test = 'tumor';
	//if ($_GET['times'] == 0) {
		$command = escapeshellcmd('LD_LIBRARY_PATH=/lib64/:$LD_LIBRARY_PATH python3 academic_search.py tumor');
		//$command = escapeshellcmd('python3 academic_search.py tumor');//. /*$_GET['subject']*/$test);
		$output = shell_exec($command);
		//echo $command;
		//echo "<hr>";
		header('Content-type: application/json');
		echo $output;
	//}
		


?>