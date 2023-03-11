from api import test

from flask import Flask, render_template



res = test.res()
app = Flask(__name__)

@app.route('/')
def trades_table():

    return render_template('trades_table.html', trades=res)

if __name__ == '__main__':
    app.run()
#print(tr.res())

