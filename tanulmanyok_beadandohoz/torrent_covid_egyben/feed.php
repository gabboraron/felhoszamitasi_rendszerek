<?php 
	
	//echo( $_GET['subject']);
	//echo "<br>";
	//echo( $_GET['times']);
	//echo "<br>";

    if ($_GET['times'] == 0) {
        $command = escapeshellcmd('python3 edited_feed.py '. $_GET['subject']);
        $output = shell_exec($command);
        
        header('Content-type: application/json');
        echo $output;
    }

	




?>