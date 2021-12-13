from collections import defaultdict
class GradeBook:
    def add_subject(self, subject):
        self.gradebook[self.name][subject] = None

    def add_mark(self, subject, mark):
        self.gradebook[self.name][subject] = mark

    def show_gradebook(self):
        print(self.gradebook)

class Subject(GradeBook):
    def __init__(self):
        self.grades = {}

    def add_student(self, name):
        self.grades[name] = defaultdict(list)

    def show_subject_gradebook(self):
        print()







