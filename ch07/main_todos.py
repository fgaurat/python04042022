def main():
    todos = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        },
        {
            "userId": 1,
            "id": 4,
            "title": "et porro tempora",
            "completed": True
        },
        {
            "userId": 1,
            "id": 5,
            "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
            "completed": False
        },
        {
            "userId": 1,
            "id": 6,
            "title": "qui ullam ratione quibusdam voluptatem quia omnis",
            "completed": False
        },
        {
            "userId": 1,
            "id": 7,
            "title": "illo expedita consequatur quia in",
            "completed": False
        }]

    with open("todos.csv",'w') as f:
        
        header = ";".join(todos[0].keys())
        print(header,file=f)
        for todo in todos:
            v = todo.values()
            v_str = [str(item) for item in v]
            
            line = ";".join(v_str)

            print(line,file=f)
            # line = f"{todo['id']};{todo['title']};{todo['userId']};{todo['completed']}"
            # print(line,file=f)


if __name__ == '__main__':
    main()


