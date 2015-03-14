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
    'recurse': 'true'
  }];
  $scope.path = '';
  $scope.recurse = true;

  $scope.addDirectory = function() {
    $scope.directories.push({'path': $scope.path, 'recurse': $scope.recurse});
  };  

  $scope.delDirectory = function() {
    var dir = $scope.directories;
    for (var i = dir.length - 1; i >= 0; i--) {
      if (dir[i].path === $scope.path) {
	dir.splice(i, 1);
      }
    }
    $scope.directories = dir;
  };  
}]);
 
