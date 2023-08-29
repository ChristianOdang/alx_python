""" A script that starts a Flask
web application: The application must run
on the default port and must run
on 0.0.0.0
"""
# import flask module
from flask import Flask

# define a flask instance
app = Flask(__name__)
# set strict_s; ashes flag to false

# create a route for index


@app.route('/')
# a function definition
def hello():
    """ 
    A function definition that returns
    a string hello... on a get request
    to a router page
    param:
        type: NONE
    Return:
        type: String
    """

    return "Hello HBNB!"


if __name__ == '__main__':
    # for every route
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0')
