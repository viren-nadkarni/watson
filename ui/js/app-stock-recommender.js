/**
* Main AngularJS Web Application
*/
var app = angular.module('stockRecommenderApp', ['ngAnimate', 'ui.bootstrap', 'angular-jqcloud']);

app.controller('GainersCtrl', function($scope, $http, StockSelected){
      $scope.parseFloat = function(value, keepSign)
    { 
        if(keepSign) {
          return parseFloat(value);
        }
        return parseFloat(value) > 0? parseFloat(value) : -parseFloat(value);
    }
  config = {};
  $http.get('http://119.81.196.131:8080/stocks/buy', config).then(
    function(response) {
      console.log(response);
      $scope.gainers_hot_positive = response.data;
    }, function(response) {
      console.log("Failed to get hot positive");
    }
  );
  $http.get('http://119.81.196.131:8080/stocks/active', config).then(
    function(response) {
      $scope.gainers_most_active = response.data;
    }, function(response) {
      console.log("Failed to get highest turnover");
    }
  );

  
  //$scope.gainers_hot_positive = ['Netease Inc. ADR', 'Tata Steel', 'Persistent Sys' ];
  //$scope.gainers_most_active = ["HDFC", "ICICI", "Sesa Goa", "GoDaddy Inc. Cl A" ];
});

app.controller('LosersCtrl', function($scope, $http, StockSelected){
      $scope.parseFloat = function(value, keepSign)
    {
              if(keepSign) {
          return parseFloat(value);
        }
      return parseFloat(value) > 0? parseFloat(value) : -parseFloat(value);
    }
  config = {};
  $http.get('http://119.81.196.131:8080/stocks/sell', config).then(
    function(response) {
      $scope.losers_hot_negative = response.data;
    }, function(response) {
      console.log("Failed to get hot positive");
    }
  );
  $http.get('http://119.81.196.131:8080/stocks/inactive', config).then(
    function(response) {
      $scope.losers_most_inactive = response.data;
    }, function(response) {
      console.log("Failed to get highest turnover");
    }
  );
  
  //$scope.gainers_hot_positive = ['j2 Global Inc.', '	InterNAP Corp.', 'IAC/InterActiveCorp.', 'HDS International Corp.'];
  //$scope.gainers_turnover = ["Federal Reserve", "Tata Steel", "firm", "Rs", "Rs", "BMC Budget"];
  
});

app.controller('WatchListCtrl', function($scope, $http, $timeout, StockSelected){
    $scope.StockSelected = StockSelected;
        $scope.parseFloat = function(value, keepSign)
    {
              if(keepSign) {
          return parseFloat(value);
        }
        return parseFloat(value) > 0? parseFloat(value) : -parseFloat(value);
    }
    var config = {};
    $scope.watchlist_symbol = [];
    var getWatchList = function() {
        //$scope.watchlist = [{symbol:'ADBE', quantity:1244, name: 'Adobe systems'}];
        
        $http.get('http://119.81.196.131:8080/watchlist', config).then(
            function(response) {
                $scope.watchlist = response.data;
                //$scope.watchlist = [{symbol:'ADBE', quantity:1244, name: 'Adobe systems'}];
                response.data.forEach(function(item){
                  $scope.watchlist_symbol.push(item.symbol);
                });
            }, function(response) {
              console.log("Failed to get watchlist");
            }
        );
        
    }
    getWatchList();
    //type ahead field
    $scope.getStocks = function(val) {
        return $http.get('http://trading-analytics-backend.mybluemix.net/demo/stocks/', {
          params: {
            input: val
          }
        }).then(function(response){
            console.log(response);
          return response.data.map(function(item){
            return item.Symbol + ' - '+ item.Name;
          });
        });
    };
    
    $scope.submitWatchlist = function() {

        var symbol = $scope.stockSelectedTypeahead.substring(0, $scope.stockSelectedTypeahead.indexOf(' - '));
        $scope.watchlist_symbol.push(symbol);
        var postData = {watchlist: $scope.watchlist_symbol};

        return $http.post('http://119.81.196.131:8080/watchlist', postData).then(function(response){
            console.log(response);
            getWatchList();
            $scope.stockSelectedTypeahead = '';
        }, function(response) {
            console.log(response);
        });
    };
    
    $scope.tagCloudStocks = [  
          {text: "Netease Inc. ADR", weight: 13,  link: "{{console.log($scope)}}"},
{text: "Tata Steel", weight: 10.5,  link: "{{console.log(scope)}}"},
          {text: "Persistent Sys", weight: 9.4},
          {text: "Sit", weight: 8},
          {text: "Amet", weight: 6.2},
          {text: "Consectetur", weight: 5},
          {text: "Adipiscing", weight: 5}];
});

app.controller('StockDetailsCtrl', function($scope, $rootScope, $http, StockSelected) {
    config = {};
        $scope.parseFloat = function(value, keepSign)
    {
              if(keepSign) {
          return parseFloat(value);
        }
        return parseFloat(value) > 0? parseFloat(value) : -parseFloat(value);
    }
    /*
  $http.get('http://119.81.196.131:8080/stocks/hot', config).then(
    function(response) {
      $scope.gainers_hot_positive = response.data;
    }, function(response) {
      console.log("Failed to get stock details");
    }
  );
    
  $http.get('http://119.81.196.131:8080/stocks/hot', config).then(
    function(response) {
      $scope.gainers_hot_positive = response.data;
    }, function(response) {
      console.log("Failed to get chart details");
    }
  );
  */
    //$scope.symbol = StockSelected.getSymbol();
    //console.log($scope.symbol);
    $scope.name = '';
    $scope.$watch(function() {
      return $rootScope.stock;
    }, function() {
      $scope.symbol = $rootScope.stock;
        if($scope.symbol) {
            new Markit.InteractiveChartApi($scope.symbol,90);
            new Markit.QuoteService($scope.symbol, function(jsonResult) {

                //Catch errors
                if (!jsonResult || jsonResult.Message){
                    console.error("Error: ", jsonResult.Message);
                    return;
                }

                //If all goes well, your quote will be here.
                console.log(jsonResult);

                //Now proceed to do something with the data.
                $("#stockName").text(jsonResult.Name);
                //console.log($scope);
                console.log(jsonResult.Name);

            });
        }

    }, true);
    

    
});

app.controller('NeutralCtrl', function($scope, $http, StockSelected){
      $scope.parseFloat = function(value, keepSign)
    { 
        if(keepSign) {
          return parseFloat(value);
        }
        return parseFloat(value) > 0? parseFloat(value) : -parseFloat(value);
    }
  config = {};
  $http.get('http://119.81.196.131:8080/stocks/hold', config).then(
    function(response) {
      console.log(response);
      $scope.gainers_hot_positive = response.data;
    }, function(response) {
      console.log("Failed to get hold");
    }
  );

});
app.factory('StockSelected', function () {
    var stock = {
        name: false,
        symbol: false,
    };
    return {
        getSymbol: function () {
            return stock.symbol;
        },
        setSymbol: function (symbol) {
            stock.symbol = symbol;
        }
    };
    
});



