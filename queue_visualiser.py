import tkinter as tk
from tkinter import messagebox

NODE_WIDTH = 80
NODE_HEIGHT = 40
VERTICAL_GAP = 10
HORIZONTAL_GAP = 40
CANVAS_WIDTH = 700
CANVAS_HEIGHT = 200

class QueueVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Visualizer")

        self.queue = []

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack(pady=20)

        control_frame = tk.Frame(root)
        control_frame.pack()

        tk.Label(control_frame, text="Enqueue Value:").grid(row=0, column=0)
        self.push_entry = tk.Entry(control_frame, width=10)
        self.push_entry.grid(row=0, column=1)

        push_btn = tk.Button(control_frame, text="Enqueue", command=self.enqueue_value)
        push_btn.grid(row=0, column=2, padx=5)

        pop_btn = tk.Button(control_frame, text="Dequeue", command=self.dequeue_value)
        pop_btn.grid(row=1, column=2, pady=5)

        self.status_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.draw_queue()

    def draw_node(self, x, y, data):
        rect = self.canvas.create_rectangle(x, y, x + NODE_WIDTH, y + NODE_HEIGHT, fill="lightblue", outline="black", width=2)
        self.canvas.create_text(x + NODE_WIDTH/2, y + NODE_HEIGHT/2, text=str(data), font=("Arial", 16))
        return rect

    def draw_queue(self):
        self.canvas.delete("all")
        x = 20
        y = 40


        centers = []

        # Draw nodes
        for i, val in enumerate(self.queue):
            self.draw_node(x, y, val)
            centers.append((x + NODE_WIDTH // 2, y + NODE_HEIGHT // 2))
            x += NODE_WIDTH + HORIZONTAL_GAP



    def enqueue_value(self):
        try:
            val = int(self.push_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter an integer value to enqueue.")
            return
        self.queue.append(val)
        self.push_entry.delete(0, tk.END)
        self.status_label.config(text=f"Enqueued {val}")
        self.draw_queue()

    def dequeue_value(self):
        if len(self.queue) == 0:
            messagebox.showinfo("Empty queue", "queue is empty. Cannot pop.")
            return
        val = self.queue.pop(0)
        self.status_label.config(text=f"deqeued {val} from queue")
        self.draw_queue()

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueVisualizer(root)


    root.mainloop()
