(function () {
    'use strict';

    angular
        .module('jbox')
        .controller('AppsController', AppsController);

    AppsController.$inject = ['$scope', 'Applications'];

    function AppsController($scope, Applications) {
        var vm = this;

        vm.save = save;
        vm.mixerPath = '';

        function save() {
            Applications.update(vm.apps);
        }

        ///

        Applications.get(function (apps) {
            vm.mixerPath = apps.mixerPath;
        });
    }
}());
