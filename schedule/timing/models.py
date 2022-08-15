from django.utils import timezone
from django.db import models

class student(models.Model):
    student_name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.student_name
    
class PossibleTimeTable(models.Model):
    student_name= models.ForeignKey(student, on_delete=models.CASCADE)
    start_lesson_datetime = models.DateTimeField()
    end_lesson_datetime = models.DateTimeField()
    
    
    def __str__(self) -> str:
        return f"{self.student_name}, с {self.start_lesson_datetime} по {self.end_lesson_datetime}"
    
    @classmethod
    def get_time_by_date_range(cls, name, start_date, end_date):
        "Этот метод позволяет получить записи о доступном времени по имени студента и диапазону дат"
        student_id = student.objects.get(student_name = name)
        student_id = getattr(student_id, "id")
        end_date += " 23:59:59"
        query_res = PossibleTimeTable.objects.filter(student_name=student_id, start_lesson_datetime__gte=start_date, end_lesson_datetime__lte = end_date)
        if query_res.count() > 0:
            return query_res
        else:
            return "Нет совпадающих дат"
    
    @classmethod
    def add_possible_time(cls, name, date, start_time, end_time):
        "Добавить свободные дату и время"
        student_id = student.objects.get(student_name = name)
        student_id = getattr(student_id, "id")
        print(student_id)
        query = PossibleTimeTable(id = student_id, lesson_date = date, lesson_time_start = start_time, lesson_time_end = end_time)
        query.save()
        return "Success"
    

class LessonTimeTable(models.Model):
    student_name= models.ForeignKey(student, on_delete=models.CASCADE)
    start_lesson_datetime = models.DateTimeField()
    end_lesson_datetime = models.DateTimeField()
   
    def __str__(self) -> str:
        return f"{self.student_name}, с {self.start_lesson_datetime} по {self.end_lesson_datetime}"
    
    def check_match(cls, name, start_date, end_date, time):
        "этот метод проверяет совпадает ли время предложенное учителем среди диапазона дат записей ученика"
        pass
    
    def add_lesson_time(self, cls, name, date, time):
        "Этот метод добавляет дату и время следующего занятия для ученика"
        pass
    
    