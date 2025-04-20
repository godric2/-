import tkinter as tk
import random
WIDTH = 400
HEIGHT = 400
SPEED = 100
SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("스네이크 게임")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.running = True
        self.food = self.spawn_food()
        self.score = 0  

        self.root.bind("<KeyPress>", self.change_direction)
        self.update()

    def spawn_food(self):
        while True:
            x = random.randint(0, (WIDTH - SIZE) // SIZE) * SIZE
            y = random.randint(1, (HEIGHT - SIZE) // SIZE) * SIZE  
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        key = event.keysym
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if key in ["Up", "Down", "Left", "Right"]:
            if key != opposite.get(self.direction):
                self.direction = key

    def move(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= SIZE
        elif self.direction == "Down":
            y += SIZE
        elif self.direction == "Left":
            x -= SIZE
        elif self.direction == "Right":
            x += SIZE

        new_head = (x, y)

        if (
            x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT
            or new_head in self.snake
        ):
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
            self.score += 1 
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")

        self.canvas.create_text(WIDTH//2, 10, fill="white", font=("Helvetica", 14, "bold"),
                                text=f"Score: {self.score}")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="green", outline="")
        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx + SIZE, fy + SIZE, fill="red", outline="")

    def update(self):
        if self.running:
            self.move()
            self.draw()
            self.root.after(SPEED, self.update)
        else:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, fill="white", font=("Helvetica", 20, "bold"),
                                    text=f"게임 오버!\n최종 점수: {self.score}")
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
