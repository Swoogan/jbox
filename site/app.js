'use strict';

// Declare app level module which depends on views, and components
var jbox = angular.module('jbox', [
  'ngRoute',
]);

jbox.config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/player'});
}]);
