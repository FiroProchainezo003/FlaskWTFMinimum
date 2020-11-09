# FlaskWTFMinimum

## プロジェクトについて

このプロジェクトはFlaskでFlask-WTFを使用する最小のサンプルです。

Flask および Flask-WTF が必要です。


# プロジェクトの取得方法

クローンしてください。

```
git clone https://github.com/FiroProchainezo003/FlaskWTFMinimum
```

## 実行方法

### windows

```shell script
# Cloneしたフォルダで
$ python3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ python app.py
```

1. 上記が完了したらブラウザで `http://localhost:5000/` にアクセス<br>
   フォームが表示されます。
2. id="name"のinputに適当な値を追加し、「Go」を押します。
3. 同一ページ(http://localhost:5000/)にPOSTされ、入力された値がid="name"のinput要素に表示さます。<br>
   また、以下の内容をコンソールにprintで表示します。<br>
   ```
   request.form["name"]
   form.name.data
   form.data.get('name')
   escape(request.form.get('name')
   escape(form.name.data)
   escape(form.data.get('name')
   ```


### linux

```shell script
# Cloneしたフォルダで
$ python3 -m vevn venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ python app.py
```

上記が完了したらブラウザで `http://localhost:5000/` にアクセス

1. 上記が完了したらブラウザで `http://localhost:5000/` にアクセス<br>
   フォームが表示されます。
2. id="name"のinputに適当な値を追加し、「Go」を押します。
3. 同一ページ(http://localhost:5000/)にPOSTされ、入力された値がid="name"のinput要素に表示さます。<br>
   また、以下の内容をコンソールにprintで表示します。<br>
   ```
   request.form["name"]
   form.name.data
   form.data.get('name')
   escape(request.form.get('name')
   escape(form.name.data)
   escape(form.data.get('name')
   ```

## 動作について

### filtersについて

本プロジェクトのFlask-WTF用のClass定義には「filters」も指定しています。<br>
WTFの動作確認だけで言えばfiltersの指定は不要です。<br>
しかしながら、Webアプリケーションとして見た場合、フォーム入力された値をエスケープして使うのが当然のため、エスケープ処理を追加してあります。(lambda/自作の関数のいずれもescape(x)を返します。)<br>

filtersにはlambdaで処理を記載するか、自作の関数を指定できます。<br>
デフォルトでは関数が動作するようにしています。(以下コード。コメントアウトされているほうがlabmda。)<br>
```python
# name = StringField('name', validators=[DataRequired()], filters=[lambda x: escape(x) if x is not None else x])
name = StringField('name', validators=[DataRequired()], filters=[filter_escape])
```

### validatorsについて

Flask-WFTではvalidatorsに指定したバリデータ(`validators=[DataRequired()]`)と、`validate_xxx(def validate_name(self, name))`として定義された自作の関数のバリデータを動作させることができます。<br>
validatorsまたはvalidate_xxxは`form.validate_on_submit()`が呼ばれた時に動作します。<br>
どちらも指定した場合は、どちらもTrueにならないとTrueになりません。<br>
DataRequired()を指定した場合、formを空にすると送信できないので確認が難しいですが、IPAddress()にすると、IPAddress(例えば：192.168.0.1)以外のものを送信するとバリデーションに失敗するのがわかります。

自作の関数からバリデーション失敗を返したい場合は以下のように書きます。<br>
```
        raise ValidationError("Error")

```


## pythonバージョン

```
$ flask --version
Python 3.7.4
Flask 1.1.2
Werkzeug 1.0.1
```

## 各モジュールがサポートしているバージョン

### Flask
[Flask - 1.1.x Installation](https://flask.palletsprojects.com/en/1.1.x/installation/)

### FlaskSQLAlchemy
[FlaskWTF - stable(0.14.2)](https://flask-wtf.readthedocs.io/en/stable/)
(使用バージョンは0.14.3、ドキュメントはstable(0.14.2)が最新の模様。)
