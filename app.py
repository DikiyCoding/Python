from flask import Flask
from flask import request
from service import ToDoService

app = Flask(__name__)


@app.route('/todo/create', methods=['POST'])
def create_todo():
    result = ToDoService().create(request.get_json())
    return result.to_json()


@app.route('/todo/get_all', methods=['GET'])
def get_all_todo():
    result = ToDoService().get_all()
    for todo in result:
        print(f'There is \"todo\" with id = {todo.get_id()},'
              f'name = {todo.get_name()}'
              f'and mark = {todo.is_done()}')
    return True


@app.route('/todo/get_all_undone', methods=['GET'])
def get_all_todo_undone():
    result = ToDoService().get_all_undone()
    for todo in result:
        print(f'There is \"todo\" with id = {todo.get_id()},'
              f'name = {todo.get_name()}'
              f'and mark = {todo.is_done()}')
    return True


if __name__ == '__main__':
    app.run()