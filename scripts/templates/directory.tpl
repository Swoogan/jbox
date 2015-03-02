<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>Admin Song Directories</title>
    <style type=text/css>
      BODY {font-family: Verdana,Geneva,Arial,Times; background: #000000; color: #FFFFFF}
      td { text-align: center; }
      table.center {
        margin-left: auto;
        margin-right: auto;
      }
    </style>
  </head>
  <body>
    [[TABLE]]
    <p><br><p>
    <table class="center">
      <tr><td><b>Add a new absolute path:</b></td><tr>
      <tr><td>
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

