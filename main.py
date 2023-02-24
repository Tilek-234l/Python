class Todo:
    def __init__(self):
        self.todo_items = []

    def add_todo(self, item):
        if not isinstance(item, TodoItem):
            return
        self.todo_items.append(item)

    def list_items(self):
        q = 1

        for i in self.todo_items:
            print(f"{q}. {i} - {i.is_done}")
            q += 1

    def find(self,word):
        answer = []
        counter = 1
        for i in self.todo_items:
            if word in i.task:
                answer.append((counter, i))
        print(answer)


class TodoItem:
    def __init__(self, task):
        self.task = task
        self.is_done = False

    def check(self):
        self.is_done = True

    def uncheck(self):
        self.is_done = False

    def __repr__(self):
        return self.task