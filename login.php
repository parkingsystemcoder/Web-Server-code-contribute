<?php
require "conn.php";
$username = $_POST["username"];
$password = $_POST["password"];
//$username = "Jia";
//$password = "123";
$mysql_qry = "UPDATE userinfo_user SET paystatus = '0'  where username like '$username'";
mysqli_query($conn, $mysql_qry);
$mysql_qry = "select * from `userinfo_user` where username like '$username' and password like '$password';";
//mysqli_query($conn, "INSERT INTO `userinfo 2.0` (`id`, `username`, `password`, `paystatus`, `code`) VALUES (NULL, '$username', '$password', '', 'rand(0,9999)')");

$result = mysqli_query($conn, $mysql_qry);
if (mysqli_num_rows($result) > 0) {
	echo "login success!";
}
else {
	echo "login not success!";
}

?>