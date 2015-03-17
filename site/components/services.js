'use strict';

/*global angular*/

var jbox = angular.module('jbox');

jbox.factory('Songs', ['$resource', function ($resource) {
  return $resource('/api/songs/:pattern', {}, {});
}]);

