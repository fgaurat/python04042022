import requests
import sqlite3

from Todo import Todo
from TodoDAO import TodoDAO

def main():
    # t = Todo(1,"le titre",True,12)
    # print(t.title)
    dao = TodoDAO(r'..\data\todos_db.db')

    todos = dao.findAll()
    print(todos)
    # [
    # Todo(1,"...",True,12),
    # ...
    # 
    # ]
    # t = Todo(0,"le titre",True,12)
    # dao.save(t)
    
    # for todo in todos:
    #     print(todo.title)


def main_read():
    con = sqlite3.connect(r'..\data\todos_db.db')
    cur = con.cursor()
    sql_completed = "SELECT id,title FROM todos WHERE completed=1"
    result_set = cur.execute(sql_completed)
    
    for id,title in result_set:
        # id,title = todo
        print(title)


    con.close()

def main_insert():
    """insert todos in sqlite DB"""
    con = sqlite3.connect(r'..\data\todos_db.db')
    cur = con.cursor()

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    for todo in todos:
        sql = f"""INSERT INTO todos(title,completed,user_id) 
        VALUES ('{todo['title']}',{todo['completed']},{todo['userId']})"""
        print(sql)
        cur.execute(sql)
    
    con.commit()
    con.close()

if __name__ == '__main__':
    main()