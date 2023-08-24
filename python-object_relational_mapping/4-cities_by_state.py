""" 
A script that use inner join to query data from multiple table
the database is passed from the terminal
"""

# import dbobject
import MySQLdb
import sys

# try connection and execution
try:
    # connect to database
    if len(sys.argv) > 3:
        database = MySQLdb.connect(user=f"{sys.argv[1]}",
                                   passwd=f"{sys.argv[2]}",
                                   db=f"{sys.argv[3]}")

        # set cursor if connection succeed
        cursor = database.cursor()

        # run the select statement on the cities table
        cursor.execute("SELECT cities.id, cities.name, \
                    states ON cities.states_id=states.id \
                    ORDER by cities.id")

        # fetch all rows in the result
        rows = cursor.fetchall()

        # loop through the result to get the cities id and name
        for row in rows:
            print(row)

    else:
        pass

    database.close()
    # if there is an error catch it with an exception message
except MySQLdb.OperationalError as e:

    # print the error message
    print("Connection failed. {}".format(e))
