<div class="side-menu sidebar-inverse">
    <nav class="navbar navbar-default" role="navigation">
        <div class="side-menu-container">
            <div class="navbar-header">
                <a class="navbar-brand" href="#">
                    <div class="icon fa fa-paper-plane"></div>
                    <div class="title">Stock Recommender</div>
                </a>
                <button type="button" class="navbar-expand-toggle pull-right visible-xs">
                    <i class="fa fa-times icon"></i>
                </button>
            </div>
            <ul class="nav navbar-nav">
                <li class="<?php echo $page=='dashboard'? 'active': '' ?>">
                    <a href="?page=dashboard">
                        <span class="icon fa fa-tachometer"></span><span class="title">Dashboard</span>
                    </a>
                </li>
                <li class="<?php echo $page=='trading_analytics'? 'active': '' ?>">
                    <a href="?page=trading_analytics">
                        <span class="icon fa fa-cubes"></span><span class="title">Trading Analytics</span>
                    </a>
                </li>
                <li class="<?php echo $page=='profile'? 'active': '' ?>">
                    <a href="?page=profile">
                        <span class="icon fa fa-user"></span><span class="title">Profile</span>
                    </a>
                </li>
            </ul>
        </div>
        <!-- /.navbar-collapse -->
    </nav>
</div>