# controllers.py
from .app import create_connection
from .models import Todo


def fetch_all_todos():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM list')
    todos = cursor.fetchall()

    connection.close()

    return todos

def create_todo(todo):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO list (title, completed) VALUES (%s, %s)', (todo.title, todo.completed))
    connection.commit()

    todo.id = cursor.lastrowid

    connection.close()

    return todo
    

def toggle_completion_status(todo_id):
    connection = create_connection()
    cursor = connection.cursor()

    # Fetch the current completion status
    cursor.execute('SELECT completed FROM list WHERE id=%s', (todo_id,))
    current_status = cursor.fetchone()

    if current_status is not None:
        current_status = current_status[0]

        # Toggle completion status
        new_status = 1 - current_status  # 1 if 0, 0 if 1
        cursor.execute('UPDATE list SET completed=%s WHERE id=%s', (new_status, todo_id))

        connection.commit()
        connection.close()
    else:
        raise ValueError(f'Todo with ID {todo_id} not found')

def delete_todo(todo_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM list WHERE id=%s', (todo_id,))
    connection.commit()

    connection.close()
