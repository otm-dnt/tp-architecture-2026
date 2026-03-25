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

# Singleton pour SchoolClass
class SchoolClass(Iterable):
    _instance = None  # instance unique

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SchoolClass, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'students'):  # pour éviter de réinitialiser la liste
            self.students = []

    def add_student(self, student):
        self.students.append(student)

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
        return iter(self.students)

    def iter_matter_4(self):
        return Matter4Iterator(self.students)


if __name__ == "__main__":
    # Même instance partout
    school_class1 = SchoolClass()
    school_class2 = SchoolClass()  # c’est la même instance

    school_class1.add_student(Student('J', 10, 12, 13, 15))
    school_class1.add_student(Student('A', 8, 2, 17, 9))
    school_class1.add_student(Student('V', 9, 14, 14, 16))

    # Affichage des classements
    school_class1.rank_matter_1()
    school_class1.rank_matter_2()
    school_class1.rank_matter_3()

    # Parcours matière 4
    print("\nParcours matière 4 avec l'itérateur :")
    for student in school_class1.iter_matter_4():
        print(f"{student.name}: {student.m4}")

    # Vérification du singleton
    print("\nVérification que school_class1 et school_class2 sont identiques :")
    print(school_class1 is school_class2)  # True
