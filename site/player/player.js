(function () {
    'use strict';

    angular.module('jbox').controller('PlayerController', PlayerController);

    PlayerController.$inject = ['$document', '$interval', '$scope', 'Songs', 'NowPlaying', 'Volume', 'Controls'];

    function PlayerController($document, $interval, $scope, Songs, NowPlaying, Volume, Controls) {
        var vm = this,
            knob = $document.getElementById('volume-index');

        /* knob above hints that there should be a directive for the volume control */
        
        vm.grabbed = false;
        vm.grabOffset = 0;
        vm.lastChange = -1;
        vm.nowplaying = NowPlaying.get();
        vm.pattern = '';
        vm.songs = Songs.get();

        function checkNowPlaying() {
            NowPlaying.get(function (data) {
                if (data.id !== vm.nowplaying.id) {
                    $scope.nowplaying = data;
                }
            });
        }

        function control(command, id) {
            if (id !== undefined) {
                Controls.save({'command': command, 'id': id});
            } else {
                Controls.save({'command': command});
            }
        }

        function filter() {
            vm.songs = Songs.get({pattern: vm.pattern});
        }

        /// volume

        Volume.get(function (volume) {
            var level = volume.level; 
            var left = Math.floor((level / 100 * 210) + 5);
            knob.style.left = left + 'px'; 
        });

        function volumeChange(e) {
            if (vm.grabbed) {
                var left = e.clientX - vm.grabOffset;
                left = Math.max(left, 5);
                left = Math.min(left, 215);

                knob.style.left = left + 'px';

                var level = Math.floor((left - 5) / 210 * 100);
                if (Math.abs(vm.lastChange - level) >= 2) {
                    Volume.update({'level': level});
                    // should put this in success
                    vm.lastChange = level;
                }
            }
        }

        function volumeGrab(e) {
            vm.grabbed = true;
            vm.grabOffset = e.clientX - e.currentTarget.offsetLeft;
        }

        function volumeRelease(e) {
            vm.grabbed = false;
            vm.grabOffset = 0;
        }

        /// volume en

        ///

        $interval(checkNowPlaying, 2000);
    }
}());
