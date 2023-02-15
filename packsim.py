import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("800x600")
        master.title("tkinter pack layout simulator")
        self.item_colors = ['IndianRed1', 'SteelBlue1', 'SpringGreen1', 'Goldenrod1', 'LightPink1','LightSteelBlue1', 'DarkSeaGreen1', 'Khaki1']
        self.item_count = len(self.item_colors)
        self.default_item_count = 4

        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        self.layout_panels()
        self.layout_control_panel()
        self.layout_items()

    def layout_panels(self):
        self.simulation_panel = tk.Frame(self, bg = "white")
        self.control_panel = tk.Frame(self)
        self.control_panel.pack(side=tk.BOTTOM)
        self.simulation_panel.pack(side=tk.TOP,expand=True, fill=tk.BOTH)
        self.contents_frame = tk.Frame(self.simulation_panel, bg="gray31")
        self.contents_frame.pack(side="top", fill="both",expand=True)

    def layout_control_panel(self):
        tk.Label(self.control_panel, text="pack").grid(column=0, row=1, sticky="news")
        tk.Label(self.control_panel, text="side").grid(column=0, row=2, sticky="news")
        tk.Label(self.control_panel, text="fill").grid(column=0, row=3, sticky="news")
        tk.Label(self.control_panel, text="expand").grid(column=0, row=4, sticky="news")
        for x in range(self.item_count):
            tk.Label(self.control_panel, text="Item " + str(x+1)).grid(column=x, row=0)

        self.creates = []
        
        self.sides = []

        self.fills = []

        self.expands = []

        for y in range(self.item_count):
        
            self.creates.append(tk.BooleanVar())
            self.creates[y].set(y < self.default_item_count)
            chk1 = ttk.Checkbutton(self.control_panel,variable=self.creates[y],command=self.layout_items)
            chk1.grid(column=y,row=1)
        
            self.sides.append(tk.StringVar())
            self.sides[y].set("top")
            cb1 = ttk.Combobox(self.control_panel,textvariable=self.sides[y],state="readonly",values=['top', 'bottom', 'left', 'right'], width=7)
            cb1.bind("<<ComboboxSelected>>", self.layout_items)
            cb1.grid(column=y,row=2)

            self.fills.append(tk.StringVar())
            self.fills[y].set("none")
            cb2 = ttk.Combobox(self.control_panel,textvariable=self.fills[y],state="readonly",values=['none', 'x', 'y', 'both'], width=7)
            cb2.bind("<<ComboboxSelected>>", self.layout_items)
            cb2.grid(column=y,row=3)

            self.expands.append(tk.BooleanVar())
            self.expands[y].set(False)
            chk2 = ttk.Checkbutton(self.control_panel,variable=self.expands[y],command=self.layout_items)
            chk2.grid(column=y,row=4)

    def layout_items(self,*args):
        self.contents_frame.pack_forget()
        for child in self.contents_frame.winfo_children():
            child.destroy()
        self.contents_frame.pack(side="top", fill="both", expand=True)
        for x in range(self.item_count):
            if self.creates[x].get():
                item = tk.Label(self.contents_frame, text=f"Item {1+x}", bg=self.item_colors[x])
                item.pack(side=self.sides[x].get(), fill=self.fills[x].get(), expand=self.expands[x].get())

root = tk.Tk()
app = Application(master=root)
app.mainloop()
