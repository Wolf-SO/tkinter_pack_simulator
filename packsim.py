import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry("800x600")
        master.title("tkinter pack layout simulator")
        self.item_colors = [
            'IndianRed1', 
            'SteelBlue1', 
            'SpringGreen1', 
            'Goldenrod1', 
            'LightPink1', 
            'LightSteelBlue1', 
            'DarkSeaGreen1', 
            'Khaki1']
        self.item_count = len(self.item_colors)
        self.default_item_count = 4

        self.pack(fill=tk.BOTH, expand=True)
        
        self.creates = []
        self.sides = []
        self.fills = []
        self.expands = []
        self.items = []
        
        self.layout_panels()
        self.layout_control_panel()
        self.layout_items()

    def layout_panels(self):
        self.simulation_panel = tk.Frame(self, bg = "white")
        self.control_panel = tk.Frame(self)
        self.control_panel.pack(side=tk.BOTTOM)
        self.simulation_panel.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.contents_frame = tk.Frame(self.simulation_panel, bg="gray31")
        self.contents_frame.pack(side="top", fill="both", expand=True)
        
        for x in range(self.item_count):
            self.items.append(tk.Label(self.contents_frame, text=f"Item {1+x}", bg=self.item_colors[x]))

    def layout_control_panel(self):
        tk.Label(self.control_panel, text="pack").grid(column=0, row=1, sticky="news")
        tk.Label(self.control_panel, text="side").grid(column=0, row=2, sticky="news")
        tk.Label(self.control_panel, text="fill").grid(column=0, row=3, sticky="news")
        tk.Label(self.control_panel, text="expand").grid(column=0, row=4, sticky="news")
        
        for x in range(self.item_count):
            tk.Label(self.control_panel, text=f"Item {1+x}").grid(column=x, row=0)

            self.creates.append(tk.BooleanVar())
            self.creates[x].set(x < self.default_item_count)
            chk1 = ttk.Checkbutton(
                self.control_panel, 
                variable=self.creates[x], 
                command=self.layout_items)
            chk1.grid(column=x, row=1)
        
            self.sides.append(tk.StringVar())
            self.sides[x].set("top")
            cb1 = ttk.Combobox(
                self.control_panel, 
                textvariable=self.sides[x], 
                state="readonly", 
                values=['top', 'bottom', 'left', 'right'], 
                width=7)
            cb1.bind("<<ComboboxSelected>>", self.layout_items)
            cb1.grid(column=x, row=2)

            self.fills.append(tk.StringVar())
            self.fills[x].set("none")
            cb2 = ttk.Combobox(
                self.control_panel,
                textvariable=self.fills[x],
                state="readonly",
                values=['none', 'x', 'y', 'both'], 
                width=7)
            cb2.bind("<<ComboboxSelected>>", self.layout_items)
            cb2.grid(column=x, row=3)

            self.expands.append(tk.BooleanVar())
            self.expands[x].set(False)
            chk2 = ttk.Checkbutton(
                self.control_panel,
                variable=self.expands[x],
                command=self.layout_items)
            chk2.grid(column=x, row=4)

    def layout_items(self,*args):
        for item in self.items:
            item.pack_forget()
        for i, item in enumerate(self.items):
            if self.creates[i].get():
                item.pack(side=self.sides[i].get(), fill=self.fills[i].get(), expand=self.expands[i].get())

root = tk.Tk()
app = Application(master=root)
app.mainloop()
