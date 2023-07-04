import tkinter as tk
from tkinter import messagebox


def validate_entry(value):
    if value.isdigit() and 1 <= int(value) <= 9:
        return True
    elif value == '':
        return True
    else:
        return False

def solve_sudoku(grid):
    if not find_empty_cell(grid):
        return True

    row, col = find_empty_cell(grid)

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False


def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def is_valid(grid, row, col, num):
    # Check row validity
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column validity
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check subgrid validity
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def print_grid(grid):
    for row in grid:
        print(row)


def solve_button_click():
    # Extract the numbers from the entry widgets and create the Sudoku grid
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entry_widgets[i][j].get()
            if value == '':
                value = '0'
            row.append(int(value))
        grid.append(row)

    # Solve the Sudoku puzzle
    if solve_sudoku(grid):
        # Update the entry widgets with the solved puzzle
        for i in range(9):
            for j in range(9):
                entry_widgets[i][j].delete(0, tk.END)
                entry_widgets[i][j].insert(tk.END, str(grid[i][j]))
    else:
        messagebox.showinfo('No Solution', 'No solution exists for the Sudoku puzzle.')


# Create the main window
window = tk.Tk()
window.title('Sudoku Solver')

# Create the entry widgets for inputting the Sudoku grid
entry_widgets = []
for i in range(9):
    row_widgets = []
    for j in range(9):
        validate_cmd = (window.register(validate_entry), '%P')
        entry = tk.Entry(window, width=2, font=('Arial', 16), validate='key', validatecommand=validate_cmd)
        entry.grid(row=i, column=j, padx=1, pady=1)
        row_widgets.append(entry)
    entry_widgets.append(row_widgets)

# Create the Solve button
solve_button = tk.Button(window, text='Solve', command=solve_button_click)
solve_button.grid(row=9, column=0, columnspan=9, padx=10, pady=10)

# Start the main event loop
window.mainloop()

