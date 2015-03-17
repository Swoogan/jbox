'use strict';

/*global angular*/

var jbox = angular.module('jbox');

jbox.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/config', {
    templateUrl: 'config/config.html',
  });
}]);

