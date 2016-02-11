<?php
$page_title="Dashboard";
$trading_analytics_host = "http://trading-analytics-backend.mybluemix.net";
$user = array("email"=>"jdoe@example.com", "name"=>"John Doe", "twitterId"=>"john_doe");
?>
<!DOCTYPE html>
<html ng-app="stockRecommenderApp">

<head>
    <title>Stock Recommender</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Fonts -->
    <link href='http://fonts.googleapis.com/css?family=Roboto+Condensed:300,400' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Lato:300,400,700,900' rel='stylesheet' type='text/css'>
    <!-- CSS Libs -->
    <link rel="stylesheet" type="text/css" href="../bower_components/bootstrap/dist/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="../bower_components/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="../bower_components/animate.css/animate.min.css">
    <link rel="stylesheet" type="text/css" href="../bower_components/bootstrap-switch/dist/css/bootstrap3/bootstrap-switch.min.css">
    <link rel="stylesheet" type="text/css" href="../bower_components/checkbox3/dist/checkbox3.min.css">
    <link rel="stylesheet" type="text/css" href="../bower_components/datatables/media/css/jquery.dataTables.min.css">
    <link rel="stylesheet" type="text/css" href="../bower_components/datatables/media/css/dataTables.bootstrap.css">
    <link rel="stylesheet" type="text/css" href="../bower_components/select2/dist/css/select2.min.css">
    <!-- CSS App -->
    <link rel="stylesheet" type="text/css" href="../css/style.css">
    <link rel="stylesheet" type="text/css" href="../css/bluemix.css">
    <link rel="stylesheet" type="text/css" href="../css/themes/flat-blue.css">
    <link rel="stylesheet" type="text/css" href="../bower_components/jqcloud2/dist/jqcloud.css">
    <style> 
    .hide {
      display:none;
    }
    </style>
</head>
<?php 
  $page = isset($_GET['page']) ? $_GET['page'] : "dashboard";
  switch($page) {
    case 'dashboard':
      $page_title = "Dashboard";
      $content = '../includes/dashboard.php';
      break;
    case 'profile':
      $page_title = "Profile";
      $content = '../includes/profile.php';
      break;
    case 'stocks':
      $page_title = "Stocks";
      $content = '../includes/stock_details.php';
      break;
    case 'trading_analytics':
      $page_title = "Trading Analytics";
      $content = '../includes/trading_analytics.php';
      break;
    default:
    $page_title = "Page Not Found";
      $content = '../includes/404.php';
      
  } ?>
              
<body class="flat-blue">
    <div class="app-container">
        <div class="row content-container">
            <?php include_once('../includes/header.php'); ?>
            <?php include_once('../includes/sidebar.php'); ?>
            <!-- Main Content -->
            <div class="container-fluid">
              <div class="side-body padding-top" id="main_content">
                <?php include_once($content); ?>
              </div>
            </div>
        </div>
        <?php include_once('../includes/footer.php'); ?>
        <div>
            <!-- Javascript Libs -->
                        <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
  <script src="//code.jquery.com/jquery-1.10.2.js"></script>
  <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
            
            <!--<script type="text/javascript" src="../bower_components/jquery/dist/jquery.min.js"></script>-->
            <script type="text/javascript" src="../bower_components/bootstrap/dist/js/bootstrap.min.js"></script>
            <script type="text/javascript" src="../bower_components/Chart.js/Chart.min.js"></script>
            <script type="text/javascript" src="../bower_components/bootstrap-switch/dist/js/bootstrap-switch.min.js"></script>
            <script type="text/javascript" src="../bower_components/matchHeight/jquery.matchHeight-min.js"></script>
            <script type="text/javascript" src="../bower_components/datatables/media/js/jquery.dataTables.min.js"></script>
            <script type="text/javascript" src="../bower_components/datatables/media/js/dataTables.bootstrap.min.js"></script>
            <script type="text/javascript" src="../bower_components/select2/dist/js/select2.full.min.js"></script>
            <script type="text/javascript" src="../bower_components/ace-builds/src/ace.js"></script>
            <script type="text/javascript" src="../bower_components/ace-builds/src/mode-html.js"></script>
            <script type="text/javascript" src="../bower_components/ace-builds/src/theme-github.js"></script>
            <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.9/angular.min.js"></script>
            <script src="../bower_components/angular-animate/angular-animate.js"></script>
            <script src="../bower_components/angular-bootstrap/ui-bootstrap.min.js"></script>
            <script src="../bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js"></script>
            <script src="../bower_components/jqcloud2/dist/jqcloud.js"></script>
            <script src="../bower_components/angular-jqcloud/angular-jqcloud.js"></script>
            <script src="https://code.highcharts.com/stock/highstock.js"></script>
            <script src="https://code.highcharts.com/stock/modules/exporting.js"></script>
            
            
            
            <!--<script src="../bower_components/bootstrap3-typeahead/bootstrap3-typeahead.min.js"></script>-->
            
            <script type="text/javascript" src="../js/app-stock-recommender.js"></script>
            <!-- Javascript -->
            <script type="text/javascript" src="../js/app.js"></script>
            <script type="text/javascript" src="../js/MarkitTimeseriesServiceSample.js"></script>
            <script type="text/javascript" src="../js/MarkitQuoteServiceSample.js"></script>
            
            <?php if($page=="dashboard") {?>
            
              <script type="text/javascript" src="../js/index.js"></script>
            <?php } ?>
            <?php if($page="trading_analysis") { ?>
            <script type="text/javascript" src="http://ta-cdn.mybluemix.net/v1/TradeoffAnalytics.js"></script>
              <script>
              (function(){
                var ta;
                //var problemPath = '../data/tradeoff.json';
                var problemPath = 'http://119.81.196.131:8080/tradeoff';
                function onPageLoad() {
                  $('.loading').show();
                  
                  ta = loadTradeoffAnalytics('ta', onTAReady);
                }
                
                function loadTradeoffAnalytics(node, callback) {
                  
                  var taClient = new TradeoffAnalytics({
                      dilemmaServiceUrl: '<?php echo $trading_analytics_host ?>/demo/dilemmas',
                  }, node);
                  taClient.start(callback);
                  return taClient;
                }

                function onTAReady() {
                  $.getJSON(problemPath, function(problem) {
                    ta.show(problem.problem, function () {
                      $('.loading', ta.node).hide();
                      ta.resize();
                    });
                  });
                }

                  $(document).ready(onPageLoad);
              })();
              </script>
            <?php } ?>
</body>

</html>
