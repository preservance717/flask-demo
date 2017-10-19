from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    # app.run()
    # app.run(host='0.0.0.0') #操作系统去监听所有公开的 IP,所有公开的IP都可以访问。
    app.run(debug=True) #代码修改时，服务器自动加载，仅在开发时使用