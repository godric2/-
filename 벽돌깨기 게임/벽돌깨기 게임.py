import tkinter as tk
import random

WIDTH = 500
HEIGHT = 400
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
BALL_SIZE = 15
BRICK_ROWS = 5
BRICK_COLUMNS = 8
BRICK_WIDTH = WIDTH // BRICK_COLUMNS
BRICK_HEIGHT = 20

class BrickBreaker:
    def __init__(self, root):
        self.root = root
        self.root.title("벽돌 깨기 게임")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.paddle = self.canvas.create_rectangle(200, 350, 200 + PADDLE_WIDTH, 350 + PADDLE_HEIGHT, fill="white")
        self.ball = self.canvas.create_oval(245, 200, 245 + BALL_SIZE, 200 + BALL_SIZE, fill="red")
        self.ball_dx = 3
        self.ball_dy = -3

        self.bricks = []
        self.create_bricks()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.update()

    def create_bricks(self):
        colors = ["red", "orange", "yellow", "green", "blue"]
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLUMNS):
                x1 = col * BRICK_WIDTH
                y1 = row * BRICK_HEIGHT
                x2 = x1 + BRICK_WIDTH
                y2 = y1 + BRICK_HEIGHT
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colors[row % len(colors)], width=2)
                self.bricks.append(brick)

    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)

    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)

    def update(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)

        if ball_coords[0] <= 0 or ball_coords[2] >= WIDTH:
            self.ball_dx *= -1
        if ball_coords[1] <= 0:
            self.ball_dy *= -1
        if ball_coords[3] >= HEIGHT:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over", fill="white", font=("Arial", 24))
            return


        if self.check_collision(ball_coords, paddle_coords):
            self.ball_dy *= -1

        bricks_to_remove = []
        collision_occurred = False

        for brick in self.bricks:
            if self.check_collision(ball_coords, self.canvas.coords(brick)):
                bricks_to_remove.append(brick)
                collision_occurred = True

        for brick in bricks_to_remove:
            self.canvas.delete(brick)
            self.bricks.remove(brick)

        if collision_occurred:
            self.ball_dy *= -1

        if not self.bricks:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="승리", fill="white", font=("Arial", 24))
            return

        self.root.after(20, self.update)

    def check_collision(self, ball, obj):
        return not (ball[2] < obj[0] or ball[0] > obj[2] or ball[3] < obj[1] or ball[1] > obj[3])

if __name__ == "__main__":
    root = tk.Tk()
    game = BrickBreaker(root)
    root.mainloop()
