<nav class="navbar navbar-default navbar-fixed-top navbar-top">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-expand-toggle">
                <i class="fa fa-bars icon"></i>
            </button>
            <ol class="breadcrumb navbar-breadcrumb">
                <li class="active"><?php echo $page_title ?></li>
            </ol>
            <button type="button" class="navbar-right-expand-toggle pull-right visible-xs">
                <i class="fa fa-th icon"></i>
            </button>
        </div>
        <ul class="nav navbar-nav navbar-right">
            <!--<button type="button" class="navbar-right-expand-toggle pull-right visible-xs">
                <i class="fa fa-times icon"></i>
            </button>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><i class="fa fa-comments-o"></i></a>
                <ul class="dropdown-menu animated fadeInDown">
                    <li class="title">
                        Notification <span class="badge pull-right">0</span>
                    </li>
                    <li class="message">
                        No new notification
                    </li>
                </ul>
            </li> -->
            <li class="dropdown danger">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><i class="fa fa-star-half-o"></i> 3</a>
                <ul class="dropdown-menu danger  animated fadeInDown">
                    <li class="title">
                        Notification <span class="badge pull-right">4</span>
                    </li>
                    <li>
                        <ul class="list-group notifications">
                            <a href="#">
                                <li class="list-group-item">
                                     <i class="fa fa-check icon"></i> GOOG is trending positively
                                </li>
                            </a>
                            <a href="#">
                                <li class="list-group-item">
                                     <i class="fa fa-comments icon"></i> AMZN is trending negatively
                                </li>
                            </a>
                            <a href="#">
                                <li class="list-group-item">
                                     <i class="fa fa-comments icon"></i> AAPL is trending negatively
                                </li>
                            </a>
                            <a href="#">
                                <li class="list-group-item message">
                                    view all
                                </li>
                            </a>
                        </ul>
                    </li>
                </ul>
            </li>
            <li class="dropdown profile">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">John Doe<span class="caret"></span></a>
                <ul class="dropdown-menu animated fadeInDown">
                    <li class="profile-img">
                        <img src="../img/profile/picjumbo.com_HNCK4153_resize.jpg" class="profile-img">
                    </li>
                    <li>
                        <div class="profile-info">
                            <h4 class="username">John Doe</h4>
                            <p>jdoe@example.com</p>
                            <div class="btn-group margin-bottom-2x" role="group">
                                <button type="button" class="btn btn-default"><i class="fa fa-user"></i> Profile</button>
                                <button type="button" class="btn btn-default"><i class="fa fa-sign-out"></i> Logout</button>
                            </div>
                        </div>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</nav>
