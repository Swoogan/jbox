'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/directories', {
    templateUrl: 'directories/directories.html',
  });
}])

