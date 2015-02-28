      function dragMouseMove(e) {
        var x = (e) ? e.pageX : event.clientX;
        var vbOffset = (e) ? dragObj.offsetWidth: dragObj.offsetWidth / 2;
        newLeft = x - document.getElementById('volumeBar').offsetLeft - vbOffset;
        if(newLeft < 0 || newLeft > 210 - dragObj.offsetWidth) return false;
        dragObj.style.left = newLeft;
        //console.log("index left: " + dragObj.style.left + " e.pageX: " + event.x);
        return false;
      }

      function dragMouseUp() {
        //dragObj = null;
        if(document.layers) document.releaseEvents(Event.MOUSEMOVE | Event.MOUSEUP);
        document.onmousemove = null;
        document.onmouseup = null;


        newleft = parseInt(dragObj.style.left)
        status = newleft;
        volume = (100 * newleft) / 225;
	location.href = 'volume.py?volume=' + parseInt(volume) + '&pixel=' + newleft
      }

      function dragMouseDown(e) {
        dragObj = this;
        if(document.layers) document.captureEvents(Event.MOUSEMOVE | Event.MOUSEUP);
        document.onmousemove = dragMouseMove;
        document.onmouseup = dragMouseUp;
        return false;
      }

