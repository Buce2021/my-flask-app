from flask import Flask, request, render_template_string, send_from_directory
import random
import os

app = Flask(__name__)

number_to_guess = random.randint(1, 100)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    message = ""
    if request.method == 'POST':
        try:
            user_guess = int(request.form['guess'])
            if user_guess < number_to_guess:
                message = "太小了！再试一次。"
            elif user_guess > number_to_guess:
                message = "太大了！再试一次。"
            else:
                message = "正确！你猜对了！"
        except ValueError:
            message = "请输入一个有效的数字。"
    
    return render_template_string('''
        <!doctype html>
        <html>
            <head>
                <title>猜数字游戏</title>
            </head>
            <body>
                <h1>猜数字游戏</h1>
                <form method="post">
                    <label for="guess">请输入一个数字：</label>
                    <input type="text" id="guess" name="guess">
                    <input type="submit" value="提交">
                </form>
                <p>{{ message }}</p>
            </body>
        </html>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)
