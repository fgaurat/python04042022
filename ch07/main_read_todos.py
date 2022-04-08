

def main():
    todos=[]

    with open('todos.csv') as f:
        lines = f.readlines()

        keys = lines[0].strip().split(';')# ['userId','id','title','completed']
        values = lines[1:]
        
        for value in values:
            item = value.strip().split(';') # [1,1,delectus aut autem,False]
            todo = {}
            # for key in keys:
            for pos,key in enumerate(keys):
                # key = 0
                #  todo['id'] = 1
                todo[key] = item[pos]

            # the_zip = list(zip(keys,item))
            # todo =  dict(the_zip)
            todos.append(todo )

    print(todos)
if __name__ == '__main__':
    main()