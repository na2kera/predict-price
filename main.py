from fastapi import FastAPI #FastAPIをインポート

app = FastAPI() #FastAPIのインスタンス作成

@app.get("/") #getメソッドで"/"にアクセス
def hello():
    return {"message":"Hello World!"}

@app.post("/")
def calc(x: int,y: int):
    z = x*y
    return {"result":z}