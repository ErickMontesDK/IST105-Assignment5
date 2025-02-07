<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Treasure Hunt</title>
    <style>
        body { 
            background-color: black;
            color: white;
        }
        .form-group * {
            display: inline;
        }
        form {
            margin-top:15px;
        }
        h1, b {
            font-size: 16px;
            margin: 0px;
        }
        #number, #text {
            background-color: rgba(255, 255, 255, 0);
            box-sizing: content-box;
            border: none;
            color: yellow;
            width: auto;
            max-width: 50px;
            -moz-appearance: textfield !important;
            appearance: textfield !important;
            -webkit-appearance: none;
        }
        .input_container {
            color: yellow;
        }
        .input_container::before {
            content: "[";
            margin-left: 5px;
        }
        .input_container::after {
            content: "]";
            margin-left: 2px;
        }
        input[type="submit"] {
            background-color: rgba(255, 255, 255, 0);
            border: none;
            margin-top: 15px;
            padding: 0;
            color: yellow;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Interactive Treasure Hunt!</h1>
    <b>Enter your details to solve the puzzle and find the treasure.</b>

    <!-- form inputs -->
    <form action="process.php" method="POST">
        <div class="form-group">
            <label for="number">Number (e.g., birth year):</label>
            <div class="input_container">
                <input type="number" id="number" name="number" required>
            </div>
        </div>
        <div class="form-group">
            <label for="text">Text (e.g., name or secret word):</label>
            <div class="input_container">
                <input type="text" id="text" name="text" required>
            </div>
        </div>
        

        

        <input type="submit" value="[Solve the Puzzle]">
    </form>


</body>
</html>