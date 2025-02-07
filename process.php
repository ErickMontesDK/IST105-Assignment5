<?php
// Get inputs from form.php
$number = $_POST['number'];
$text = $_POST['text'];

// just checking there are not empty, but they are "required" in the input fields
if (empty($number) || empty($text)) {
    die("Please, complete all the fields");
}

// executing python script sending the arguments
$command = escapeshellcmd("python process.py $number $text");
$output = shell_exec($command);

// printing the output values in the html 
echo"<style>body { background-color:black; color:white;} .asw_container {display:flex; flex-direction:column; margin-bottom:10px;} .answer::before {content:'-'}</style>";
echo "$output";

?>