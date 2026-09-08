from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('mft.db')



class Student(Model):
    name = CharField(max_length=15)
    family = CharField(max_length=15)
    
    
    class Meta:
        database = db
        table_name = 'st'
        
Student.create_table()