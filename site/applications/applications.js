'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/applications', {
          templateUrl: 'applications/applications.html',
          controller: 'AppController'
        });
}])

.controller('AppController', ['$scope', 'Applications', function($scope, Applications) {
  $scope.apps = Applications.get();
  
  $scope.save = function () {
    Applications.update($scope.apps);
  };
}])

.factory('Applications', ['$resource', function($resource){
  return $resource('/api/applications', {}, {
    update: { method: 'PUT' }
  });
}]);
