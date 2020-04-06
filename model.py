class ToDoModel:
    def __init__(self, _id, _name):
        self._id = _id
        self._name = _name
        self._is_done = False

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, _name):
        self._name = _name

    def is_done(self):
        return self._is_done

    def set_as_done(self):
        self._is_done = True

    def to_json(self):
        return {'name': self._name,
                'id': self._id}

    def equals(self, _id):
        return self._id == _id


class ToDoDB:
    def __init__(self):
        self.todos = []
        self._id = 0

    def create(self, name):
        todo = ToDoModel(self._id, name)
        self.todos.append(todo)
        self._id += 1
        return todo

    def update(self, _id, name):
        for todo in self.todos:
            if todo.get_id.equals(_id):
                self.todos.remove(todo)
                todo.set_name(name)
                self.todos.append(todo)
                return True
            else:
                print("Current id does not exist")
                return False

    def delete(self, _id):
        for todo in self.todos:
            if todo.get_id.equals(_id):
                self.todos.remove(todo)
                return True
            else:
                print("Current id does not exist")
                return False

    def mark_as_done(self, _id):
        for todo in self.todos:
            if todo.get_id.equals(_id):
                todo.set_as_done()
                return True
            else:
                print("Current id does not exist")
                return False

    def get_all(self):
        return self.todos
