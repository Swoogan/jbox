'use strict';

/*globals angular*/

var jbox = angular.module('jbox');

jbox.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/player', {
    templateUrl: 'player/player.html',
    controller: 'PlayerController'
  });
}]);

jbox.controller('PlayerController', ['$scope', 'Songs', 'NowPlaying', 'Volume',
  function ($scope, Songs, NowPlaying, Volume) {
    $scope.pattern = '';
    $scope.songs = Songs.get();
    $scope.nowplaying = NowPlaying.get();
    $scope.volume = Volume.get();
    $scope.grabbed = false;
    $scope.grabOffset = 0;

    $scope.filter = function () {
      $scope.songs = Songs.get({pattern: $scope.pattern});
    };

    $scope.volumeChange = function (e) {
      if ($scope.grabbed) {
        var left = e.clientX - $scope.grabOffset;
	if (left < 10) left = 10;
        if (left > 205) left = 205;
	var knob = document.getElementById('volume-index');
        knob.style.left = left + 'px';
        var level = Math.floor(left/210 * 100);
        Volume.update({'level': level});
      }
    };

    $scope.volumeGrab = function (e) {
      $scope.grabbed = true;
      $scope.grabOffset = e.clientX - e.currentTarget.offsetLeft;
    };

    $scope.volumeRelease = function (e) {
      $scope.grabbed = false;
      $scope.grabOffset = 0;
      var left = parseInt(e.currentTarget.offsetLeft); 
      var level = Math.floor(left/210 * 100);
      Volume.update({'level': level});
    };
}]);

jbox.factory('NowPlaying', ['$resource', function ($resource) {
  return $resource('/api/nowplaying', {}, {});
}]);

jbox.factory('Volume', ['$resource', function ($resource) {
  return $resource('/api/volume', {}, {
    update: { method: 'PUT' }
  });
}]);

