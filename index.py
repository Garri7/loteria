from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(27,34)
    random_number1 = random.randint(11,18)
    random_number2 = random.randint(43,49)
    random_number4 = random.randint(35,42)
    random_number3 = random.randint(1,10)
    random_number5 = random.randint(19,26)
    return render_template('index.html', 
    random_number=random_number, 
    random_number1=random_number1,
    random_number2=random_number2,
    random_number3=random_number3,
    random_number4=random_number4,
    random_number5=random_number5)
    # return render_template('index.html')

@app.route('/sobre')
def about():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True)    