'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/directories', {
    templateUrl: 'directories/directories.html',
    controller: 'DirectoryCtrl',
  });
}])

.controller('DirectoryCtrl', ['$scope', function($scope) {
  $scope.directories = [{
    'path': '/home/swoogan/Software/development/jbox/mp3s',
    'recurse': 'Y'
  }];
}]);
 
