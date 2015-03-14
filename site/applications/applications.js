'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/applications', {
          templateUrl: 'applications/applications.html',
          controller: 'AppCtrl'
        });
}])

.controller('AppCtrl', ['$scope', function($scope) {
  $scope.mpg123 = '/usr/bin/mpg123';
  $scope.alsamixer = '/usr/bin/alsamixer';

  $scope.save = function () {
    // nothing to do yet
  };
}]);

