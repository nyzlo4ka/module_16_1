from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_main() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def read_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def read_user_info(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


