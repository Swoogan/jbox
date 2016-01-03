(function () {
    'use strict';

    angular
        .module('jbox')
        .controller('DirectoriesController', DirectoriesController);

    DirectoriesController.$inject = ['$log', 'Directories'];

    function DirectoriesController($log, Directories) {
        var vm = this;

        vm.addDirectory = addDirectory;
        vm.delDirectory = delDirectory;
        vm.directories = Directories.get();
        vm.path = '';
        vm.recurse = true;

        function addDirectory() {
            vm.directories[vm.path] = vm.recurse;
            Directories.update(vm.directories);
        }

        function delDirectory(path) {
            delete vm.directories[path];
            $log.log(path);

            // for (var i = dirs.length - 1; i >= 0; i--) {
            //     if (dirs[i].path === $scope.path) {
            //         dirs.splice(i, 1);
            //     }
            // }

            Directories.update(vm.directories);
        }
    }
}());
