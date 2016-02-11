<div class="row" ng-show="$root.stock" ng-controller="StockDetailsCtrl">
    <div class="col-xs-12">
        <div class="card">
          <div class="card-header">
              <div class="card-title">
                <div class="title">{{symbol}} - <span id="stockName"></span></div>
              </div>
          </div>
            <div class="card-body no-padding">
                <div id="chartDemoContainer" style="height: 400px; min-width: 310px"></div>
            </div>
        </div>
        <div class="card">
          <div class="card-header">
              <div class="card-title">
                <div class="title">News Source </div>
              </div>
          </div>
            <div class="card-body no-padding">
                <div>
                    <div class="list-group">
                        <a class="list-group-item" target="_blank" href="http://www.moneycontrol.com/news/cnbc-tv18-comments/googles-pichai-microsofts-nadella-to-visit-indiadec_4448561.html?utm_source=ref_article">
                             Google's Pichai, Microsoft's Nadella to visit India in Dec
                        </a>
                        <a class="list-group-item" target="_blank" href="http://www.moneycontrol.com/news/world-news/googles-internet-beaming-balloons-to-take-offindonesia_3845681.html?utm_source=ref_article">
                             Google's Internet-beaming balloons to take off in Indonesia
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>