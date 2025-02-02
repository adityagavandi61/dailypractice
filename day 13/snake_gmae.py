import tkinter as tk
import random

# Constants
WIDTH = 500
HEIGHT = 500
SNAKE_SIZE = 10
SPEED = 100  # Lower is faster

# Colors
BG_COLOR = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game (Tkinter)")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()

        self.snake = [[100, 100], [90, 100], [80, 100]]  # Initial snake
        self.food = [random.randrange(0, WIDTH, SNAKE_SIZE), random.randrange(0, HEIGHT, SNAKE_SIZE)]
        self.direction = "Right"
        
        self.root.bind("<KeyPress>", self.change_direction)
        
        self.run_game()

    def change_direction(self, event):
        key = event.keysym
        if key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Right":
            head_x += SNAKE_SIZE
        elif self.direction == "Left":
            head_x -= SNAKE_SIZE
        elif self.direction == "Up":
            head_y -= SNAKE_SIZE
        elif self.direction == "Down":
            head_y += SNAKE_SIZE

        new_head = [head_x, head_y]

        # Check for collision with walls
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.game_over()
            return
        
        # Check for collision with itself
        if new_head in self.snake:
            self.game_over()
            return

        # Move the snake
        self.snake.insert(0, new_head)

        # Check for eating food
        if new_head == self.food:
            self.food = [random.randrange(0, WIDTH, SNAKE_SIZE), random.randrange(0, HEIGHT, SNAKE_SIZE)]
        else:
            self.snake.pop()  # Remove the last part of the tail

    def draw_objects(self):
        self.canvas.delete("all")
        
        # Draw food
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + SNAKE_SIZE, self.food[1] + SNAKE_SIZE, fill=FOOD_COLOR)

        # Draw snake
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + SNAKE_SIZE, segment[1] + SNAKE_SIZE, fill=SNAKE_COLOR)

    def run_game(self):
        self.move_snake()
        self.draw_objects()
        self.root.after(SPEED, self.run_game)  # Run the game loop after every SPEED milliseconds

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="red", font=("Arial", 20))
        self.root.update()

# Run the game
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
