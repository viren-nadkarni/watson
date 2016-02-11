<?php $page_title = "Profile" ?>
<div class="row">
    <div class="col-xs-12">
        <div class="card">
            <div class="card-header">
                <div class="card-title">
                    <div class="title">User Information</div>
                </div>
            </div>
            <div class="card-body">
                <form class="form-horizontal">
                    <div class="form-group">
                        <label class="col-sm-2 control-label " for="inputEmail3">Email</label>
                        <div class="col-sm-10">
                            <input type="email" placeholder="Email" id="inputEmail3" class="form-control disabled" disabled value="<?php echo $user['email'] ?>"> 
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="inputEmail3">Name</label>
                        <div class="col-sm-10">
                            <input type="text" placeholder="Name" id="name" class="form-control" value="<?php echo $user['name'] ?>">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" for="inputEmail3">Twitter username</label>
                        <div class="col-sm-10">
                            <input type="text" placeholder="twitterId" id="twitterId" class="form-control" value="<?php echo $user['twitterId'] ?>">
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="col-sm-offset-2 col-sm-10">
                            <button class="btn btn-default" type="submit">Save</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>