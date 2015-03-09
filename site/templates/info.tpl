<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="refresh" content="15">
    <title>Now Playing</title>
    <script src="/js/info.js"></script>
    <style type=text/css>
      .song-info-table {font-size: 8px; font-family: Verdana, Geneva, Arial, sans-serif; cursor: default; background: #000000; color: #FFFFFF; text-align: center; }
      .song-title { font-size: 9px; font-family: Verdana, Geneva, Arial, sans-serif; background: #b4ae00; text-align: center; }
      .song-artist { font-size: 9px; font-family: Verdana, Geneva, Arial, sans-serif; background: #36648b; text-align: center; }
      .song-info { font-size: 10px; font-family: Verdana, Geneva, Arial, sans-serif; background: #5f5f5f;  text-align: center;}
      .song-label { font-size: 10px; font-family: Verdana, Geneva, Arial, sans-serif; background: #5f5f5f;  text-align: left;}
    </style>
  </head>
  <body onload="changeSong({{ song.id }})">
    <table border="0" cellspacing="2" cellpadding="1" class="song-info-table">
      <tr>
   	<td class="song-label">Song:</TD>
   	<td colspan="3" class="song-title">{{ song.title }}</TD>
      </tr>
      <tr>
      	<td class="song-label">Artist:</TD>
      	<td colspan="3" class="song-artist">{{ song.artist }}</TD>
      </tr>
      <tr>
      	<td style="text-align: center;" class="song-info"><img src="/images/stereo.png"></TD>
      	<td style="text-align: center;" class="song-info">{{ song.bitrate }} kbps</TD>
      	<td style="text-align: center;" class="song-info">{{ song.frequency }} kHz</TD>
      	<td style="text-align: center;" class="song-info">{{ song.length }}</TD>
      </tr>
    </table>
  </body>
</html>

