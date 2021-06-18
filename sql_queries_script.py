# drop tables

killers_bio_drop = "DROP TABLE IF EXISTS killers_bio"
killers_additional_details_drop = "DROP TABLE IF EXISTS killers_additional_details"


# creating tables 

killers_bio_create = ("""
    CREATE TABLE IF NOT EXISTS killers_bio
    (
        KillerID int PRIMARY KEY,  
        YearBorn int,  
        Race text,
		Sex text		
    )
""")

killers_additional_create = ("""
    CREATE TABLE IF NOT EXISTS killers_additional_details
    (
        KillerID int PRIMARY KEY, 
        AgeFirstKill int, 
        AgeLastKill int, 
        Motive text,  
        Sentence text, 
        InsanityPlea text
    )
""")

# inserting records

killers_bio_table_insert = ("""
    INSERT INTO killers_bio
    (KillerID, YearBorn, Race, Sex)
    VALUES (%s, %s, %s, %s);
""")

killers_additional_table_insert = ("""
    INSERT INTO killers_additional_details
    (KillerID, AgeFirstKill, AgeLastKill, Motive, Sentence,InsanityPlea)
    VALUES (%s, %s, %s, %s, %s, %s);
""")


# create and drop tables

create_table_queries = [killers_bio_create, killers_additional_create]
drop_table_queries = [killers_bio_drop, killers_additional_details_drop]