from flask import Flask, render_template, url_for, redirect, request
from models import Student

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    sts = Student.select().order_by(Student.id.desc())
    return render_template('index.html', s=sts)
@app.route('/details/<int:id>')
def details(id):
    st=Student.get_by_id(id)
    return render_template('details.html',st=st)
@app.route('/delete/<int:id>')
def delete(id):
    st = Student.get_by_id(id)
    st.delete_instance()
    return redirect(url_for('index'))


@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == 'POST':
        n = request.form['firstname']
        l = request.form['lastname']
        Student.create(name=n,family=l)
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    st = Student.get_by_id(id)
    if request.method == 'POST':
        new_firstname = request.form['name']
        new_lastname = request.form['family']
        st.name = new_firstname
        st.family = new_lastname
        st.save()
        return redirect(url_for('index'))
    return render_template('update.html', st=st)
        

@app.route('testpage')
def test():
    pass

if __name__ == '__main__':
    app.run(debug=True)