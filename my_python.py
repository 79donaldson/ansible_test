from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is my first application!' 

@app.route('/template')
def template():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)