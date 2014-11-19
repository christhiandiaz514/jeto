function DomainControllerListController($scope, $routeParams, DomainControllers, $http, $location, createDialog) {
    $scope.update = function() {
        DomainControllers.get({}, function(infos) {
            $scope.domain_controllers = infos.domain_controllers;
            $scope.domain_controllers.sort(function(a, b){ return a.name > b.name; });
            $scope.resource = infos;
            $('.loading').hide();
        });
    };

    $scope.update();
    $scope.resetInfos = function(){
       setTimeout($scope.update, 100);
       $scope.domain_controllerInfo = {
           'name': '',
           'address': '',
           'port': '',
           'accept_self_signed': false,
       };
    };

    $scope.resetInfos();

    $scope.create = function() {
        createDialog('/partials/admin/domainController/form.html',{
           id : 'createDialog',
           title: 'Add a new domain controller',
           backdrop: true,
           scope: $scope,
           success: {
               label: 'Add',
               fn: function(){
                   $('.loading').show();
                   var domain_controller = new DomainController();
                   domain_controller.name = $scope.projectInfo.name;
                   domain_controller.state = 'create';
                   domain_controller.$save();
                   setTimeout($scope.resetInfos, 100);
               }
           },
           cancel: {
               label: 'Cancel',
           },
        });
    };

    $scope.delete = function(item) {
        $scope.deleteItemId = item.id;
        createDialog({
            id : 'deleteDialog',
            title: 'Delete domain controller',
            backdrop: true,
            scope: $scope,
            btntype: 'danger',
            template: 'Are you sure you want to delete <b>' + item.name +'</b> ?',
            success: {
                label: 'Delete',
                fn: function(){
                    $('.loading').show();
                    id = $scope.deleteItemId;
                    $http.delete('/api/domainController/' + id)
                    .success(function() {
                        setTimeout($scope.update, 100);
                    });
                }
            },
            cancel: {
                label: 'Cancel',
            },
        });
    };
}

function DomainControllerController($scope, $routeParams, DomainControllers, $http, $location, $log) {
    $scope.update = function() {
        DomainControllers.get({id: $routeParams.id}, function(infos) {
            $scope.domain_controller = infos;
            $scope.resource = infos;
        });
    };

    $scope.update();
    $scope.resetInfos = function(){
       setTimeout($scope.update, 100);
    };
}
