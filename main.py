from flask import Flask
app = Flask(__name__)  # __name__ 代表目前執行的模組

@app.route("/")  # 函式的裝飾 (Decorator) : 以函式為基礎，提供附加的功能，原路徑:http://127.0.0.1:5000
def home():
    return "Hello Flask2"

@app.route("/test")  # 代表要處理網站路徑，也就是路徑:http://127.0.0.1:5000/test
def test():          # 其餘沒有定義的路徑就會跳出 Not Found (程式沒有處理此路徑)(ex:http://127.0.0.1:5000/hfiefpresovuh)
    return "This is test"

if __name__ == "__main__":  # 如果以主程式執行
    app.run()  # 啟動伺服器