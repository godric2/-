import tkinter as tk
import random

WIDTH = 300
HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE
SPEED = 500

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[0, 1, 0], [1, 1, 1]]
]

class TetrisGame:
    def __init__(self, root):
        self.root = root
        self.root.title("테트리스")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = None
        self.score = 0
        self.game_over = False
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate)
        self.spawn_piece()
        self.update()

    def spawn_piece(self):
        self.current_piece = random.choice(SHAPES)
        self.piece_x = GRID_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.piece_y = 0

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    self.canvas.create_rectangle(x * BLOCK_SIZE, y * BLOCK_SIZE,
                                                 (x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE, fill="blue", outline="black")

    def draw_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.canvas.create_rectangle((self.piece_x + x) * BLOCK_SIZE, 
                                                 (self.piece_y + y) * BLOCK_SIZE,
                                                 (self.piece_x + x + 1) * BLOCK_SIZE, 
                                                 (self.piece_y + y + 1) * BLOCK_SIZE, fill="red", outline="black")

    def move_left(self, event):
        if self.valid_move(-1, 0):
            self.piece_x -= 1

    def move_right(self, event):
        if self.valid_move(1, 0):
            self.piece_x += 1

    def move_down(self, event):
        if not self.valid_move(0, 1):
            self.lock_piece()
            self.clear_lines()
            if self.game_over_condition():
                self.game_over = True
            else:
                self.spawn_piece()
        else:
            self.piece_y += 1

    def rotate(self, event):
        new_piece = list(zip(*self.current_piece[::-1]))
        if self.valid_move(0, 0, new_piece):
            self.current_piece = new_piece

    def valid_move(self, dx, dy, piece=None):
        piece = piece or self.current_piece
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.piece_x + x + dx
                    new_y = self.piece_y + y + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or self.grid[new_y][new_x]:
                        return False
        return True

    def lock_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.piece_y + y][self.piece_x + x] = 1

    def clear_lines(self):
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_to_clear.append(y)
        for line in lines_to_clear:
            self.grid.pop(line)
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
            self.score += 100

    def game_over_condition(self):
        for x in range(GRID_WIDTH):
            if self.grid[0][x]:
                return True
        return False

    def draw_score(self):
        self.canvas.delete("score")
        self.canvas.create_text(WIDTH // 2, 20, text=f"Score: {self.score}", fill="white", font=("Arial", 16))

    def update(self):
        if not self.game_over:
            self.canvas.delete("all")
            self.draw_grid()
            self.draw_piece()
            self.draw_score()
            self.move_down(None)
            self.root.after(SPEED, self.update)
        else:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, fill="white", font=("Arial", 20, "bold"),
                                    text=f"게임 오버!\n최종 점수: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TetrisGame(root)
    root.mainloop()
