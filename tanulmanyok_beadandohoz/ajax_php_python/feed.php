<?php 

/*echo "string<hr>";
for ($i=0; $i < 2; $i++) { 
	echo $i."string";
	echo "<br>";
	sleep(2);
}*/


	$command = escapeshellcmd('python3 feed.py Budapest');
	$output = shell_exec($command);
	echo $output;
	echo "<hr>";




?>