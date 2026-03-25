from collections.abc import Iterable, Iterator
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

# Classe représentant la salle de classe
class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    def rank_matter_1(self):
        sorted_students = sorted(self.students, key=lambda s: s.m1, reverse=True)
        print("\nClassement matière 1 :")
        for student in sorted_students:
            print(f"{student.name}: {student.m1}")
            # Classement matière 2
    def rank_matter_2(self):
        sorted_students = sorted(self.students, key=lambda s: s.m2, reverse=True)
        print("\nClassement matière 2 :")
        for student in sorted_students:
            print(f"{student.name}: {student.m2}")
            # Classement matière 3
    def rank_matter_3(self):
        sorted_students = sorted(self.students, key=lambda s: s.m3, reverse=True)
        print("\nClassement matière 3 :")
        for student in sorted_students:
            print(f"{student.name}: {student.m3}")
    def __iter__(self):
        return Matter1Iterator(self.students)
        
if __name__ == "__main__":
    # Création d'une instance de la classe
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    # Affichage des moyennes pour vérifier
    print("Moyennes des étudiants :")
    for student in school_class.students:
        print(f"{student.name}: moyenne = {student.average()}")

    # Tri matière 1
    school_class.rank_matter_1()
    # Tri matière 2
    school_class.rank_matter_2()

    # Tri matière 3
    school_class.rank_matter_3()
    
    # Parcours matière 1 avec l'itérateur
    print("\nParcours des étudiants avec l'itérateur matière 1 :")
    for student in school_class:
        print(f"{student.name}: {student.m1}")

  
