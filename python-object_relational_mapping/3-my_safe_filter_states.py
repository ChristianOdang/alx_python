''' 
A script that takes the arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the arguement which is passed from the terminal.
'''

# import dbobjects
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
        db_cur = database.cursor()

        # run the select statement on the state table
        # get the data from the terminal
        db_cur.execute("SELECT * FROM states WHERE name = %s \
                        ORDER by states.id", (sys.argv[4],))

        # fetch all data in the resulte
        all_datas = db_cur.fetchall()

        # loop through the result to get the state id and name
        for all_data in all_datas:
            # print only the capital letter not the small letter
            # print(row) if row[1][0] == 'N' else None
            print(all_data)

        database.close()

    else:
        pass

# if there is an error message catch it with an execution message
except MySQLdb.OperationalError as err:

    # print the error message
    print("Connection failed. {}".format(err))
