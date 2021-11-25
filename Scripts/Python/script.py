from header import *

engine = create_engine('sqlite:///tasks.db', echo=True)

#Проверяю, существует ли вообще таблица
with engine.connect() as con:
    if not engine.dialect.has_table(con, 'tasks'):
        metadata.create_all(engine) #Создаю, если нет

meta = MetaData(engine)
tasks = Table('tasks', meta, autoload=True)
mapper(Task, tasks)
Session = sessionmaker(bind=engine)
session = Session()
