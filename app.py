from flask import Flask, render_template, request, escape
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'secret'

def filter_escape(x):
    return escape(x)

class MyForm(FlaskForm):
    # name = StringField('name', validators=[DataRequired()], filters=[lambda x: escape(x), filter_escape])
    name = StringField('name', validators=[DataRequired()], filters=[filter_escape])

    def validate_name(self, name):
        print(name)




@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = MyForm()

    if request.method == 'POST':
        print('request : ' + request.form.get('name'))
        print('wtforms : ' + form.name.data)
        print('wtforms : ' + form.data.get('name'))
        print('request : ' + escape(request.form.get('name')))
        print('wtforms : ' + escape(form.name.data))
        print('wtforms : ' + escape(form.data.get('name')))
        form.validate_on_submit()
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
