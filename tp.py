from collections.abc import Iterable, Iterator

# Décorateur pour ajouter une 4ème matière
def add_matter_4(cls):
    original_init = cls.__init__
    def new_init(self, name, m1, m2, m3, m4=0):
        original_init(self, name, m1, m2, m3)
        self.m4 = m4
    cls.__init__ = new_init
    return cls

@add_matter_4
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3 + getattr(self, 'm4', 0)) / 4

# Itérateurs pour les matières
class MatterIterator(Iterator):
    def __init__(self, students, attr):
        self.sorted_students = sorted(students, key=lambda s: getattr(s, attr), reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.sorted_students):
            student = self.sorted_students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

# Classe représentant la salle de classe
class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    # Méthodes de classement
    def rank_matter_1(self):
        sorted_students = sorted(self.students, key=lambda s: s.m1, reverse=True)
        print("\nClassement matière 1 :")
        for s in sorted_students:
            print(f"{s.name}: {s.m1}")

    def rank_matter_2(self):
        sorted_students = sorted(self.students, key=lambda s: s.m2, reverse=True)
        print("\nClassement matière 2 :")
        for s in sorted_students:
            print(f"{s.name}: {s.m2}")

    def rank_matter_3(self):
        sorted_students = sorted(self.students, key=lambda s: s.m3, reverse=True)
        print("\nClassement matière 3 :")
        for s in sorted_students:
            print(f"{s.name}: {s.m3}")

    def rank_matter_4(self):
        sorted_students = sorted(self.students, key=lambda s: getattr(s, 'm4', 0), reverse=True)
        print("\nClassement matière 4 :")
        for s in sorted_students:
            print(f"{s.name}: {s.m4}")

    # Itérateurs
    def __iter__(self):
        return MatterIterator(self.students, 'm1')

    def iter_matter_2(self):
        return MatterIterator(self.students, 'm2')

    def iter_matter_3(self):
        return MatterIterator(self.students, 'm3')

    def iter_matter_4(self):
        return MatterIterator(self.students, 'm4')


if __name__ == "__main__":
    # Création de la salle de classe
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13, 15))
    school_class.add_student(Student('A', 8, 2, 17, 14))
    school_class.add_student(Student('V', 9, 14, 14, 16))

    # Affichage des moyennes
    print("Moyennes des étudiants :")
    for s in school_class.students:
        print(f"{s.name}: moyenne = {s.average()}")

    # Classements
    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()
    school_class.rank_matter_4()

    # Parcours avec itérateurs
    print("\nParcours matière 1 :")
    for s in school_class:
        print(f"{s.name}: {s.m1}")

    print("\nParcours matière 2 :")
    for s in school_class.iter_matter_2():
        print(f"{s.name}: {s.m2}")

    print("\nParcours matière 3 :")
    for s in school_class.iter_matter_3():
        print(f"{s.name}: {s.m3}")

    print("\nParcours matière 4 :")
    for s in school_class.iter_matter_4():
        print(f"{s.name}: {s.m4}")
