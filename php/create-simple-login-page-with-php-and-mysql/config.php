<?php

session_start();

$host = "localhost"; /* Host name */
$user = "anvesh"; /* User */
$password = "anvesh123"; /* Password */
$dbname = "nsdb"; /* Database name */

$con = mysqli_connect($host, $user, $password,$dbname);
// Check connection
if (!$con) {
 die("Connection failed: " . mysqli_connect_error());
}