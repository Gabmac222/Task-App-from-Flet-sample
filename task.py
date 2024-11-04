import flet as ft

def main(page: ft.Page):
    # Set theme colors and properties
    page.bgcolor = "#1a237e"  # Dark blue background
    page.title = "Task Manager"
    page.window_width = 600
    page.window_height = 600
    page.theme_mode = "dark"

    # Task list to store all tasks
    tasks = []

    # Function to add new task
    def add_task(e):
        if task_input.value:
            # Create task row with delete button
            task_row = ft.Row(
                controls=[
                    ft.Text(
                        task_input.value,
                        color="white",
                        size=16,
                        expand=True
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE,
                        icon_color="white",
                        on_click=lambda e, task=len(tasks): delete_task(e, task)
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
            
            tasks.append(task_row)
            task_list.controls.append(task_row)
            task_input.value = ""
            page.update()

    # Function to delete task
    def delete_task(e, task_index):
        task_list.controls.pop(task_index)
        tasks.pop(task_index)
        page.update()

    # Create input field and add button
    task_input = ft.TextField(
        hint_text="Enter your task",
        border_color="white",
        color="white",
        expand=True
    )

    add_button = ft.ElevatedButton(
        text="Add Task",
        style=ft.ButtonStyle(
            bgcolor={"": "#3949ab"},  # Lighter blue
            color={"": "white"}
        ),
        on_click=add_task
    )

    # Create container for input controls
    input_row = ft.Row(
        controls=[
            task_input,
            add_button
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Create container for task list
    task_list = ft.Column(spacing=10)

    # Main container
    main_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Task Manager",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color="white"
                ),
                input_row,
                task_list
            ],
            spacing=20
        ),
        padding=20
    )

    page.add(main_container)

ft.app(target=main)