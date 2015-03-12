'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/player', {
    templateUrl: 'player/player.html',
    controller: 'PlayerCtrl'
  });
}])

.controller('PlayerCtrl', ['$scope', '$http', function($scope, $http) {
  $http.get('/songs.json').success(function(data) {
    $scope.songs = data;
  });

  $scope.nowplaying = {
    'title': 'Absolutel',
    'artist': 'Headstones',        
    'bitrate': '128',        
    'frequency': '48',        
    'length': '2:36'
  };
}]);
 
