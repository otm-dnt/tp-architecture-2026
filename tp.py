from collections.abc import Iterable, Iterator

# Classe Student avec 4 matières
class Student:
    def __init__(self, name, m1, m2, m3, m4=0):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4  # 4ème matière par défaut 0

    def average(self):
        return (self.m1 + self.m2 + self.m3 + self.m4) / 4

# Itérateur pour la matière 4
class Matter4Iterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda s: s.m4, reverse=True)
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

    # Classements existants
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

    def __iter__(self):
        # Par défaut on retourne l'itérateur de la matière 1
        return iter(self.students)

    # Méthode spécifique pour l'itérateur de la 4ème matière
    def iter_matter_4(self):
        return Matter4Iterator(self.students)

if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13, 15))
    school_class.add_student(Student('A', 8, 2, 17, 9))
    school_class.add_student(Student('V', 9, 14, 14, 16))

    # Classements existants
    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()

    # Parcours matière 4 avec l'itérateur
    print("\nParcours matière 4 avec l'itérateur :")
    for student in school_class.iter_matter_4():
        print(f"{student.name}: {student.m4}")
