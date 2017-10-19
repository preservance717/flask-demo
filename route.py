from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/user/<username>') #url增加变量部分，变量字段标记成 <variable_name>
def show_user_profile(username):
    return 'user %s' % username

@app.route('/post/<int:post_id>')#也可以指定一个可选的转换器通过规则 <converter:variable_name>
def show_post(post_id):
    return 'POST %d' % post_id

@app.route('/project/') #访问一个结尾不带斜线的 URL('/project') 会被 Flask 重定向到带斜线的规范URL('/project/')去
def show_project():
    return 'project page'

@app.route('/about')#访问结尾带斜线的 URL('/about/) 会产生一个 404 “Not Found” 错误。
def about():
    return 'about page'

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, url_for
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     pass
# @app.route('/login')
# def login():
#     pass
# @app.route('/user/<username>')
# def profile(username): pass
#
# with app.test_request_context():
#     print (url_for('index'))
#     print (url_for('login'))
#     print (url_for('login', next='/'))
#     print (url_for('profile', username='John Doe'))