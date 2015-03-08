<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <META http-equiv="pragma" content="no-cache">
    <title>Volume Bar</title>
    <script language="JavaScript" type="text/javascript" src="../js/volumebar.js"></script>
    <STYLE TYPE=text/css>
      <!--
        A {cursor:default;}
        BODY {cursor:default; background:#000000}
        IMG {cursor:default;}
      -->
    </style>
  </head>
  <body>
    <div id="volumeBar" style="position:relative; left:0px; width:210px; height:13px;">
      <img id="bar" style="position:absolute; top:0px; left:0px; width: 210px; height=13px; z-index:1;"  src="../images/bar.png" alt="Bar">
      <img id="index" style="position:absolute; top:0px; left:[[LEFT]]px; width:15px; height:13px; z-index:2;" src="../images/index.png" alt="Index">
    </div>
    <script>
      document.getElementById('index').onmousedown = dragMouseDown;
    </script>
  </body>
</html>

