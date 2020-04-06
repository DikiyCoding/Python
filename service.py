from model import ToDoDB


class ToDoService:
    def __init__(self):
        self.db = ToDoDB()

    def create(self, params):
        return self.db.create(params['name'])

    def update(self, params):
        return self.db.update(params['id'], params['name'])

    def delete(self, params):
        return self.db.delete(params['id'])

    def mark(self, params):
        return self.db.mark_as_done(params['id'])

    def get_all(self):
        return self.db.get_all()

    def get_all_undone(self):
        undone = []
        for todo in self.get_all():
            if not todo.is_done:
                undone.append(todo)
        return undone
