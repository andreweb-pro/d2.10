import os
from bottle import Bottle, request
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[BottleIntegration()])

app = Bottle()

@app.route('/')
def index():
    form = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>D2</title>
    </head>
    <body>
        <h1>This is main page</h1>
        <hr>
        <h2>For visit successful page, append to the end of URL "https://d2-10.herokuapp.com/success"</h2>
        <hr>
        <h2>For visit fail page, append to the end of URL "https://d2-10.herokuapp.com/fail"</h2>
        <hr>
    </body>
</html>
"""
    return form

@app.route('/success')
def success():
    return


@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")


app.run(host='localhost', port=8080)
