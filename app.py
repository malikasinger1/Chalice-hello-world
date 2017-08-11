from chalice import Chalice
from chalice import CORSConfig

app = Chalice(app_name='helloworld')
app.debug = True


# GET with url param
@app.route('/user/{name}')  # if no method then it is GET
def hello_name(name):
    # '/hello/james' -> {"hello": "james"}
    return {'param': name}


# POST with body
@app.route('/user', methods=['POST'])
def create_user():
    # This is the JSON body the user sent in their POST request.
    bodyJson = app.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return {'body': bodyJson}


# GET, POST, PUT and DELETE at same time
@app.route('/users', methods=['GET', 'PUT', 'POST', 'DELETE'])
def create_user():
    # This is the JSON body the user sent in their POST request.
    bodyJson = app.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return {'body': bodyJson}


# Customised response
@app.route('/user', methods=['DELETE'])
def delete_user():
    return Response(body="user is deleted",
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})


# Simple Cors:*
@app.route('/home', methods=['GET'], cors=True)
def delete_user():
    return Response(body="user is deleted",
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})


# Simple Cors:*
@app.route('/home', methods=['GET'], cors=True)
def home():
    return Response(body="user is deleted",
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})


# Customised Cors

config = CORSConfig(
    allow_origin='https://foo.example.com',
    allow_headers=['X-Special-Header'],
    max_age=600,
    expose_headers=['X-Special-Header'],
    allow_credentials=True
)


@app.route('/home', methods=['GET'], cors=config)
def home():
    return Response(body="user is deleted",
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})
