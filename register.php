<?php
require "conn.php";
$username = $_POST["username"];
$password = $_POST["password"];
//$username = "bphui";
//$password = "komamon";
$randomnum = rand(0,9999);
mysqli_query($conn, "INSERT INTO `userinfo_user` (`id`, `username`, `password`, `paystatus`, `code`) VALUES (NULL, '$username', '$password', '', '$randomnum')");
echo "register success!";
?>