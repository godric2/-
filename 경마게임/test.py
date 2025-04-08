import tkinter as tk
import random

NUM_HORSES = 5
FINISH_LINE = 700
TRACK_HEIGHT = 80
STEP_DELAY = 100  

class HorseRaceGame:
    def __init__(self, root):
        self.root = root
        self.root.title("경마 게임")
        self.canvas = tk.Canvas(root, width=800, height=TRACK_HEIGHT * NUM_HORSES + 50, bg="green")
        self.canvas.pack()

        self.horses = []
        self.positions = [0] * NUM_HORSES
        self.running = False

        self.start_button = tk.Button(root, text="🏁 경주 시작!", command=self.start_race, font=("Arial", 14))
        self.start_button.pack(pady=10)

        self.draw_track()
        self.draw_finish_line()

    def draw_track(self):
        for i in range(NUM_HORSES):
            y = TRACK_HEIGHT * i + 30
            self.canvas.create_line(0, y, FINISH_LINE + 50, y, fill="white", dash=(4, 2))
            horse = self.canvas.create_oval(10, y - 20, 50, y + 20, fill=self.random_color())
            self.horses.append(horse)

    def draw_finish_line(self):
        for i in range(NUM_HORSES):
            top = TRACK_HEIGHT * i + 10
            bottom = TRACK_HEIGHT * i + 50
            for j in range(0, 40, 10):
                color = "white" if (j // 10) % 2 == 0 else "black"
                self.canvas.create_rectangle(FINISH_LINE, top + j, FINISH_LINE + 10, top + j + 10, fill=color, outline=color)

    def random_color(self):
        return f"#{random.randint(0, 0xFFFFFF):06x}"

    def start_race(self):
        if not self.running:
            self.running = True
            self.positions = [0] * NUM_HORSES
            self.canvas.delete("result")
            self.move_horses()

    def move_horses(self):
        for i in range(NUM_HORSES):
            step = random.randint(1, 10)
            self.positions[i] += step
            self.canvas.move(self.horses[i], step, 0)

            coords = self.canvas.coords(self.horses[i])
            if coords[2] >= FINISH_LINE:
                self.running = False
                winner = i + 1
                self.canvas.create_text(
                    400, TRACK_HEIGHT * NUM_HORSES + 30,
                    text=f" 말 {winner}번 우승! ", font=("Arial", 18), fill="yellow", tags="result"
                )
                return

        if self.running:
            self.root.after(STEP_DELAY, self.move_horses)

if __name__ == "__main__":
    root = tk.Tk()
    game = HorseRaceGame(root)
    root.mainloop()
