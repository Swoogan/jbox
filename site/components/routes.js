(function () {
    'use strict';

    angular.module('jbox').config(Routes);

    Routes.$inject = ['$routeProvider'];

    function Routes($routeProvider) {
        $routeProvider
        .when('/config', {
            templateUrl: 'config/config.html',
        })
        .when('/player', {
            templateUrl: 'player/player.html',
            controller: 'PlayerController',
            controllerAs: 'player',
        }),
        .when('/applications', {
            templateUrl: 'applications/applications.html',
            controller: 'AppsController'
            controller: 'apps'
        });
    }
}());
