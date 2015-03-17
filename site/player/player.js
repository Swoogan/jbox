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

    $scope.filter = function () {
      $scope.songs = Songs.get({pattern: $scope.pattern});
    };

//    $scope.volumeChange = function(grabbed) {
    $scope.volumeChange = function () {
      console.log('move');
    };

    $scope.volumeGrab = function () {
      console.log('grab');
      $scope.grabbed = true;
    };

    $scope.volumeRelease = function () {
      console.log('release');
      $scope.grabbed = false;
    };
      /*
    $scope.volumeChange = function(e) {
      var x = (e) ? e.pageX : event.clientX;
      var vbOffset = (e) ? dragObj.offsetWidth: dragObj.offsetWidth / 2;
      newLeft = x - document.getElementById('volumeBar').offsetLeft - vbOffset;
      if(newLeft < 0 || newLeft > 210 - dragObj.offsetWidth) return false;
      dragObj.style.left = newLeft;
      //console.log("index left: " + dragObj.style.left + " e.pageX: " + event.x);
      return false;
    };

    $scope.volumeRelease = function() {
      //dragObj = null;
      if(document.layers) document.releaseEvents(Event.MOUSEMOVE | Event.MOUSEUP);
      document.onmousemove = null;
      document.onmouseup = null;

      newleft = parseInt(dragObj.style.left)
      status = newleft;
      volume = (100 * newleft) / 225;
      location.href = 'volume.py?volume=' + parseInt(volume) + '&pixel=' + newleft
    };

    $scope.volumeGrab = function() {
      $scope.grabbed = true;
      dragObj = e.currentTarget;
      if(document.layers) document.captureEvents(Event.MOUSEMOVE | Event.MOUSEUP);
      document.onmousemove = dragMouseMove;
      document.onmouseup = dragMouseUp;
      return false;
    };
    */
}]);

jbox.factory('NowPlaying', ['$resource', function ($resource) {
  return $resource('/api/nowplaying', {}, {});
}]);

jbox.factory('Volume', ['$resource', function ($resource) {
  return $resource('/api/volume', {}, {
    update: { method: 'PUT' }
  });
}]);

