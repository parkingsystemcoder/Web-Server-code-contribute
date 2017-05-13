<?php
require "pi_conn.php";
$code = $_POST["code"];
$status = $_POST["status"];
$id = $_POST["id"];
mysqli_query($conn, "UPDATE carparkslot_parkingslot SET status = '$status', code = '$code' where id like '$id'");
echo "Insert Successful";
?>