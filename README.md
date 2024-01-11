# Transportation_Project_SQL
A project created for Saint Cloud State. Given XML network and events files, create a program that can perform queries on events.

# NOTES
* XML files were shortened because there were over 250,000 lines in the nodes/links file and over 3,000,000 lines in events. Github doesn't allow files over 25 MB.
* The events table used to be broken up into many tables to reduce data redundancy and improve organization, however inserting events was too slow on my machine. Thus the events table was consolidated into one table to improve performance at the cost of storing redundant data.

# Final_Loaderv2.py
The program that reads the XML files into their respective tables. It's v2 because it was created after the consolidation of the various events tables.

# MainApplication.py
The core program that performs queries on the database. Features seeing what events happened at certain nodes/links and querying by time or event type.

# DB Schema Code.txt
The SQL code for the database.
