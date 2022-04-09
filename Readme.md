 # Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals:
 
 <br>
The purpose of this database is to gain analytical insight for Sparkify into the way their users listen to music. They want to gain an understanding of what songs users listen to as well as a way to query the current data that they have. I used the logfiles and songs json files to put to gether a database that should satisfy their business needs.  
 <br>
 
 # State and justify your database schema design and ETL pipeline:
 <br>
 
For the design of this database I chose to use a star schema. I thought that this design was more appropriate since they needed the ability to run simple queries against the database. It provides a simpler way for them to query the database allowing for more flexibility to satisfy their business needs. I used the songplays table as a fact table and the other tables(user, songs, artist, and time) as dimension tables. 
 <br>
 
 # Example queries:
 <br>
 
You could find the number of artist by location 

%sql SELECT count(artist_id) as "Number of artist", location FROM artists group by location 
<br>  

You could find the number of users by location

%sql SELECT count(user_id) as "Number of users", location FROM songplays group by location
    
    
