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
        })
        .when('/applications', {
            templateUrl: 'applications/applications.html',
            controller: 'AppsController',
            controllerAs: 'apps',
        })
        .when('/directories', {
            templateUrl: 'directories/directories.html',
            controller: 'DirectoriesController',
            controllerAs: 'dirs',
        })
        .when('/mp3scan', {
            templateUrl: 'mp3scan/mp3scan.html',
        });
    }
}());
