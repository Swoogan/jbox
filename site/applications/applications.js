'use strict';

/*global angular*/

var jbox = angular.module('jbox');

jbox.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/applications', {
    templateUrl: 'applications/applications.html',
    controller: 'AppController'
  });
}]);

jbox.controller('AppController', ['$scope', 'Applications', function ($scope, Applications) {
  $scope.apps = Applications.get();

  $scope.save = function () {
    Applications.update($scope.apps);
  };
}]);

jbox.factory('Applications', ['$resource', function ($resource) {
  return $resource('/api/applications', {}, {
    update: { method: 'PUT' }
  });
}]);
