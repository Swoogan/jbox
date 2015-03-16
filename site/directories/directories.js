'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/directories', {
    templateUrl: 'directories/directories.html',
    controller: 'DirectoriesController',
  });
}])

.controller('DirectoriesController', ['$scope', 'Directories', function($scope, Directories) {
  $scope.directories = Directories.get();
  $scope.path = '';
  $scope.recurse = true;

  $scope.addDirectory = function() {
    $scope.directories[$scope.path] = $scope.recurse;
    Directories.update($scope.directories);
  };  

  $scope.delDirectory = function(path) {
    delete $scope.directories[path];
    console.log(path);

//    for (var i = dirs.length - 1; i >= 0; i--) 
//      if (dirs[i].path === $scope.path)
//	dirs.splice(i, 1);

    Directories.update($scope.directories);
  };  
}])

.factory('Directories', ['$resource', function($resource){
  return $resource('/api/directories', {}, {
    update: { method: 'PUT' }
  });
}]);

