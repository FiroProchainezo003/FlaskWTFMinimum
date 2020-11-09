from flask import Flask, render_template, request, escape
from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms.validators import DataRequired, IPAddress

app = Flask(__name__)
app.secret_key = 'secret'


def filter_escape(x):
    if x is not None:
        return escape(x)
    else:
        return x


class MyForm(FlaskForm):
    # lambdaの場合
    # name = StringField('name', validators=[DataRequired()], filters=[lambda x: escape(x) if x is not None else x])
    # 関数の場合
    name = StringField('name', validators=[DataRequired()], filters=[filter_escape])
    # name = StringField('name', validators=[IPAddress()], filters=[filter_escape])

    # Validationを自作関数で実行する場合
    def validate_name(self, name):
        print(name.data)
        # if name.data == 'test':
        #     raise ValidationError("Error")


@app.route('/', methods=['GET', 'POST'])
def wtf_minimum():
    form = MyForm()

    if request.method == 'POST':
        print('request : ' + request.form.get('name'))
        print('wtforms : ' + form.name.data)
        print('wtforms : ' + form.data.get('name'))
        print('request : ' + escape(request.form.get('name')))
        print('wtforms : ' + escape(form.name.data))
        print('wtforms : ' + escape(form.data.get('name')))
        if form.validate_on_submit():
            return render_template('index.html', form=form)
        else:
            return render_template('index.html', form=form)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
