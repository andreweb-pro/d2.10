import os
from bottle import Bottle, request
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[BottleIntegration()])

app = Bottle()


@app.route('/success')
def success():
    return


@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")


app.run(host='localhost', port=8080)