<?php
// Get inputs from form.php by using their names attributes
$number = $_POST['number'];
$text = $_POST['text'];

// just checking if there are not empty, even though they have the "required" attribute in the input fields
if (empty($number) || empty($text)) {
    die("Please, complete all the fields");
}

// executing python script sending the arguments
//escapeshellcmd prevents to execute the text received as a command
$command = escapeshellcmd("python process.py $number $text");
//executing and recieving the response from the python script
$output = shell_exec($command);

// printing the output values in the html, and adding some css style
echo"<style>body { background-color:black; color:white;} .asw_container {display:flex; flex-direction:column; margin-bottom:10px;} .answer::before {content:'-'}</style>";
echo "$output";

?>