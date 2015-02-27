<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="refresh" content="15">
    <title>Now Playing</title>
    <script type="text/javascript" language="JavaScript" src="../js/info.js"></script>
    <style type=text/css>
      <!--
        BODY {font-size: 8px; font-family: Verdana,Geneva,Arial,Times; cursor: default; background: #000000; color: #FFFFFF}
        .songTitle {font-size: 9px; font-family: Verdana,Geneva,Arial,Times; background: #b4ae00}
        .songArtist {font-size: 9px; font-family: Verdana,Geneva,Arial,Times; background: #36648b}
        .songInfo {font-size: 10px; font-family: Verdana,Geneva,Arial,Times; background: #5f5f5f}
      -->
    </style>
  </head>
  <body onload="changeSong([[ID]])">
    <center>
      <table border="0" cellspacing="2" cellpadding="1">
      	<tr>
      		<td align="left" class="songInfo">Song:</TD>
      		<td colspan="3" align="center" class="songTitle">[[TITLE]]</TD>
      	</tr>
      	<tr>
      		<td align="left" class="songInfo">Artist:</TD>
      		<td colspan="3" align="center" class="songArtist">[[ARTIST]]</TD>
      	</tr>
      	<tr>
      		<td align="center" class="songInfo"><img src="../images/stereo.png"></TD>
      		<td align="center" class="songInfo">[[BITRATE]] kbps</TD>
      		<td align="center" class="songInfo">[[FREQUENCY]] kHz</TD>
      		<td align="center" class="songInfo">[[LENGTH]]</TD>
      	</tr>
      </table>
    </center>
  </body>
</html>

