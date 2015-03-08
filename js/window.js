function UA(){
  var v = navigator.appVersion.toLowerCase(), u = navigator.userAgent.toLowerCase(), n = navigator.appName;
  this.mac = (v.indexOf("mac")+1);
  this.win = (v.indexOf("win")+1);
  this.nn = (n == "Netscape");
  this.ie = (n == "Microsoft Internet Explorer");
  this.aol = (u.indexOf("aol")+1);
  this.opera = (u.indexOf("opera")+1);
  this.ver = (this.ie) ? parseFloat(v.split('msie ')[1]) : parseFloat(v);
  this.v4 = (parseInt(v) == 4);
  this.os = (this.mac) ? 'mac' : (this.win) ? 'win' : navigator.platform;
  this.name = (this.nn) ? 'nn' : (this.ie) ? 'ie' : n;
  this.codeName = this.name +'_'+ parseInt(this.ver) + '_'+ this.os;
}
var ua = new UA();

function getWidth(width) {
  var args = getWidth.arguments;
    if(args[1]) {
      if(ua.mac) {
        if(ua.ie && ua.v4) width += 2;
        if(ua.nn) width += 17;
      }
      if(ua.win) {
        width += 16;
        if(ua.aol) width += 20;
      }
    }
    else {
      if(ua.mac) {
      if(ua.ie && ua.v4) width -= 17;
    }
    if(ua.win) {
      if(ua.aol) width += 20;
    }
  }
  return width;
}

function getHeight(height) {
  var args = getHeight.arguments;
    if(args[1]) {
      if(ua.mac) {
        if(ua.ie && ua.v4) height -= 15;
      }
      if(ua.win) {
        if(ua.aol) height += 20;
      }
    }
    else {
      if(ua.mac) {
        if(ua.ie && ua.v4) height -= 15;
      }
      if(ua.win) {
        if(ua.aol) height += 20;
      }
    }
  return height;
}

function remoteOpen(file,width,height) {
  var remote = window.open(file,'remote','width='+getWidth(width)+',height='+getHeight(height)+',top=0,left=0,directories=0',null);
  remote.focus();
}
 

