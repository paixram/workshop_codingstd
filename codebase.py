class Student:
    """Clase que representa a un estudiante y gestiona sus calificaciones."""

    def __init__(self, student_id: str, name: str):
        if not student_id or not name:
            raise ValueError("El ID y el nombre del estudiante no pueden estar vacíos.")
        self.id = student_id
        self.name = name
        self.grades: list[float] = []
        self.is_passed = False
        self.honor_roll = False

    def add_grade(self, grade: float):
        """Agrega una calificación válida (0–100)."""
        if not isinstance(grade, (int, float)):
            print(f"Calificación inválida: {grade}. Debe ser numérica.")
            return
        if 0 <= grade <= 100:
            self.grades.append(float(grade))
        else:
            print(f"Calificación fuera de rango: {grade}")

    def calculate_average(self) -> float:
        """Calcula el promedio de calificaciones."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self) -> str:
        """Convierte el promedio a una nota literal."""
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        return "F"

    def update_status(self):
        """Actualiza el estado de aprobación y honor."""
        avg = self.calculate_average()
        self.is_passed = avg >= 60
        self.honor_roll = avg >= 90

    def remove_grade(self, index: int):
        """Elimina una calificación por índice."""
        try:
            del self.grades[index]
        except IndexError:
            print(f"Error: no existe calificación en el índice {index}.")

    def report(self):
        """Muestra un reporte completo del estudiante."""
        avg = self.calculate_average()
        print("===== REPORTE DEL ESTUDIANTE =====")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.name}")
        print(f"Calificaciones: {self.grades}")
        print(f"Promedio: {avg:.2f}")
        print(f"Nota literal: {self.determine_letter_grade()}")
        print(f"Estado: {'Aprobado' if self.is_passed else 'Reprobado'}")
        print(f"Cuadro de honor: {'Sí' if self.honor_roll else 'No'}")
        print("==================================\n")


def start_run():
    """Ejecuta un caso de prueba del sistema."""
    student = Student("001", "Luis Inga")
    student.add_grade(95)
    student.add_grade(88)
    student.add_grade(70)
    student.update_status()
    student.report()


if __name__ == "__main__":
    start_run()