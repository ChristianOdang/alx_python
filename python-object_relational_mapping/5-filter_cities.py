""" 
  A script that takes in the name of a state as an arguement and lists 
  all cities of that state, using the database hbtn_0e_4_usa
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
        cursor.execute("SELECT name FROM cities WHERE state_id = ( \
                    SELECT states.id FROM states \
                    WHERE name LIKE %s)", (sys.argv[4],))

        # fetch all rows in the result
        rows = cursor.fetchall()

        # loop through the result to get the cities id,
        # name and append, till the end of the result
        result = ', '.join(row[0] for row in rows)
        print(result)
    else:
        pass

    database.close()

# if there is an error, catch it with an exception
except MySQLdb.OperationalError as e:
    print(e)
