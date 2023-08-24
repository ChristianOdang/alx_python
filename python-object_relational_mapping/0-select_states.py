'''
A script that lists all states from the database hbtn_0e_0_usa
'''
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

        # run the select statement on the states table
        cursor.execute("SELECT * FROM states ORDER by states.id")

        # fetch all rows in the result
        rows = cursor.fetchall()

        # loop through the result to get the state id and name
        for row in rows:
            print(row)
    else:
        pass
# if there is an error catch it with and exception message
except MySQLdb.OperationalError as e:
    # print the error message
    print("Connection failed. {}".format(e))
