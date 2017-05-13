<?php
require "conn.php";
$username= $_POST["username"];
//$code = "0";

mysqli_select_db($conn, "django_database_rev");
$mysql_qry = "select * from `serversysteminfo_systeminfo` where username like '$username'";
$result = mysqli_query($conn, $mysql_qry);
while ($row = mysqli_fetch_assoc($result))
	{
		$output[]= $row;
	}

echo json_encode($output);
?>