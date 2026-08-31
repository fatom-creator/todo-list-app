#!/usr/bin/env python3
"""
Example usage of the TodoApp class programmatically (without the interactive menu).
"""

from todo_app import TodoApp


def example_usage():
    """
    Demonstrates how to use the TodoApp class in your own scripts.
    """
    # Create an instance of TodoApp
    app = TodoApp("my_tasks.json")

    print("\n🎯 Example Usage of TodoApp\n")

    # Add some tasks
    print("1️⃣ Adding tasks...")
    app.add_task(
        title="Learn Python",
        description="Complete Python basics course",
        priority="High",
        due_date="2024-09-15"
    )

    app.add_task(
        title="Read a book",
        description="Read 'Clean Code' by Robert Martin",
        priority="Medium",
        due_date="2024-10-01"
    )

    app.add_task(
        title="Exercise",
        priority="Low",
        due_date="2024-09-05"
    )

    # View all tasks
    print("\n2️⃣ Viewing all tasks...")
    app.view_tasks()

    # View pending tasks
    print("3️⃣ Viewing pending tasks...")
    app.view_tasks(filter_by="pending")

    # Mark a task as complete
    print("4️⃣ Marking task 1 as complete...")
    app.mark_complete(1)

    # View completed tasks
    print("\n5️⃣ Viewing completed tasks...")
    app.view_tasks(filter_by="completed")

    # Update a task
    print("\n6️⃣ Updating task 2...")
    app.update_task(
        task_id=2,
        due_date="2024-09-30",
        priority="High"
    )

    # Display statistics
    print("\n7️⃣ Displaying statistics...")
    app.display_statistics()

    # View all tasks again
    print("8️⃣ Viewing all tasks after updates...")
    app.view_tasks()


if __name__ == "__main__":
    example_usage()
