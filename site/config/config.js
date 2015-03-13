'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/config', {
    templateUrl: 'config/config.html',
  });
}])

