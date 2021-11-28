
from sqlalchemy import Column, String, Integer, Boolean, MetaData, Table, create_engine
from sqlalchemy.orm import declarative_base, mapper, sessionmaker

metadata = MetaData()

tasks = Table('tasks', metadata,
    Column('userid', Integer, primary_key=True),
    Column('_tasktext', String),
    Column('_deadlinetype', Integer),
    Column('_deadlinetime', Integer),
    Column('_completed', Boolean)
)


class Task():
    _tasktext = ""       #Текст напоминания
    _deadlinetype = 0   #Тип дедлайна
    _deadlinetime = 0    #Время дедлайна
    _completed = False     #Выполнено ли

    def __init__(self, **kwargs):
        self._completed = kwargs["completed"]
        self._deadlinetime = kwargs["deadlinetime"]
        self._deadlinetype = kwargs["deadlinetype"]
        self._tasktext = kwargs["tasktext"]

    def change_complitation(self):
        self._completed = not self._completed
        #вызывется скроллбар

    def change_priority(self):
        self._deadlinetype = (self._deadlinetype + 1) % 3

    def set_time(self):
        #Преобразование форматов времени
        pass
