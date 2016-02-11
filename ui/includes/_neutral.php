<div class="col-xs-12" ng-controller="NeutralCtrl">
  <div class="card">
      <!--<div class="card-header">
          <div class="card-title">
            <div class="title">Positive Trend</div>
          </div>
      </div>-->
      <div class="card-body">
        <div class="row">
            <div class="col-sm-6">
                <div class="sub-title">Stocks to hold on to<span class="description"> </span></div>
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th>Symbol</th>
                            <th>Sentiment</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr ng-repeat="stock in gainers_hot_positive | limitTo:5 track by $index " ng-click="$root.stock=stock[0];" class="clickable-row">
                            <th scope="row">{{stock[0]}}</th>
                            <td><!--
                              <div class="progress">
                                <div title="{{parseFloat(stock[1])*100}}%"  style="width: {{parseFloat(stock[1])*100}}%" aria-valuemax="100" aria-valuemin="0" aria-valuenow="80" role="progressbar" class="progress-bar progress-bar-success">
                                    <span class="sr-only">{{parseFloat(stock[1])*100}}% Complete</span>
                                </div>
                              </div>-->
                              No buzz found
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
      </div>
  </div>
      
</div>