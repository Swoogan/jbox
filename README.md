JBox v0.9.0 - Remote MP3 JukeBox Server.

CLIENT REQUIREMENTS:

- A browser that supports layers, javascript, and css

The following browsers are know to work:

- Mozilla >= 0.9
- IE >= 5.0

SERVER REQUIREMENTS:

- mpg123 >= 0.59r (http://www.mpg123.de)
- aumix >= 1.9 (http://jpj.net/~trevor/aumix.html)
- apache (http://www.apache.org)
  - apache mod userdir
  - apache mod cgi
- apache suexec module (comes with Mandrake, don't know about others)
- python 2.0 or greater (http://www.python.org)
- FlatDB 1.0 python module (http://www.swoogan.ca)
- Mp3Info 1.0 python module (http://www.swoogan.ca)

Please refer to INSTALL for installation information

Once JBox is installed, open in index.html in a browser, and click on the cfg icon and do the following:

1. Configure the app locations
2. Add directories to the database.
3. Add songs to the database.
4. Create a song page (this is necessary becuase if you have 1200 songs like me the page takes too long to be created dynamically every time you view it). This means that everytime you update the song table in the database you will have to refresh the song page.
5. Refresh the server

And eventually:
Enjoy !

All python code and html is copyright (C) Colin Svingen 2002

