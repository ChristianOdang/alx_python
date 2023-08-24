''' 
A script that lists all states with a name starting with N(upper N)
from the database hbtn_0e_0_usa
'''
# import dbobject
import MySQLdb
import sys


# try connection and execution
try:
    if len(sys.argv) > 3:
        database = MySQLdb.connect(user=f"{sys.argv[1]}",

                                   passwd=f"{sys.argv[2]}",
                                   db=f"{sys.argv[3]}")

        # set cursor for the connection
        cur = database.cursor()

        # run the select statement on the states table where users name start
        # with N using the like operation
        cur.execute("SELECT * FROM states WHERE name LIKE \
                     'N%' ORDER by states.id")

        # fetch all rows in the result
        rows = cur.fetchall()

        # loop through the result to get the states id
        for row in rows:

            # print only the capital letter not the small letter
            print(row) if row[1][0] == 'N' else None
    else:
        pass

    # if there is an error catch it with an exception message
except MySQLdb.OperationalError as e:

    # print the error message
    print("Connection failed. {}".format(e))
