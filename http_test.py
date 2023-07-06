# from flask import Flask
from flask import Flask, request

app = Flask(__name__)


# ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    # # リクエストメソッドの使用
    # print(request.method)
    # # return "login page"
    # # メソッドはpostで送信ボタンの作成
    # return '''
    # <form action="/login" method="post">
    #     Password:<input type="text"><br>
    #     <input type='submit'>
    # </from>
    # '''
    # リクエストメソッドGETのときは以下の処理を行う
    if request.method == "GET":
        return '''
        <form action="/login" method="post">
            Password:<input type="text"><br>
            <input type='submit'>
        </from>
        '''
    # リクエストメソッドPOSTの時は以下の処理を行う
    if request.method == "POST":
        return "Login in"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
