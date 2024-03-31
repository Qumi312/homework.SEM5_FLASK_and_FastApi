"""
Объедините студентов в команды по 2-5 человек  в сессионных залах.
Создать API для получения списка фильмов по жанру. Приложение должно иметь возможность получать список фильмов по заданному жанру.
●	Создайте модуль приложения и настройте сервер и маршрутизацию.
●	Создайте класс Task с полями id, title, description и genre.
●	Создайте список tasks для хранения фильмов.
●	Создайте маршрут для получения списка фильмов по жанру (метод GET).
●	Реализуйте валидацию данных запроса и ответа.
"""

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str


tasks = [
    Task(id=1, title="Task01", description="Description 1"),
    Task(id=2, title="Task02", description="Description 2"),
    Task(id=3, title="Task03", description="Description 3"),
    Task(id=4, title="Task04", description="Description 3"),
    Task(id=5, title="Task05", description="Description 3"),
    Task(id=6, title="Task06", description="Description 4"),
]

@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks


@app.post('/tasks/')
async def create_post(task: Task):
    tasks.append(task)
    return tasks


@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    for index, t in enumerate(tasks):
        if t.id == task_id:
            return tasks[index]
    # raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    for index, t in enumerate(tasks):
        if t.id == task_id:
            tasks[index] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")




if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000)
