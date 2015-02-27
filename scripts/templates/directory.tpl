<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>Admin Song Directories</title>
    <style type=text/css>
      <!--
        BODY {font-family: Verdana,Geneva,Arial,Times; background: #000000; color: #FFFFFF}
      -->
    </style>
  </head>
  <body>
    [[TABLE]]
    <p><br><p>
    <table align="center">
      <tr><td align="center"><b>Add a new absolute path:</b></td><tr>
      <tr><td align="center">
        <form action="directory.py" method="post">
          <input type="text" name="newdir" size="40"><br>
          Recurse into Subdirectorys? <input type="checkbox" name="recurse" CHECKED value="Y"><p>
          <input type="submit" value="Add" name="add">
          <input type="reset" value="Clear">
        </td>
        </form>
      </tr>
    <table>
  </body>
</html>

