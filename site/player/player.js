'use strict';

/*globals angular*/

var jbox = angular.module('jbox');

jbox.config(['$routeProvider', function ($routeProvider) {
  $routeProvider.when('/player', {
    templateUrl: 'player/player.html',
    controller: 'PlayerController'
  });
}]);

jbox.controller('PlayerController', ['$scope', 'Songs', 'NowPlaying', 'Volume', 'Controls',
  function ($scope, Songs, NowPlaying, Volume, Controls) {
    $scope.pattern = '';
    $scope.songs = Songs.get();
    $scope.nowplaying = NowPlaying.get();

    $scope.grabbed = false;
    $scope.grabOffset = 0;
    $scope.lastChange = -1;

    var knob = document.getElementById('volume-index');
    var volume = Volume.get(function () {
      var level = volume.level; 
      var left = Math.floor((level / 100 * 210) + 5);
      knob.style.left = left + 'px'; 
    });

    $scope.filter = function () {
      $scope.songs = Songs.get({pattern: $scope.pattern});
    };

    $scope.volumeChange = function (e) {
      if ($scope.grabbed) {
        var left = e.clientX - $scope.grabOffset;
        left = Math.max(left, 5);
        left = Math.min(left, 215);

        knob.style.left = left + 'px';

        var level = Math.floor((left - 5) / 210 * 100);
        if (Math.abs($scope.lastChange - level) >= 2) {
          Volume.update({'level': level});
          // should put this in success
          $scope.lastChange = level;
        }
      }
    };

    $scope.volumeGrab = function (e) {
      $scope.grabbed = true;
      $scope.grabOffset = e.clientX - e.currentTarget.offsetLeft;
    };

    $scope.volumeRelease = function (e) {
      $scope.grabbed = false;
      $scope.grabOffset = 0;
    };

    $scope.control = function (command, id) {
      if (id) {
	Controls.save({'command': command, 'id': id});
      } else {
	Controls.save({'command': command});
      }
    };
}]);

jbox.factory('NowPlaying', ['$resource', function ($resource) {
  return $resource('/api/nowplaying', {});
}]);

jbox.factory('Volume', ['$resource', function ($resource) {
  return $resource('/api/volume', {}, {
    update: { method: 'PUT' }
  });
}]);

jbox.factory('Controls', ['$resource', function ($resource) {
  return $resource('/api/controls', {});
}]);
