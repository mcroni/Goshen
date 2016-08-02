from pony.orm import *

db = Database('sqlite','details.sqlite',create_db = True)


class Person(db.Entity):
    name = Required(str)
    number = Required(int)






sql_debug(True)
db.generate_mapping(create_tables=True)

with db_session:
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Me', number='00271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Love', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Me', number='00271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Love', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Me', number='00271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Love', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Me', number='00271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Love', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Me', number='00271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Love', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Me', number='00271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Love', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Me', number='00271808617')
    p = Person(name='Kate', number='0271808617')
    p = Person(name='Love', number='0271808617')
    p = Person(name='Kate', number='0271808617')
    
