# 📝 To-Do List Application with Local Storage

A command-line to-do list manager with persistent data storage using JSON files. This application allows you to manage your tasks efficiently with features like task priorities, due dates, and completion tracking.

## 🎯 Features

- ✅ **Add Tasks** - Create new tasks with title, description, priority, and due date
- 📋 **View Tasks** - Display all tasks or filter by status (pending/completed)
- ✏️ **Update Tasks** - Modify existing tasks
- ✓ **Mark Complete** - Mark tasks as completed or incomplete
- 🗑️ **Delete Tasks** - Remove tasks from your list
- 📊 **Statistics** - View task completion statistics
- 💾 **Local Storage** - All data is saved in `tasks.json` for persistence
- 🎨 **User-Friendly Interface** - Clean and intuitive command-line menu

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/fatom-creator/todo-list-app.git
cd todo-list-app
```

2. Run the application:
```bash
python3 todo_app.py
```

## 💻 Usage

When you run the application, you'll see a menu with the following options:

```
========================================
       📝 TO-DO LIST APPLICATION
========================================
1. Add a new task
2. View all tasks
3. View pending tasks
4. View completed tasks
5. Mark task as complete
6. Mark task as incomplete
7. Update a task
8. Delete a task
9. View statistics
10. Exit
========================================
```

### Examples

#### Adding a Task
```
Enter your choice (1-10): 1
Enter task title: Complete Python project
Enter task description (optional): Finish the to-do list app
Enter priority (Low/Medium/High) [Default: Medium]: High
Enter due date (optional): 2024-12-31
✓ Task 'Complete Python project' added successfully!
```

#### Viewing Tasks
```
Enter your choice (1-10): 2

================================================================================
                              TASKS (ALL)
================================================================================

[○] ID: 1 | Complete Python project
    Priority: High | Due: 2024-12-31
    Description: Finish the to-do list app
```

#### Marking a Task Complete
```
Enter your choice (1-10): 5
Enter task ID to mark as complete: 1
✓ Task 1 marked as completed!
```

## 📁 Data Storage

All tasks are automatically saved to `tasks.json` in the application directory. This file is created automatically on first run.

### Sample tasks.json Structure
```json
[
    {
        "id": 1,
        "title": "Complete Python project",
        "description": "Finish the to-do list app",
        "priority": "High",
        "due_date": "2024-12-31",
        "completed": false,
        "created_at": "2024-08-31 10:30:45"
    }
]
```

## 🏗️ Architecture

The application uses a `TodoApp` class that handles all operations:

- **load_tasks()** - Loads tasks from JSON file
- **save_tasks()** - Saves tasks to JSON file
- **add_task()** - Adds a new task
- **view_tasks()** - Displays tasks with optional filtering
- **update_task()** - Updates task information
- **mark_complete()** - Marks a task as completed
- **mark_incomplete()** - Marks a task as incomplete
- **delete_task()** - Deletes a task
- **get_statistics()** - Returns task statistics

## 🎓 Learning Outcomes

This project demonstrates:

- Object-oriented programming (OOP)
- File I/O operations
- JSON data format and manipulation
- Error handling and validation
- User input/output management
- Data persistence
- Python standard library usage (json, os, datetime)

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Created as an educational project by **fatom-creator**

## 🤝 Contributing

Feel free to fork this repository and submit pull requests with improvements!

## 📧 Contact

For questions or suggestions, please reach out via GitHub Issues.
