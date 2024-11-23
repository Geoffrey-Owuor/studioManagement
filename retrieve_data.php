<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Retrieval</title>
    <link rel="stylesheet" type="text/css" href="style1.css">
    <link href="https://fonts.googleapis.com/css?family=Quicksand&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>
<body>
<div class="container">
<h1 class="real">List Of Recorded Sessions</h1>
<h3 class="real"><a href="http://localhost/studio/index.php">Back to main menu</a></h3>
<br>
<table class="table">
    <thead>
        <tr>
            <th>user_id</th>
            <th>username</th>
            <th>email</th>
            <th>session</th>
            <th>date</th>
        </tr>
    </thead>
    <tbody>
    <?php
    //Connect to the database
    $hostName = "localhost";
    $userName = "root";
    $password ='';
    $databaseName = "trial_data";
    $connection = new mysqli($hostName, $userName, $password, $databaseName);

    if ($connection->connect_error){
        die("Connection failed: ". $connection->connect_error);
    }
   //Read all recorded sessions from the table sessions
    $sql = "SELECT * FROM sessions";
    $result = $connection->query($sql);

    if(!$result){
        die("Invalid query: ". $connection->error);
    }

    //READ DATA OF EACH ROW
    while($row = $result->fetch_assoc()){
        echo "<tr>
            <td>". $row["user_id"]. "</td>
            <td>". $row["username"]. "</td>
            <td>". $row["email"]. "</td>
            <td>". $row["session"]. "</td>
            <td>". $row["date"]. "</td>
          </tr>";
    }

    ?>
    </tbody>
</table>
</div>
</body>
</html>