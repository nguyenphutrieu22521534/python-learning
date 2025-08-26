from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    name: str
    student_id: int
    grades: List[float] = field(default_factory=list)
    is_active: bool = True

    def average_grade(self) -> float:
        """Phương thức tự định nghĩa"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


# Sử dụng
student1 = Student("Alice", 12345, [8.5, 9.0, 7.5])
student2 = Student("Bob", 12346)

print(student1)  # Student(name='Alice', student_id=12345, grades=[8.5, 9.0, 7.5], is_active=True)
print(student2)  # Student(name='Bob', student_id=12346, grades=[], is_active=True)
print(f"Điểm trung bình: {student1.average_grade():.2f}")  # 8.33