<?php
include("connection.php");
session_start();
?>
 
<?php
if (isset($_POST['logout'])) {
    // Unset all session variables
    $_SESSION = array();

    // Destroy the session
    session_destroy();

    // Redirect to the login page
    header("location: index.php");
    exit;
}
?>

<!DOCTYPE HTML>
<html>

<head>

    <title>Target Market Profiling System</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <noscript>
        <link rel="stylesheet" href="assets/css/noscript.css" />
    </noscript>


    <style>
        /* CSS for table */
        .t {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            border: none;
            /* Remove border from table */
            background-color: #f8f8f8;
            /* Add background color to table */
            border-radius: 10px;
            /* Increase border radius for rounded edges */
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
            /* Add box shadow */
        }

        th,
        td {
            border: none;
            /* Remove borders from table cells */
            padding: 2px;
            /* Increase padding for more spacing */
            text-align: left;
            font-size: 12px;
            /* Add font size */
            color: #333;
            /* Add text color */
            margin: 0px;

        }

        th {
            background-color: #f2f2f2;
            font-weight: bold;
            /* Add bold font weight to table headers */
            font-size: 10px;
        }

        th:first-child,
        td:first-child {
            border-left: none;
        }

        th:last-child,
        td:last-child {
            border-right: none;
        }

        /* Add hover effect for table rows */
        tr:hover {
            background-color: #fafafa;
            /* Change background color on hover */
            /* Update row hover color here */
        }

        /* Add zebra striping effect for table rows */
        tr:nth-child(even) {
            background-color: #e9e9e9;
        }

        /* Add text wrapping for table cells */
        th,
        td {
            white-space: nowrap;
            /* Prevent text from wrapping */
            overflow: hidden;
            /* Hide overflowed text */
            text-overflow: ellipsis;
            /* Add ellipsis for overflowed text */
        }

        /* Add box shadow for table */
        .t {
            box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
            /* Add box shadow */
        }

        /* Add transition effect for hover */
        .t:hover {
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
            /* Add box shadow on hover */
        }



        .pagination {
            display: inline-block;
            margin: 10px 0;
        }

        .pagination a,
        .pagination span {
            display: inline-block;
            padding: 5px 10px;
            margin: 0 5px;
            border: 1px solid #ccc;
            background-color: #fff;
            color: #333;
            text-decoration: none;
            width: 45px;
            text-align: center;
        }

        .pagination .active {
            border: 1px solid #333;
            background-color: #333;
            color: #fff;
        }


        .pagination a:hover {
            background-color: #ddd;
        }





        /* Style for the line segment */
        .line-segment {
            width: 100%;
            height: 1px;
            background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0));
            background-repeat: no-repeat;
            background-position: bottom;
            margin-top: 20px;
            margin-bottom: 20px;
            /* Increased margin for more spacing */
        }

        /* Style for the heading tags */
        h2 {
            margin-top: 0;
            /* Remove default margin */
            margin-bottom: 10px;
            /* Add margin for spacing */
            font-size: 24px;
            /* Increase font size for more emphasis */
            color: #333;
            /* Set font color */
        }





        /* Add CSS for image enlargement on hover */
        img {
            border-radius: 5px;
            /* Add border radius */
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);
            /* Add box shadow */
            transition: transform 0.3s ease-in-out;
            /* Add transition for smooth effect */
            max-width: 100%;
            /* Ensure images fit within container */
            height: auto;
            /* Maintain aspect ratio */
            border-radius: 5px;
            /* Add border radius */
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
            /* Add box shadow */
        }

        img:hover {
            transform: scale(1.01);
            /* Enlarge image on hover */
        }




        .typing-effect {
            position: relative;
            overflow: hidden;
            /* Add a constant blinking cursor */
            animation: typing 3s steps(20);
        }

        /* CSS animation for typing effect */
        @keyframes typing {
            from {
                width: 0;
            }

            to {
                width: 100%;
            }
        }

        /* Styling for blinking cursor */
        .typing-effect::after {
            content: "_";
            position: absolute;
            right: 15;
            animation: blinking 1s infinite;
        }

        /* CSS animation for blinking cursor */
        @keyframes blinking {

            from,
            to {
                opacity: 0;
            }

            50% {
                opacity: 1;
            }
        }



        /* CSS styles for the "Points Available" section */
        .points {
            margin-left: 20px;
            font-weight: bold;
            color: #000;
            display: inline-block;
            padding: 10px;
            background-color: #f2f2f2;
            border-radius: 5px;
        }

        body {
            background-image: url("images/overlay.png"), linear-gradient(60deg, #e37682 70%, #5f4d93 90%);
        }


        .rainbow-line {
            height: 3px;
            background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        }
    </style>




</head>

<body class="is-preload">

    <!-- Wrapper -->
    <div id="wrapper">

        <!-- Header -->
        <header id="header" class="alt">
            <span class="logo"><img src="https://i.ibb.co/c6XrQT7/ecommerce-campaign-concept-illustration-114360-8432-removebg-preview.png" height="200" width="200" alt="ecommerce-campaign-concept-illustration-114360-8432-removebg-preview"></span>
            <h1 style="font-family: Consolas, monospace" class="typing-effect">Target Market Profiling System</h1>
            <p>Welcome User<br />
                built by Ishan Katoch, Tarushi Rastogi, Kamlesh Rani, Sonali Jindal.
            </p>
        </header>

        <!-- Nav -->
        <nav id="nav">
            <ul>
                <li><a href="#intro" class="active">Transactions</a></li>
                <li><a href="#first">Graphs</a></li>
                <li><a href="#second">Recommendations</a></li>
                <li><a href="#cta">Log Out</a></li>

            </ul>
        </nav>




        <!-- Main -->
        <div id="main">

            <!-- Introduction -->
            <section id="intro" class="main">
                <div class="spotlight">
                    <div class="content">
                        <header class="major">
                            <h2>Transactions</h2>
                        </header>


                        <?php
                        // define the number of records per page
                        $records_per_page = 10;

                        // retrieve the current page number
                        if (isset($_GET['page']) && is_numeric($_GET['page'])) {
                            $current_page = $_GET['page'];
                        } else {
                            $current_page = 1;
                        }

                        // calculate the offset for the database query
                        $offset = ($current_page - 1) * $records_per_page;

                        // retrieve data from the database
                        $sql = "SELECT * FROM generated_data";

                        // check if sorting options are set
                        if (isset($_GET['order_by']) && isset($_GET['sort'])) {
                            $order_by = $_GET['order_by'];
                            $sort = $_GET['sort'];
                            $sql .= " ORDER BY $order_by $sort";
                        } else {
                            // default values if sorting options are not set
                            $order_by = 'UserName';
                            $sort = 'asc';
                            $sql .= " ORDER BY $order_by $sort";
                        }

                        // add limit and offset to the SQL query
                        $sql .= " LIMIT $records_per_page OFFSET $offset";

                        // execute the SQL query
                        $result = mysqli_query($con, $sql);

                        // display data in a table
                        echo "<table class='t'>";
                        echo "<tr>
<th style='padding-right: 2px;'>UserName <a href='?order_by=username&sort=asc'>▲</a> <a href='?order_by=username&sort=desc'>▼</a></th>
<th style='padding-right: 2px;'>Transaction ID</th>
<th style='padding-right: 2px;'>Invoice Number</th>
<th style='padding-right: 2px;'>Date of Transaction</th>
<th style='padding-right: 2px;'>Order ID</th>
<th style='padding-right: 2px;'>Amount Paid</th>
<th style='padding-right: 2px;'>Product Name</th>
</tr>";

                        // display data in the table
                        while ($row = mysqli_fetch_assoc($result)) {
                            echo "<tr>
  <td>" . $row['UserName'] . "</td>
  <td>" . $row['Transaction ID'] . "</td>
  <td>" . $row['Invoice Number'] . "</td>
  <td>" . $row['Date of Transaction'] . "</td>
  <td>" . $row['Order ID'] . "</td>
  <td>" . $row['Amount Paid'] . "</td>
  <td>" . $row['Product Name'] . "</td>
</tr>";
                        }
                        echo "</table>";

                        // get the total number of records in the database
                        $sql = "SELECT COUNT(*) AS total FROM generated_data";
                        $result = mysqli_query($con, $sql);
                        $row = mysqli_fetch_assoc($result);
                        $total_records = $row['total'];

                        // calculate the total number of pages
                        $total_pages = ceil($total_records / $records_per_page);

                        // display pagination links
                        echo "<div class='pagination'>";
                        for ($i = 1; $i <= $total_pages; $i++) {
                            echo "<a href='?page=$i'";
                            if ($i == $current_page) {
                                echo " class='active'";
                            }
                            echo ">$i</a>";
                        }
                        echo "</div>";
                        ?>



                        <div class="rainbow-line"></div>
                        <br>


                        <div class="t">
                            <?php
                            // Retrieve the latest transaction date for each user
                            $sql = "SELECT UserName, MAX(`Date of Transaction`) as LatestTransactionDate FROM generated_data GROUP BY UserName";
                            $result = mysqli_query($con, $sql);

                            // Define the number of results per page
                            $results_per_page = 10;

                            // Count the total number of results
                            $number_of_results = mysqli_num_rows($result);

                            // Calculate the total number of pages
                            $total_number_of_pages = ceil($number_of_results / $results_per_page);

                            // Determine the current page
                            if (!isset($_GET['page'])) {
                                $current_page = 1;
                            } else {
                                $current_page = $_GET['page'];
                            }

                            // Calculate the offset
                            $offset = ($current_page - 1) * $results_per_page;

                            // Retrieve the latest transaction dates for the current page
                            $sql_page = $sql . " LIMIT " . $offset . "," . $results_per_page;
                            $result_page = mysqli_query($con, $sql_page);

                            // Display the latest transaction dates in a table format
                            echo "<table>";
                            echo "<tr>
        <th>User Name</th>
        <th style='text-align:right'>Latest Transaction Date</th>
      </tr>";
                            while ($row = mysqli_fetch_assoc($result_page)) {
                                echo "<tr>
            <td style='font-size: 15px'>" . $row['UserName'] . "</td>
            <td style='font-size: 15px; font-weight: bold; text-align:right'>" . $row['LatestTransactionDate'] . "</td>
          </tr>";
                            }
                            echo "</table>";

                            // Display the pagination links
                            echo "<div class='pagination'>";
                            for ($i = 1; $i <= $total_number_of_pages; $i++) {
                                if ($i == $current_page) {
                                    echo "<span class='current-page'>" . $i . "</span>";
                                } else {
                                    echo "<a href='?page=" . $i . "'>" . $i . "</a>";
                                }
                            }
                            echo "</div>";
                            ?>
                        </div>









            </section>

            <!-- First Section -->
            <section id="first" class="main special">
                <header class="major">
                    <h2>Graphs</h2>
                </header>


                <div class="graph-container" style="border-top: 1px solid rgba(0, 0, 0, 0.1); border-bottom: 1px solid rgba(0, 0, 0, 0.1); margin: 20px 0; padding: 20px 0;">
                    <img src="aisle_graph.png" alt="Graph" style='max-width: 100%'>
                    <img src="cust_ord_graph.png" alt="Graph" style='max-width: 100%'>
                    <img src="dept_graph.png" alt="Graph" style='max-width: 100%'>
                    <img src="freq_dow_graph.png" alt="Graph" style='max-width: 100%'>
                    <img src="freq_graph.png" alt="Graph" style='max-width: 100%'>
                    <img src="top15_graph.png" alt="Graph" style='max-width: 100%'>
                </div>





                <footer class="major">
                    <ul class="actions special">
                        <li><a href="generic.html" class="button">Learn More</a></li>
                    </ul>
                </footer>
            </section>

            <!-- Second Section -->
            <section id="second" class="main special">
                <header class="major">
                    <h2>Recommendations</h2>
                    <p>Here are some AI Recommended Recommendations for You</p>
                </header>


















                <footer class="major">
                    <ul class="actions special">
                        <li><a href="generic.html" class="button">Learn More</a></li>
                    </ul>
                </footer>
            </section>

            <!-- Get Started -->
            <section id="cta" class="main special">
                <header class="major">
                    <h2>Log Out</h2>
                    <p>Thanks, Visit Again !</p>
                </header>
                <footer class="major">
                    <ul class="actions special">
                        <form method="post">
                            <input type="submit" name="logout" value="Log Out">
                        </form>
                    </ul>
                </footer>
            </section>

        </div>

        <!-- Footer -->
        <footer id="footer">
            <section>
                <h2>Aliquam sed mauris</h2>
                <p>Sed lorem ipsum dolor sit amet et nullam consequat feugiat consequat magna adipiscing tempus etiam
                    dolore veroeros. eget dapibus mauris. Cras aliquet, nisl ut viverra sollicitudin, ligula erat
                    egestas velit, vitae tincidunt odio.</p>
                <ul class="actions">
                    <li><a href="generic.html" class="button">Learn More</a></li>
                </ul>
            </section>
            <section>
                <h2>Etiam feugiat</h2>
                <dl class="alt">
                    <dt>Address</dt>
                    <dd>1234 Somewhere Road &bull; Nashville, TN 00000 &bull; USA</dd>
                    <dt>Phone</dt>
                    <dd>(000) 000-0000 x 0000</dd>
                    <dt>Email</dt>
                    <dd><a href="#">information@untitled.tld</a></dd>
                </dl>
                <ul class="icons">
                    <li><a href="#" class="icon brands fa-twitter alt"><span class="label">Twitter</span></a></li>
                    <li><a href="#" class="icon brands fa-facebook-f alt"><span class="label">Facebook</span></a></li>
                    <li><a href="#" class="icon brands fa-instagram alt"><span class="label">Instagram</span></a></li>
                    <li><a href="#" class="icon brands fa-github alt"><span class="label">GitHub</span></a></li>
                    <li><a href="#" class="icon brands fa-dribbble alt"><span class="label">Dribbble</span></a></li>
                </ul>
            </section>
        </footer>

    </div>



    <!-- Scripts -->
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/jquery.scrollex.min.js"></script>
    <script src="assets/js/jquery.scrolly.min.js"></script>
    <script src="assets/js/browser.min.js"></script>
    <script src="assets/js/breakpoints.min.js"></script>
    <script src="assets/js/util.js"></script>
    <script src="assets/js/main.js"></script>

</body>

</html>
