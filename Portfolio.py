from flask import Flask,render_template,request
import csv
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/<string:subsite>')
def components(subsite = None):
    if subsite[-5:]=='.html':
        return render_template(subsite)
    else:
        return render_template(subsite+'.html')


def write_to_csv(data):
    with open("database.csv",mode='a',newline='') as csvfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(csvfile,delimiter=',',quotechar='',quoting=csv.QUOTE_NONE)
        csv_writer.writerow([email,subject,message])


def write_to_file(data):
    with open("database.txt",mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")


@app.route('/submit_form', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'Form Submitted! Hurray!'
        except:
        	return'did not save to database'
    else:
        return 'Something went wrong!'


