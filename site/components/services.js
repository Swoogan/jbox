'use strict';

angular.module('jbox')

.factory('Songs', ['$resource', function($resource){
  return $resource('/api/songs/:pattern', {}, {});
}]);

