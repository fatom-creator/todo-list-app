#!/usr/bin/env python3
"""
To-Do List Application with Local Storage
A command-line to-do list manager with persistent data storage using JSON files.

Features:
- Add, view, update, and delete tasks
- Mark tasks as complete or incomplete
- Persistent storage using JSON
- Priority levels for tasks
- Due dates for tasks
"""

import json
import os
from datetime import datetime

# Configuration
TASKS_FILE = "tasks.json"


class TodoApp:
    """
    A to-do list application with local storage functionality.
    """

    def __init__(self, tasks_file=TASKS_FILE):
        """
        Initialize the TodoApp.
        
        Args:
            tasks_file (str): Path to the JSON file storing tasks
        """
        self.tasks_file = tasks_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Load tasks from the JSON file.
        
        Returns:
            list: List of task dictionaries
        """
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def save_tasks(self):
        """
        Save tasks to the JSON file.
        """
        try:
            with open(self.tasks_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
            print("✓ Tasks saved successfully!")
        except IOError as e:
            print(f"✗ Error saving tasks: {e}")

    def add_task(self, title, description="", priority="Medium", due_date=""):
        """
        Add a new task to the to-do list.
        
        Args:
            title (str): Task title
            description (str): Task description
            priority (str): Task priority (Low, Medium, High)
            due_date (str): Task due date
        """
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Task '{title}' added successfully!")

    def view_tasks(self, filter_by="all"):
        """
        View all tasks or filter by status.
        
        Args:
            filter_by (str): 'all', 'completed', or 'pending'
        """
        if not self.tasks:
            print("\n📋 No tasks found. Add a task to get started!\n")
            return

        filtered_tasks = self.tasks
        if filter_by == "completed":
            filtered_tasks = [t for t in self.tasks if t["completed"]]
        elif filter_by == "pending":
            filtered_tasks = [t for t in self.tasks if not t["completed"]]

        if not filtered_tasks:
            print(f"\n📋 No {filter_by} tasks found.\n")
            return

        print(f"\n{'='*80}")
        print(f"{'TASKS (' + filter_by.upper() + ')':^80}")
        print(f"{'='*80}\n")

        for task in filtered_tasks:
            status = "✓" if task["completed"] else "○"
            print(f"[{status}] ID: {task['id']} | {task['title']}")
            print(f"    Priority: {task['priority']} | Due: {task['due_date'] or 'Not set'}")
            if task["description"]:
                print(f"    Description: {task['description']}")
            print()

    def update_task(self, task_id, title=None, description=None, priority=None, due_date=None):
        """
        Update an existing task.
        
        Args:
            task_id (int): The ID of the task to update
            title (str): New task title
            description (str): New task description
            priority (str): New task priority
            due_date (str): New task due date
        """
        for task in self.tasks:
            if task["id"] == task_id:
                if title:
                    task["title"] = title
                if description is not None:
                    task["description"] = description
                if priority:
                    task["priority"] = priority
                if due_date is not None:
                    task["due_date"] = due_date
                self.save_tasks()
                print(f"✓ Task {task_id} updated successfully!")
                return
        print(f"✗ Task with ID {task_id} not found.")

    def mark_complete(self, task_id):
        """
        Mark a task as completed.
        
        Args:
            task_id (int): The ID of the task to mark complete
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"✓ Task {task_id} marked as completed!")
                return
        print(f"✗ Task with ID {task_id} not found.")

    def mark_incomplete(self, task_id):
        """
        Mark a task as incomplete.
        
        Args:
            task_id (int): The ID of the task to mark incomplete
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = False
                self.save_tasks()
                print(f"✓ Task {task_id} marked as incomplete!")
                return
        print(f"✗ Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """
        Delete a task from the to-do list.
        
        Args:
            task_id (int): The ID of the task to delete
        """
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()
                print(f"✓ Task '{deleted_task['title']}' deleted successfully!")
                return
        print(f"✗ Task with ID {task_id} not found.")

    def get_statistics(self):
        """
        Get statistics about tasks.
        
        Returns:
            dict: Statistics including total, completed, and pending tasks
        """
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["completed"])
        pending = total - completed
        return {
            "total": total,
            "completed": completed,
            "pending": pending
        }

    def display_statistics(self):
        """
        Display task statistics.
        """
        stats = self.get_statistics()
        print(f"\n{'='*40}")
        print(f"{'📊 STATISTICS':^40}")
        print(f"{'='*40}")
        print(f"Total Tasks: {stats['total']}")
        print(f"Completed: {stats['completed']}")
        print(f"Pending: {stats['pending']}")
        if stats["total"] > 0:
            completion_rate = (stats["completed"] / stats["total"]) * 100
            print(f"Completion Rate: {completion_rate:.1f}%")
        print(f"{'='*40}\n")


def display_menu():
    """
    Display the main menu.
    """
    print(f"\n{'='*40}")
    print(f"{'📝 TO-DO LIST APPLICATION':^40}")
    print(f"{'='*40}")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. View pending tasks")
    print("4. View completed tasks")
    print("5. Mark task as complete")
    print("6. Mark task as incomplete")
    print("7. Update a task")
    print("8. Delete a task")
    print("9. View statistics")
    print("10. Exit")
    print(f"{'='*40}")


def main():
    """
    Main application loop.
    """
    app = TodoApp()

    print("\n🎉 Welcome to the To-Do List Application!")
    print("📝 Your tasks are automatically saved to tasks.json\n")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-10): ").strip()

        if choice == "1":
            # Add a new task
            title = input("Enter task title: ").strip()
            if not title:
                print("✗ Task title cannot be empty.")
                continue
            description = input("Enter task description (optional): ").strip()
            priority = input("Enter priority (Low/Medium/High) [Default: Medium]: ").strip() or "Medium"
            due_date = input("Enter due date (optional): ").strip()
            app.add_task(title, description, priority, due_date)

        elif choice == "2":
            # View all tasks
            app.view_tasks()

        elif choice == "3":
            # View pending tasks
            app.view_tasks(filter_by="pending")

        elif choice == "4":
            # View completed tasks
            app.view_tasks(filter_by="completed")

        elif choice == "5":
            # Mark task as complete
            try:
                task_id = int(input("Enter task ID to mark as complete: ").strip())
                app.mark_complete(task_id)
            except ValueError:
                print("✗ Invalid task ID. Please enter a number.")

        elif choice == "6":
            # Mark task as incomplete
            try:
                task_id = int(input("Enter task ID to mark as incomplete: ").strip())
                app.mark_incomplete(task_id)
            except ValueError:
                print("✗ Invalid task ID. Please enter a number.")

        elif choice == "7":
            # Update a task
            try:
                task_id = int(input("Enter task ID to update: ").strip())
                title = input("Enter new title (leave blank to skip): ").strip()
                description = input("Enter new description (leave blank to skip): ").strip()
                priority = input("Enter new priority (leave blank to skip): ").strip()
                due_date = input("Enter new due date (leave blank to skip): ").strip()

                app.update_task(
                    task_id,
                    title=title if title else None,
                    description=description if description else None,
                    priority=priority if priority else None,
                    due_date=due_date if due_date else None
                )
            except ValueError:
                print("✗ Invalid task ID. Please enter a number.")

        elif choice == "8":
            # Delete a task
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                app.delete_task(task_id)
            except ValueError:
                print("✗ Invalid task ID. Please enter a number.")

        elif choice == "9":
            # View statistics
            app.display_statistics()

        elif choice == "10":
            # Exit
            print("\n👋 Thank you for using To-Do List Application!")
            print("✓ Your tasks have been saved. See you next time!\n")
            break

        else:
            print("✗ Invalid choice. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()
