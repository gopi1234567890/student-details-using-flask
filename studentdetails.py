from flask import Flask, request, render_template

import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mydatabase = mysql.connector.connect(
    host='localhost', user='root',
    passwd='mypass', database='students_final')

mycursor = mydatabase.cursor()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        rollno = request.form['roll']

        query = "SELECT * FROM students1 WHERE student_id = '" + str(rollno) + "'"
        mycursor.execute(query)
        details1 = mycursor.fetchall()
        l = []
        l.append(details1[0])
        return render_template('test.html', details=l)
    else:
        return render_template('index133.html')


if __name__ == '__main__':
    # cors = CORS(app)

    app.run(debug=True, port=8000)