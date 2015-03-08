JBox v0.10.0 - Remote MP3 JukeBox Server.

CLIENT REQUIREMENTS:

- A modern browser 

The following browsers are know to work:

- Google Chrome

SERVER REQUIREMENTS:

- mpg123 >= 0.59r (http://www.mpg123.de)
- python 3.1 or greater (http://www.python.org)
- python cherrypy module
- python mutagen module

Please refer to INSTALL for installation information

Once JBox is installed, open http://127.0.0.1:8080/html/ in a browser, and click on the cfg icon and do the following:

1. Configure the app locations
2. Add directories to the database.
3. Add songs to the database.
4. Create a song page (this is necessary becuase if you have 1200 songs like me the page takes too long to be created dynamically every time you view it). This means that everytime you update the song table in the database you will have to refresh the song page.
5. Refresh the server

And eventually:
Enjoy !

All python code and html is copyright (C) Colin Svingen 2002

