(function() {
    'use strict';

    angular
        .module('app.dashboard')
        .config(configFunction);

    configFunction.$inject = ['$routeProvider'];

    function configFunction($routeProvider) {
        $routeProvider.when('/user/', {
            templateUrl: 'templates' + '/user_profile/dashboard.html',
            controller: 'dashboardController',
            controllerAs: 'vm',
           
        });
    }
});    