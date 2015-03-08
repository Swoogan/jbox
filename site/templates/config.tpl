<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>JBox Configuration</title>
    <style type=text/css>
      BODY {font-family: Verdana,Geneva,Arial,Times; background: #000000; color: #FFFFFF}
      .table {font-size: 12px;}
      table.center {
        margin-left: auto;
        margin-right: auto;
      }
    </style>
  </head>
  <body>
    <form action="config.py" method="post">
      <table class="center" style="width: 500px; border: 0">
        <tr><td colspan="2" style="text-align: center"><b>Configuration Options</b></td></tr>
        <tr><td class="table">Absolute path of mpg123: </td><td><input type="text" name="MPG123_PATH" value="[[MPG123_PATH]]" size="40"></td></tr>
        <tr><td class="table">Absolute path of aumix: </td><td><input type="text" name="AUMIX_PATH" value="[[AUMIX_PATH]]" size="40"></td></tr>
        <tr><td colspan="2">&nbsp;</td></tr>
        <tr><td colspan="2" style="text-align: center"><input type="submit" name="save" value="Save"></td></tr>
      </table>
    </form>
  </body>
</html>

