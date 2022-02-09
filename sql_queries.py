# DROP TABLES

songplay_table_drop = "DROP table songplays"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table times"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL, 
    start_time time NOT NULL,
    user_id int NOT NULL,
    level text,
    song_id int  NOT NULL,
    artist_id varchar  NOT NULL,
    session_id int,
    location text,
    user_agent text,
    PRIMARY KEY(songplay_id),
    CONSTRAINT time_table FOREIGN KEY(start_time) REFERENCES times(start_time),
    CONSTRAINT users_table FOREIGN KEY(user_id) REFERENCES users(user_id),
    CONSTRAINT artist_table FOREIGN KEY(artist_id) REFERENCES artists(artist_id),
    CONSTRAINT song_table FOREIGN KEY(song_id) REFERENCES songs(song_id)
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id int PRIMARY KEY,
    first_name text,
    last_name text,
    gender text,
    level text    
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id SERIAL PRIMARY KEY,
    title text,
    artist_id varchar NOT NULL,
    year int,
    duration float,
    CONSTRAINT artist_table FOREIGN KEY(artist_id) REFERENCES artists(artist_id)
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY,
    name text,
    location text,
    latitude float,
    longitude float
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS times (
    start_time time PRIMARY KEY,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id) 
DO NOTHING;
""")
## there should be no conlicts because songplay_id is an auto-generated key

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = """
INSERT INTO songs (title, artist_id, year, duration)
VALUES (%s, %s, %s, %s)
ON CONFLICT (song_id) 
DO NOTHING;
"""

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) 
DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO times (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) 
DO NOTHING;
""")
# if start times are equal there is no need to update the table.

# FIND SONGS

song_select = ("""
SELECT
songs.song_id,
artists.artist_id
FROM songs
INNER JOIN artists
ON songs.artist_id = artists.artist_id
AND songs.title = %s
AND artists.name = %s
AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create,  time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]