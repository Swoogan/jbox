'use strict';

function clicked(qrystr, mode) {
  var lctn, cmd = '';

  if (mode === null) {
    mode = 0;
  }

  if (mode === 0) {
    cmd = 'parent.parent.frames.current.location.reload()';
  } else if (mode === 1) {
    lctn = 'scripts/';
    cmd = 'parent.frames.current.location.reload()';
  } else if (mode === 2) {
    lctn = 'scripts/';
  }

  location.href = lctn + 'controller.py?' + qrystr;
  setTimeout(cmd, 700);
}

