'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/directories', {
    templateUrl: 'directories/directories.html',
    controller: 'DirectoryCtrl',
  });
}])

.controller('DirectoryCtrl', ['$scope', '$http', function($scope, $http) {
  $http.get('/api/directories').success(function(data) {
    $scope.directories = data;
  });

  $scope.path = '';
  $scope.recurse = true;

  $scope.addDirectory = function() {
    $scope.directories[$scope.path] = 'recurse';
    $http.put('/api/directories', $scope.directories);
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
 
