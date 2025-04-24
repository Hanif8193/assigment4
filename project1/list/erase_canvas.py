
import tkinter as tk

CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400

CELL_SIZE: int = 40
ERASER_SIZE: int = 1  # جتنے سیلز کو ایک ساتھ صاف کرنا چاہتے ہیں

# گرڈ بنانے والا فنکشن
def create_grid(canvas):
    cell = []
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        row_cells = []
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="green", outline="black")
            row_cells.append(rect)
        cell.append(row_cells)
    return cell

# ایریزر فنکشن
def erase(event):
    global grid, canvas
    x, y = event.x, event.y
    row = y // CELL_SIZE
    col = x // CELL_SIZE

    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        for i in range(-ERASER_SIZE // 2, ERASER_SIZE // 2 + 1):
            if 0 <= col + i < len(grid[0]):
                canvas.itemconfig(grid[row][col + i], fill="white")

# مین فنکشن
def main():
    global canvas, grid

    root = tk.Tk()
    root.title("Grid Eraser Canvas")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    grid = create_grid(canvas)
    canvas.bind("<B1-Motion>", erase)  # لیفٹ کلک کے ساتھ ڈریگ پر ایریزر چلے گا

    root.mainloop()

if __name__ == "__main__":
    main()
