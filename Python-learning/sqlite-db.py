import sqlite3

# Create DB
'''create_table(c)'''
def create_table(p):
    print("I am here at top")
    try:
        p.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")
    except:
        print ("DB is already there")

# Static way of entering data
'''enter_data()'''
def enter_data():
    c.execute("INSERT INTO example VALUES ('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES ('Python', 3.3, 'Immediate')")
    c.execute("INSERT INTO example VALUES ('Python', 3.4, 'Expert')")
    conn.commit()

# Dynamic Way of entering data into DB
'''enter_dynamic_data()'''
def enter_dynamic_data():
    lang = input("What language")
    version = float(input("What version?"))
    skill = input("What skill level?")

    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (? , ?, ?)", (lang, version, skill))
    conn.commit()


# read from the database
def read_from_database():
    '''
    what_skill = input("What Skill level that are we looking for? ")
    what_language = input("What language? ")
    sql= "SELECT * from example where Skill = ? and Language = ?"
    for row in c.execute(sql, [(what_skill), (what_language)]):
        print(row)
    '''
    sql = "SELECT * from example"
    for row in c.execute(sql):
        print(row)
    '''
    for row in c.execute(sql, ([what_skill])):
        print(row)
    '''

def update_database():
    sql = "UPDATE example SET Skill = 'expert' where Skill = 'Expert'"
    c.execute(sql)
    sql = "DELETE FROM example where Skill = 'expert'"
    c.execute(sql)
    conn.commit()


print ("I am here at bottom")
conn=sqlite3.connect('tutorial.db')
c=conn.cursor()
create_table(c)
enter_dynamic_data()
update_database()
read_from_database()
conn.close()

