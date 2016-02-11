<div class="col-xs-12" ng-controller="WatchListCtrl">
  <div class="card">
      <!--<div class="card-header">

          <div class="card-title">
          <div class="title">My Watchlist </div>
          </div>
          
      </div> -->
      <div class="card-body" id="watchlist-list">
          <div class="row">
              <div class="col-sm-6 col-md-6">
                  <!--<div class="sub-title">Contextual classes <span class="description">( .active , .success , .info , .warning , .danger )</span></div>-->
                  <form class=" form-inline col-md-12" ng-submit="submit()">
                      <div class="form-group">
                            <input type="text" style="width:430px;" ng-model="stockSelectedTypeahead" placeholder="Search.." uib-typeahead="stock for stock in getStocks($viewValue)" typeahead-loading="loadingStocks" typeahead-no-results="noResults" class="form-control">
                            <i ng-show="loadingStocks" class="glyphicon glyphicon-refresh"></i>
                      </div>
                      <input class="btn btn-default" type="submit" ng-click="submitWatchlist()" value="Add"/>
                  </form>
                  <table class="table table-striped table-hover">
                      <thead>
                          <tr>
                              <th>Stock</th>
                              <th>Symbol</th>
                              <th>Quantity Traded</th>
                              <th>Sentiment</th>
                          </tr>
                      </thead>
                      <tbody>
                          <tr ng-repeat="stock in watchlist track by $index" ng-click="$root.stock=stock.symbol;" class="clickable-row">
                              <td scope="row">{{stock.name}}</td>
                              <td scope="row">{{stock.symbol}}</td>
                              <td scope="row">{{stock.quantity}}</td>
                              <!--<td><div class="circle {{stock.state >0? 'green': 'red'}}" style="opacity: {{stock.state>0?stock.state: -stock.state }}">&nbsp;</div></td> -->
                              <td>
                              <!--<div class="circle {{stock.buzz == 'positive' ? 'green': stock.buzz == 'neutral'? 'grey': 'red'}}">&nbsp;</div>-->
                                <div class="progress">
                                  <div title="{{parseFloat(stock.buzz_factor)*100}}%" style="width: {{parseFloat(stock.buzz_factor)*100}}%" aria-valuemax="100" aria-valuemin="0" aria-valuenow="80" role="progressbar" class="progress-bar progress-bar-{{parseFloat(stock.buzz_factor, true) < 0 ? 'danger':'success'}}">
                                      <span class="sr-only">{{parseFloat(stock[1])*100}}% Complete</span>
                                  </div>
                                </div>
                              </td>
                          </tr>
                      </tbody>
                  </table>
              </div>
              <!--
              <div class="col-sm-6 col-md-6">
                  <jqcloud words="tagCloudStocks" width="500" height="350" steps="7" handlers="{click: function() { alert('it worked for'); }}"></jqcloud>
              </div>
              -->
          </div>
      </div>
  </div>
  

</div>