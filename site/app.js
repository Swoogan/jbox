/*global angular*/

(function () {
    'use strict';

    var jbox = angular.module('jbox', [
	'ngRoute',
	'ngResource',
    ]);

    // Should move config to config.js ?

    jbox.config(Config);
    
    Config.$inject = ['$routeProvider'];

    function Config($routeProvider) {
	$routeProvider.otherwise({redirectTo: '/player'});
    }
}());
