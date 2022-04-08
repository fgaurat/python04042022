import requests
from pprint import pprint
import csv


def main():
    file_name = 'todos.csv'
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=";")

        for row in reader:
            pprint(row)




def main_write_csv():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()
    print(len(todos))
    
    with open('todos.csv', 'w', newline='') as csvfile:
        header = todos[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=header,delimiter=';')
        writer.writeheader()
        for todo in todos:
            writer.writerow(todo)





if __name__ == '__main__':
    main()