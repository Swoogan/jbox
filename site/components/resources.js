(function () {
    'use strict';

    angular
        .module('jbox')
        .factory('NowPlaying', NowPlaying);

    NowPlaying.$inject = ['$resource'];

    function NowPlaying($resource) {
        return $resource('/api/nowplaying');
    }

    ///

    angular
        .module('jbox')
        .factory('Volume', Volume);

    Volume.$inject = ['$resource'];

    function Volume($resource) {
        return $resource('/api/volume', {}, {
            update: {method: 'PUT'}
        });
    }

    ///

    angular
        .module('jbox')
        .factory('Controls', Controls);

    Controls.$inject = ['$resource'];

    function Controls($resource) {
        return $resource('/api/controls');
    }

    ///

    angular
        .module('jbox')
        .factory('Applications', Applications);

    Applications.$inject = ['$resource'];

    function Applications($resource) {
        return $resource('/api/applications', {}, {
            update: {method: 'PUT'}
        });
    }
}());
