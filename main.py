from flask import Flask

app = Flask(__name__)


@app.route('/')
def mbl_digiform():
  return "MBL/ATML BORROWER'S DIGIFORM!"


app.run(host='0.0.0.0', port=8080)
