from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mbl_digiform():
  return render_template('home.html')

  #"MBL/ATML BORROWER'S DIGIFORM!"


app.run(host='0.0.0.0', port=8080)
