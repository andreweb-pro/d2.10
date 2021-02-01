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
    return HTTPResponse(status=200, body="Successful page")


@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")


if os.environ.get("APP_LOCATION") == "heroku":
    sentry_sdk.init(dsn=os.environ['SENTRY_DSN'],
                    integrations=[BottleIntegration()]
                    )
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3,
    )
elif __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
