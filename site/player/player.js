'use strict';

angular.module('jbox')

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/player', {
    templateUrl: 'player/player.html',
    controller: 'PlayerController'
  });
}])

.controller('PlayerController', ['$scope', 'Songs', 'NowPlaying',  function($scope, Songs, NowPlaying) {
  $scope.pattern = '';
  $scope.songs = Songs.get();
  $scope.nowplaying = NowPlaying.get();

  $scope.filter = function() {
    $scope.songs = Songs.get({pattern: $scope.pattern});
  };
}])

.factory('NowPlaying', ['$resource', function($resource){
  return $resource('/api/nowplaying', {}, {});
}]);

 
