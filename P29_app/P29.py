from flask import Flask, render_template,url_for
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
             

@app.route("/eda")
def eda():
    return render_template('eda.html')

@app.route("/conclusion")
def conclusion():
    return render_template('conclusion.html')

if __name__ == '__main__':
    app.run(debug=True)