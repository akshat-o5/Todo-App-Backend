# Todo App

A basic Todo App built with Flask and MySQL.
Stay organized and boost your productivity with our intuitive ToDo app! Effortlessly manage tasks, set priorities, and track your progress with a user-friendly interface. Whether you're tackling work projects or personal goals, this app simplifies your day, helping you stay focused on what matters most. Never miss a deadline again – download our ToDo app and take control of your tasks with ease!

## Features
- Add, update, and delete Todo items.
- Mark Todo items as completed or not completed.

## Getting Started

### Prerequisites
- Python (>=3.6)
- MySQL server

### Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/todo-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd todo-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure your MySQL database:

    Update the `mysql_config` dictionary in `app.py` with your database details.

5. Run the application:

    ```bash
    python app.py
    ```

    The Todo App should now be running locally. Open your web browser and go to http://localhost:5000 to access the app.

## Usage
- Open the app in your web browser.
- Add new Todo items by entering the title in the provided form and clicking the "Add" button.
- View, update, or delete existing Todo items.
- Toggle the completion status of Todo items.

## API Endpoints
- **GET /todos:** Retrieve all Todo items.
- **POST /add:** Add a new Todo item.
- **PUT /update/<int:todo_id>:** Update the completion status of a Todo item.
- **DELETE /delete/<int:todo_id>:** Delete a Todo item.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Blog
For more information, do checkout my blog [Blog](https://akshato2.hashnode.dev/building-a-todo-app-with-flask-and-mysql-a-comprehensive-guide)
