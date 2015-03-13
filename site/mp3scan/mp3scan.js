'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/mp3scan', {
    templateUrl: 'mp3scan/mp3scan.html',
  });
}])

