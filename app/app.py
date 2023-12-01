# app.py
from flask import Flask, request, jsonify, render_template
import mysql.connector
from app.models import Todo
from app.controllers import *


app = Flask(__name__, template_folder='../template')

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'klaus@17320',
    'database': 'todoDB'
}

# Function to create a MySQL connection
def create_connection():
    return mysql.connector.connect(**mysql_config)



@app.route('/todos', methods=['GET'])
def get_todos():
    todos = fetch_all_todos()
    return jsonify({'todos': todos})

@app.route('/add', methods=['POST'])
def add_todo():
    data = request.form
    new_todo = Todo(title=data['title'], completed=data.get('completed', False))
    created_todo = create_todo(new_todo)
    return jsonify({'message': 'Todo created successfully', 'todo': created_todo.__dict__}), 201




@app.route('/toggle/<int:todo_id>', methods=['PUT'])
def toggle_completion(todo_id):
    try:
        toggle_completion_status(todo_id)
        return jsonify({'message': f'Toggle completion status for Todo with ID {todo_id} successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500




@app.route('/delete/<int:todo_id>', methods=['DELETE'])
def delete_todo_route(todo_id):
    delete_todo(todo_id)
    return jsonify({'message': 'Todo with id {todo_id} deleted successfully'})



@app.route('/')
def index():
    todos = fetch_all_todos()
    # print(todos)
    return render_template('base.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)