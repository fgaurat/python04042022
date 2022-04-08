import sqlite3

from Todo import Todo


class TodoDAO:


    def __init__(self,db_file) -> None:
        self._con = sqlite3.connect(db_file)

    def findAll(self):
        la_liste = []
        cur = self._con.cursor()
        sql_completed = "SELECT id,title,completed,user_id FROM todos WHERE completed=1"
        result_set = cur.execute(sql_completed)
        # la_liste = [Todo(id,title,completed,userId) for id,title,completed,userId in result_set]

        for id,title,completed,userId in result_set:
            la_liste.append(Todo(id,title,completed,userId))

        return la_liste

    def __del__(self):
        self._con.close()