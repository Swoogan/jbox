'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/applications', {
          templateUrl: 'applications/applications.html',
          controller: 'AppCtrl'
        });
}])

.controller('AppCtrl', ['$scope', '$http', function($scope, $http) {
  $http.get('/api/applications').success(function(data) {
    $scope.mpg123 = data.mpg123;
    $scope.alsamixer = data.alsamixer;
  });


  $scope.save = function () {
    $http.put('/api/applications', {'mpg123': $scope.mpg123, 'alsamixer': $scope.alsamixer});
  };
}]);

