 # The purpose of this database in the context of the startup, Sparkify, and their analytical goals:
<br>
The purpose of this database is to gain analytical insight for Sparkify into the way their users listen to music. They want to gain an understanding of what songs users listen to as well as a way to query the current data that they have. I used the logfiles and songs json files to put to gether a database that should satisfy their business needs.  
<br>
 # Justifification of the database schema design and ETL pipeline:
<br>
For the design of this database I chose to use a star schema. I thought that this design was more appropriate since they needed the ability to run simple queries against the database. It provides a simpler way for them to query the database allowing for more flexibility to satisfy their business needs. I used the songplays table as a fact table and the other tables(user, songs, artist, and time) as dimension tables. 
<br>
# Database design: 
For this project I used a star schema including the following 5 tables.
*songplay_table I used this as the Fact table. This table includes the fields songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, and the user_agent. This table holds information pertaining to which song the user is listening to. 
*user_table I used this as a dimension table. It holds information about the user. It includes the fields of user_id, first_name, last_name, gender, and level.
*song_table I used this table as a dimension table. It holds information about each song. It includes the fields of song_id, title, artist_id, year, and the duration of the song.
*artist_table I used this table as a dimension table. It holds information about each artist. It includes the field sof artist_id, name, location, latitude, and longitude of the artist.
*time_table I used this table as a dimension table. It holds information about the start time of the song. It includes the start_time, hour, day, week, month, year, and weekday.
<br>
# ETL Process: 
For this process I used two files. The first file log dataset(log_data) which included the artist, auth, firstName, gender, itemSession, lastName, length, level, location, method, page, registration, sessionid, song, status, ts(timestamp), userAgent, and the userId. This was used to populate the time, artist, user, and songplays tables. 
I second file the song(song_data) dataset which included the information of num_songs, artist_id, artist_logitude, artist_latitude, artist_location, artist_name, song_id, title, duration, and year of the song. This was used to populate the song and songplays tables.
<br>
# Project Repository files: 
For this project I've included the following files:
*create_tables.py (This uses the sql_queries file to actually create the tables for the database. It also drops them if needed.)
*etl.ipynb (This is a notebook that contains the etl process of each table it is similar to the etl.py file but in notebook form )
*etl.py (This file uses the queries in sql_queries.py to extract data from the song_data and log_data files and then puts them into each table)
*sql_queries.py (This file contains the queries used by the etl.py file or the etl.ipynb notebook to insert into and create the required tables. )
<br>
# How To Run the Project: 
To run this project open a notebook and use the '!python create_tables.py' then either open up the etl.ipynb notebook and run each line or use the '!python etl.py' command.
<br>
 # Example queries:
<br>
You could find the number of artist by location 
%sql SELECT count(artist_id) as "Number of artist", location FROM artists group by location 
<br>    
You could find the number of users by location
%sql SELECT count(user_id) as "Number of users", location FROM songplays group by location
    
   
