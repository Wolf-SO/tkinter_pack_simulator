import tkinter as tk
from tkinter import ttk

class PackableWidget:
    def __init__(self, widget, pack=False):
        self.widget = widget
        self.pack = tk.BooleanVar(value=pack)
        self.side = tk.StringVar(value="top")
        self.fill = tk.StringVar(value="none")
        self.expand = tk.BooleanVar(value=False)

class Application(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        super().__init__(root)
        root.geometry("800x600")
        root.title("tkinter pack layout simulator")
        
        self.item_colors = [
            'IndianRed1', 
            'SteelBlue1', 
            'SpringGreen1', 
            'Goldenrod1', 
            'LightPink1', 
            'LightSteelBlue1', 
            'DarkSeaGreen1', 
            'Khaki1']
        self.default_item_count = 4
        self.item_count = len(self.item_colors)

        self.pack(fill=tk.BOTH, expand=True)

        self.items = []

        self.populate_app()
        
        self.layout_items()

    def populate_app(self):
        self.simulation_panel = tk.Frame(self, bg = "white")
        self.control_panel = tk.Frame(self)
        self.control_panel.pack(side=tk.BOTTOM)
        self.simulation_panel.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.contents_frame = tk.Frame(self.simulation_panel, bg="gray31")
        self.contents_frame.pack(side="top", fill="both", expand=True)

        # row-header for item's pack arguments
        tk.Label(self.control_panel, text="pack").grid(column=0, row=1, sticky="news")
        tk.Label(self.control_panel, text="side").grid(column=0, row=2, sticky="news")
        tk.Label(self.control_panel, text="fill").grid(column=0, row=3, sticky="news")
        tk.Label(self.control_panel, text="expand").grid(column=0, row=4, sticky="news")
        
        for x in range(self.item_count):
            self.add_item(x)
            
    def add_item(self, x):
        # col-header for item controls 
        tk.Label(self.control_panel, text=f"Item {1+x}").grid(column=1+x, row=0)

        widget = tk.Label(self.contents_frame, text=f"Item {1+x}", bg=self.item_colors[x])
        item = PackableWidget(widget, x < self.default_item_count)
        self.items.append(item)
        
        chk1 = ttk.Checkbutton(
            self.control_panel, 
            variable=item.pack, 
            command=self.layout_items)
        chk1.grid(column=1+x, row=1)
    
        cb1 = ttk.Combobox(
            self.control_panel, 
            textvariable=item.side, 
            state="readonly", 
            values=['top', 'bottom', 'left', 'right'], 
            width=7)
        cb1.bind("<<ComboboxSelected>>", self.layout_items)
        cb1.grid(column=1+x, row=2)

        cb2 = ttk.Combobox(
            self.control_panel,
            textvariable=item.fill,
            state="readonly",
            values=['none', 'x', 'y', 'both'], 
            width=7)
        cb2.bind("<<ComboboxSelected>>", self.layout_items)
        cb2.grid(column=1+x, row=3)

        chk2 = ttk.Checkbutton(
            self.control_panel,
            variable=item.expand,
            command=self.layout_items)
        chk2.grid(column=1+x, row=4)
        
    def layout_items(self,*args):
        # remove all widgets from frame
        for item in self.items:
            item.widget.pack_forget()
        # re-pack all widgets to frame
        for item in self.items:
            if item.pack.get():
                item.widget.pack(side=item.side.get(), fill=item.fill.get(), expand=item.expand.get())

app = Application()
app.mainloop()
