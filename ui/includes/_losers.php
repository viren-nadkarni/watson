<div class="col-xs-12" ng-controller="LosersCtrl">
  <div class="card">
      <!--<div class="card-header">
          <div class="card-title">
            <div class="title">Negative Trend</div>
          </div>
      </div>-->
      <div class="card-body">
        <div class="row">
            <div class="col-sm-6">
                <div class="sub-title">In the news<span class="description">Stocks that are in the news for NO good reason </span></div>
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th>Symbol</th>
                            <th>Sentiment</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr ng-repeat="stock in losers_hot_negative  | limitTo:5 track by $index" ng-click="$root.stock=stock[0];" class="clickable-row">
                            <th scope="row">{{stock[0]}}</th>
                            <td>
                            <div class="progress">
                                <div title="{{parseFloat(stock[1])*100}}%" style="width: {{parseFloat(stock[1])*100}}%" aria-valuemax="100" aria-valuemin="0" aria-valuenow="80" role="progressbar" class="progress-bar progress-bar-danger">
                                    <span class="sr-only">{{parseFloat(stock[1])*100}}% Complete </span>
                                </div>
                            </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="col-sm-6">
                <div class="sub-title">Least Traded Stocks <span class="description"></span></div>
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th>Symbol</th>
                            <th>Quantity Traded</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr ng-repeat="stock in losers_most_inactive  | limitTo:5 track by $index" ng-click="$root.stock=stock[0];" class="clickable-row">
                            <th scope="row">{{stock[0]}}</th>
                            <td>
                              {{stock[1]}}     
                            </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
      </div>
  </div>
      
</div>