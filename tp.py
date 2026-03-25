from collections.abc import Iterable, Iterator

# Classe étudiant
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3


# Itérateur pour la matière 1
class Matter1Iterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.m1, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.sorted_students):
            student = self.sorted_students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration


# Itérateur pour la matière 2
class Matter2Iterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.m2, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.sorted_students):
            student = self.sorted_students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration


# Itérateur pour la matière 3
class Matter3Iterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.m3, reverse=True)
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

    # Méthodes de tri classiques
    def rank_matter_1(self):
        sorted_students = sorted(self.students, key=lambda s: s.m1, reverse=True)
        print("\nClassement matière 1 :")
        for student in sorted_students:
            print(f"{student.name}: {student.m1}")

    def rank_matter_2(self):
        sorted_students = sorted(self.students, key=lambda s: s.m2, reverse=True)
        print("\nClassement matière 2 :")
        for student in sorted_students:
            print(f"{student.name}: {student.m2}")

    def rank_matter_3(self):
        sorted_students = sorted(self.students, key=lambda s: s.m3, reverse=True)
        print("\nClassement matière 3 :")
        for student in sorted_students:
            print(f"{student.name}: {student.m3}")

    # Itérateurs
    def __iter__(self):
        return Matter1Iterator(self.students)

    def iter_matter_2(self):
        return Matter2Iterator(self.students)

    def iter_matter_3(self):
        return Matter3Iterator(self.students)


# Main
if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    # Affichage des moyennes
    print("Moyennes des étudiants :")
    for student in school_class.students:
        print(f"{student.name}: moyenne = {student.average()}")

    # Tri matière 1, 2 et 3
    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()

    # Parcours avec itérateurs
    print("\nParcours matière 1 avec l'itérateur :")
    for student in school_class:
        print(f"{student.name}: {student.m1}")

    print("\nParcours matière 2 avec l'itérateur :")
    for student in school_class.iter_matter_2():
        print(f"{student.name}: {student.m2}")

    print("\nParcours matière 3 avec l'itérateur :")
    for student in school_class.iter_matter_3():
        print(f"{student.name}: {student.m3}")
