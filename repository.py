import sqlite3
from faker import Faker
from random import randint
from datetime import datetime


def create_db():
    with open("init_db6.sql", "r") as f:
        sql = f.read()

    with sqlite3.connect("db6.db") as con:
        cur = con.cursor()
        cur.executescript(sql)

def populate_db():
    # sql_command = "--------------"
    sql_command = "\n".join(f'INSERT INTO students (name_student, code_group, address_s, email, n_tel) VALUES ("{Faker("uk").name()}", "ET-22","{Faker("uk").address()}","{Faker().email()}", "{Faker("uk").phone_number()}");' for _ in range(16))
    sql_command = sql_command + "\n".join(f'INSERT INTO students (name_student, code_group, address_s, email, n_tel) VALUES ("{Faker("uk").name()}", "MR-22","{Faker("uk").address()}","{Faker().email()}", "{Faker("uk").phone_number()}");' for _ in range(12))
    sql_command = sql_command + "\n".join(f'INSERT INTO students (name_student, code_group, address_s, email, n_tel) VALUES ("{Faker("uk").name()}", "MN-22","{Faker("uk").address()}","{Faker().email()}", "{Faker("uk").phone_number()}");' for _ in range(17))
    sql_command = sql_command + "\n".join(f'INSERT INTO teachers (teacher_id, name_teacher, address_t, email, n_tel) VALUES ("{randint(20,150)}","{Faker("uk").name()}", "{Faker("uk").address()}","{Faker().email()}", "{Faker("uk").phone_number()}");' for _ in range(5))

    with sqlite3.connect("db6.db") as con:
        cur = con.cursor()
        cur.executescript(sql_command)
    return sql_command


def populate2_db():
  
    sql_command = (f'INSERT INTO groups (code_group, name_group) VALUES ("ET-22", "Підприємництво та торгівля");')
    sql_command = sql_command + "\n" + (f'INSERT INTO groups (code_group, name_group) VALUES ("MR-22", "Маркетинг");')
    sql_command = sql_command + "\n" + (f'INSERT INTO groups (code_group, name_group) VALUES ("MN-22", "Менеджмент");')
    print(sql_command)
    with sqlite3.connect("db6.db") as con:
        cur = con.cursor()
        cur.executescript(sql_command)
    return sql_command

def populate3_db():
  
    sql_command = (f'INSERT INTO disciplines (discip, teacher, name_discipline) VALUES (26, 122, "Математичний аналіз");')
    sql_command = sql_command + "\n" + (f'INSERT INTO disciplines (discip, teacher, name_discipline) VALUES (35, 136, "Психологія");')
    sql_command = sql_command + "\n" + (f'INSERT INTO disciplines (discip, teacher,name_discipline) VALUES (31, 136, "Філософія");')
    sql_command = sql_command + "\n" + (f'INSERT INTO disciplines (discip, teacher,name_discipline) VALUES (12, 40, "Обчислювальний інтелект");')
    sql_command = sql_command + "\n" + (f'INSERT INTO disciplines (discip, teacher,name_discipline) VALUES (22, 85, "Крос-платформне програмування");')
    sql_command = sql_command + "\n" + (f'INSERT INTO disciplines (discip, teacher,name_discipline) VALUES (8, 141, "Професійна та цивільна безпека");')
    sql_command = sql_command + "\n" + (f'INSERT INTO disciplines (discip, teacher,name_discipline) VALUES (17, 40, "Інформаційний маркетинг та менеджмент");')
    # print(sql_command)
    with sqlite3.connect("db6.db") as con:
        cur = con.cursor()
        cur.executescript(sql_command)
    return sql_command

def populate4_db():
    sql_command = ''
    for k in range(800):
        l = randint(1,7)
        match l:
            case 1:
                d = 26
                t = 122
            case 2:
                d = 35
                t = 136
            case 3:
                d = 31
                t = 136
            case 4:
                d = 12
                t = 40
            case 5:
                d = 17
                t = 40
            case 6:
                d = 22
                t = 85
            case 7:
                d = 6
                t = 141
        day = randint(1,30)
        if day >=10:
            day = str(day)
        else:
            day = '0'+str(day)
        d_r = f'2023-0{str(randint(3,7))}-{day}'
        sql_command = sql_command + (f'INSERT INTO ritings (stud_id, discip, riting, teacher, date_r) VALUES ({randint(1,45)}, {d}, {randint(2,5)}, {t}, {d_r} );') + '\n' 
    
    # print(sql_command)
    with sqlite3.connect("db6.db") as con:
        cur = con.cursor()
        cur.executescript(sql_command)
    return sql_command
create_db()
populate_db()
# print(populate_db())
populate2_db()
populate3_db()
populate4_db()