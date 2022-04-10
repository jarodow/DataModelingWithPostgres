import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """This procedure opens the song_data file and inserts the song and artist records into the file
        It passes the filepath as an argument"""
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0]
    song_data = song_data.tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values[0]
    artist_data = artist_data.tolist()
    cur.execute(artist_table_insert, artist_data)



def process_log_file(cur, filepath):
    """this procedure process the logfile
It passes the log_data_file as an argument filepath
It converts the timestamp to datatime
It then inserts the data into the time records
It then Inserts into the user table, then the songplay table
"""
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    #df.ts = str(pd.to_datetime(df.ts))
    time_data = [df.ts.values,t.dt.hour.values,t.dt.day.values,t.dt.week.values,t.dt.month.values,t.dt.year.values,t.dt.weekday.values]
    column_labels = pd.to_datetime(df['ts'], unit='ms')
    time_df = pd.DataFrame(time_data, columns = column_labels)
    time_df = time_df.transpose()
   
    #iterating through each row
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)



def process_data(cur, conn, filepath, func):
    """ This procedure process the song_data file through the argument as filepath
    It extracts the information then stores it into the 
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """ this procedure connects to the database
    then runs the process_song_file function loading the song_data
    then runs the process_log_file funciton loading the log_data
    then it closes the connection 
    """
    #connecting to the sparkifydb
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    #running the process_song_file function loading the song_data file
    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    #running the process_log_file function loading the log_data file
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)


#closing the connection to the sparkify database    
    conn.close()


if __name__ == "__main__":
    main()
