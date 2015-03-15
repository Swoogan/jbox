'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/player', {
    templateUrl: 'player/player.html',
    controller: 'PlayerCtrl'
  });
}])

.controller('PlayerCtrl', ['$scope', 'Songs', function($scope, Songs) {
  $scope.pattern = 'judy';
  $scope.songs = Songs.get();

  $scope.filter = function() {
    $scope.songs = Songs.get({pattern: $scope.pattern});
  };

  $scope.nowplaying = {
    'title': 'Absolutel',
    'artist': 'Headstones',        
    'bitrate': '128',        
    'frequency': '48',        
    'length': '2:36'
  };
}]);
 
