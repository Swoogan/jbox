/*global angular*/

(function () {
    'use strict';

    angular.module('jbox', [
        'ngRoute',
        'ngResource',
    ]);

    // Should move config to config.js ?

    angular
        .module('jbox')
        .config(Config);

    Config.$inject = ['$routeProvider'];

    function Config($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/player'});
    }
}());
