
import time


class Priorities: #Типы срочностей, для клика на кнопку-переключения
    @staticmethod
    def __init__(self):
        self.priorities = ["НЕТ СРОЧНОСТИ", "ДО СРОКА", "СРОЧНО"]

class Task:
    _tasktext = "" #Текст напоминания
    _deadlinetype = 0 #Тип дедлайна
    _deadlinetime = 0 #Время дедлайна
    _completed = False #Выполнено ли

    def __init__(self, **kwargs):
        self._completed = kwargs["completed"]
        self._deadlinetime = kwargs["deadlinetime"]
        self._deadlinetype = kwargs["deadlinetype"]
        self._tasktext = kwargs["tasktext"]

    def change_complitation(self): #Изменить факт выполнения
        self._completed = not self._completed
        #вызывется скроллбар

    def change_priority(self): #Изменить приоритет
        self._deadlinetype = (self._deadlinetype + 1) % 3

    def set_time(self):
        #Преобразование форматов времени
        pass
