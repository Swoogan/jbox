(function () {
    'use strict';

    /*global angular*/

    angular.module('jbox').config(Routes);
    
    Routes.$inject = ['$routeProvider'];

    function Routes($routeProvider) {
        $routeProvider
        .when('/config', {
            templateUrl: 'config/config.html',
        })
        .when('/player', {
            templateUrl: 'player/player.html',
            controller: 'PlayerController'
        });

    }
}());
