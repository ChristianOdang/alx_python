""" A script that starts a Flask
web application: The application must run
on the default port and must run
on 0.0.0.0
"""
# import flask module
from glob import escape
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


@app.route('/hbnb')
def hbnb():
    ''' 
    A function that returns
    a string hbnh... on a get
    request to a router page
    param:
        type: NONE
    Return:
        type: String
    '''
    return "HBNB"


@app.route('/c/<text>')
def hbnb_C_is_fun(text):
    ''' 
    A function definition that returns 
    a string... on a get request
    to a router page
    parameter:
         type: type
    return:
         type: String
    '''
    return f"C {text.replace('_',' ')}"


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    ''' 
      A function definition that returns 
      a string... on a get request
      to a router page
      parameter:
           type: string
      return:
           type: string
      '''
    return f"Python {escape(text.replace('_',' '))}"


@app.route('/number/<int:n>')
def hello_id(n):
  ''' 
  Function that returns the int parameter passed
  Parameter:
        type:
  return:
        type: string + values pass
  '''
  return f"{n} is a number"


if __name__ == '__main__':
    # for every route
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0')
