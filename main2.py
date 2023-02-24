# # # import datetime
# # #
# # #
# # # class Human:
# # #     count_of_hands = 1
# # #     count_of_legs = 2
# # #
# # #     def __int__(self, name, birthday):
# # #         self.name = name
# # #         self.birthday = birthday
# # #
# # #     def greet(self):
# # #         print(self.name)
# # #
# # #        @staticmethod
# # #     def now():
# # #             return datetime.datetime.now()
# # #
# # #         @classmethod
# # #     def change_count_of_hands(cls):
# # #         cls.count_of_hands(cls)
# # #
# # # class Student(Human):
# # #     def __init__(self, group):
# # #         self.group = group
# # class Human:
# #     count_of_hands = 2
# #     count_of_legs = 2
# #
# #     def init(self, name, birthday=0):
# #         self.name = name
# #         self.birthday = birthday
# #
# #         def info(self):
# #             print(f"Этого студента зовут {self.name} и он изучает {self.group}")
# #             print(f"Он родился в {self.birthday} году")
# #
# #     def get_name(self):
# #         return self.name
# #     def __repr__(self):
# #         return self.name
# #
# #
# #
# #
# #
# # class Child(Human):
# #     def __init__(self, name, group=None, birthday=None):
# #         if group:
# #             self.group = group
# #
# #         super().__init__(name,birthday)
# #     def info(self):
# #         print(f"Этого студента зовут {self.name} и он изучает {self.group}")
# #         print(f"Он родился в {self.birthday} году")
# # class Group:
# #     def __init__(self,name):
# #         self.name = name
# #         self.students = []
# #     def add_student(self,student):
# #         self.students.append(student)
# #         student.group = self.name
# # java = Group("Java")
# # python = Group("Python")
# # print(java.__dict__)
# # print(python.__dict__)
# class TodoItem:
#     def __init__(self, description):
#         self.description = description
#         self.is_done = False
#
#     def check(self):
#         self.is_done = True
#
#     def uncheck(self):
#         self.is_done = False
#
#
# class Todo:
#     def __init__(self):
#         self.todo_items = []
#
#     def add_todo(self, item):
#         self.todo_items.append(item)
#
#     def list_items(self):
#         for index, item in enumerate(self.todo_items):
#             print(f"{index}: [{item.is_done and 'x' or ' '}] {item.description}")
#
#     def find(self, word):
#         found_items = []
#         for index, item in enumerate(self.todo_items):
#             if word in item.description:
#                 found_items.append((index, item))
#         return found_items
#
#
# def main():
#     todo = Todo()
#     menu = {
#         "1": todo.list_items,
#         "2": lambda: todo.add_todo(TodoItem(input("Enter task description: "))),
#         "3": lambda: todo.todo_items[int(input("Enter task index: "))].check(),
#         "4": lambda: todo.todo_items[int(input("Enter task index: "))].uncheck(),
#         "5": lambda: print(todo.find(input("Enter search word: ")))
#     }
#     while True:
#         print("Menu:")
#         print("1. List all tasks")
#         print("2. Add a task")
#         print("3. Check a task")
#         print("4. Uncheck a task")
#         print("5. Find a task")
#         print("0. Exit")
#         choice = input("Enter your choice: ")
#         if choice == "0":
#             break
#         if choice in menu:
#             menu[choice]()
#         else:
#             print("Invalid choice")
#
#
# if __name__ == "__main__":
#     main()
#
#
