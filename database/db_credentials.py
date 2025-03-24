# Citation for the following code:
# Date: 05/19/2024
# Copied from: CS 340 Flask Guide
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

# To actually have your app use this file, you need to RENAME the file to db_credentials.py
# You will find details about your CS340 database credentials on Canvas.

# the following will be used by the webapp.py to interact with the database
# You can also use environment variables

# For Local Devlelopment
host = 'localhost'
user = 'root'                                   # can be different if you set up another username in your MySQL installation
passwd = ''                        # set accordingly
db = 'cs_340'


# For OSU Flip Servers

host = 'classmysql.engr.oregonstate.edu'      # MUST BE THIS
user = 'CS340_swanbria'       # don't forget the cs340_ prefix
passwd = 'IKWjiilHUyLz'               # should only be 4 digits if default
db = 'cs340_swanbria'                                  
