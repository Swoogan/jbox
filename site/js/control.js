      <!--
      function clicked(qrystr, mode){
        if(mode == null) mode = 0;

        if(mode == 0){
          lctn = '';
          cmd = 'parent.parent.frames.current.location.reload()';
        }
        else if (mode == 1){
          lctn = 'scripts/';
          cmd = 'parent.frames.current.location.reload()';
        }
        else if (mode == 2){
          lctn = 'scripts/';
          cmd = '';
        }

        location.href = lctn + 'controller.py?' + qrystr;
        setTimeout(cmd,700);
      }
      //-->      

