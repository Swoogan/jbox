'use strict';

/*globals angular*/

var jbox = angular.module('jbox');

jbox.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/mp3scan', {
    templateUrl: 'mp3scan/mp3scan.html',
  });
}]);

