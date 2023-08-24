'''
This model is the same as before but this take the name
arguement which is passed from the terminal
'''
# import dbobject
import MySQLdb
import sys

# try connection and exception
try:
    # connection to database
    if len(sys.argv) > 3:
        database = MySQLdb.connect(user=f'{sys.argv[1]}',

                                   passwd=f'{sys.argv[2]}',
                                   db=f'{sys.argv[3]}')
        # set cursor if connection succeed
        cursor = database.cursor()

        # run the select statement on the states tables
        # get the data from the terminal
        cursor.execute("SELECT * FROM states WHERE name = %s \
                    ORDER by states.id", (sys.argv[4],))

        # fetch all rows in the result
        rows = cursor.fetchall()

        # loop through the result to get the state id and name
        for row in rows:
            # print only the capital letter not the small letter
            print(row) if row[1][0] == 'N' else None
    else:
        pass

# if there is an error catch it with an execution message
except MySQLdb.OperationalError as e:

    # print the error message
    print("Connection failed. {}".format(e))
