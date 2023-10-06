import mysql.connector
from internet_connect import check_internet_connection


def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1852001",
        database="data"
    )
    return connection


def get_QandA():
    connect = connect_to_db()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM data.q_and_a")
    return cursor.fetchall()


def insert_q_and_a(question, answer):
    con = connect_to_db()
    cur = con.cursor()
    query = "INSERT INTO q_and_a (question, answer) VALUES ('{}', '{}')".format(question, answer)
    cur.execute(query)
    con.commit()


def get_answer_from_QandA(question):
    rows = get_QandA()
    answer = ""
    for row in rows:
        if row[1].lower() in question.lower():
            answer = row[2]
            break
    return answer


# insert_q_and_a("change your name", "change your name")

def get_name():
    con = connect_to_db()
    cur = con.cursor()
    # Select value with name
    query = "SELECT value FROM memory WHERE name='assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]


def update_name(name):
    con = connect_to_db()
    cur = con.cursor()
    # Update value name
    query = "UPDATE memory SET value = '{}' WHERE name ='assistant_name'".format(name)
    cur.execute(query)
    con.commit()


def update_last_seen(last_seen):
    con = connect_to_db()
    cur = con.cursor()
    # Update value name
    query = "UPDATE memory SET value = '{}' WHERE name = 'last_seen'".format(last_seen)
    cur.execute(query)
    con.commit()


def get_last_seen():
    con = connect_to_db()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'last_seen'"
    cur.execute(query)
    return cur.fetchall()[0][0]


def turn_on_speech():
    if check_internet_connection():
        con = connect_to_db()
        cur = con.cursor()
        query = "UPDATE memory SET value = 'on' WHERE name = 'speech'"
        cur.execute(query)
        con.commit()
        return "Speaking..."
    else:
        return "Check your Internet Access"


def turn_off_speech():
    con = connect_to_db()
    cur = con.cursor()
    query = "UPDATE memory SET value = 'off' WHERE name = 'speech'"
    cur.execute(query)
    con.commit()
    return "No Speak!"


def speak_is_on():
    con = connect_to_db()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'speech'"
    cur.execute(query)
    ans = str(cur.fetchall()[0][0])
    if ans == "on":
        return True
    else:
        return False
