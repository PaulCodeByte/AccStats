from flask import Flask, render_template, url_for, request
import main 


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show', methods=['POST'])
def show():
    stats = request.form.get('data')
    stats=main.stats(stats)
    
    
    return render_template('show.html', data=stats)

if __name__ == "__main__":
    app.run(debug=True)