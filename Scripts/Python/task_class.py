
import sqlalchemy as sql
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import declarative_base, Session

engine = sql.create_engine('sqlite:///reminders.db', echo=True)
Base = declarative_base()


class Priorities: #Типы срочностей, для клика на кнопку-переключения
    @staticmethod
    def __init__(self):
        self.priorities = ["НЕТ СРОЧНОСТИ", "ДО СРОКА", "СРОЧНО"]


class Task(Base):

    __tablename__ = 'reminders'
    _userid = Column(Integer, primary_key=True)


    _tasktext = Column(String)          #Текст напоминания
    _deadlinetype = Column(Integer)     #Тип дедлайна
    _deadlinetime = Column(Integer)     #Время дедлайна
    _completed = Column(Boolean)        #Выполнено ли


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


Base.metadata.create_all(engine)
with Session(engine) as session:
    session.begin()
    example_task = Task(completed=True, deadlinetime=23, deadlinetype=2323, tasktext="Abc")
    try:
        session.add(example_task)
    except:
        session.rollback()
        raise
    else:
        session.commit()
