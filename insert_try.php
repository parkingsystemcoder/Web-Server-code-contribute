<?php
require "conn.php";

mysqli_query($conn, "SELECT * FROM userinfo");
//insert data
mysqli_query($conn, "INSERT INTO userinfo (id,username,password,code) VALUES (4,'Yenchang',1234,1111)"); 
//delete
mysqli_query($conn, "DELETE FROM userinfo WHERE id='5'"); 
//select only one row to display
$mysql_qry = mysqli_query($conn, "SELECT * FROM userinfo");

while ($rows = mysqli_fetch_array($mysql_qry)):

           $name = $rows['username'];
           $code = $rows['code'];
           $id = $rows['id'];

           echo "ID: $id, Name: $name<br> Code giving $code<br><br>";

           endwhile; 
?>