from file_cleaner import FileCleaner
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Required for loading image logos

class CleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Cleaner")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Use absolute path for icon
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "icon.ico")
        try:
            self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Could not load icon: {e}")

        self.clean_temp = tk.BooleanVar()
        self.clean_traces = tk.BooleanVar()
        self.clean_softwaredist = tk.BooleanVar()
        self.clean_junk = tk.BooleanVar()
        self.clean_driverstore = tk.BooleanVar()

        self.cleaner = FileCleaner()

        self.create_widgets()

    def create_widgets(self):
        # Importing here is optional, but okay
        import os
        from PIL import Image, ImageTk

        # Build full path to logo image
        script_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(script_dir, "logo.png")

        try:
            img = Image.open(logo_path)
            img = img.resize((100, 100))
            self.logo = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.logo).pack(pady=10)
        except Exception as e:
            print(f"Could not load logo image: {e}")

        ttk.Label(self.root, text="Select What to Clean", font=("Arial", 14)).pack(pady=10)

        ttk.Checkbutton(self.root, text="Temporary Files", variable=self.clean_temp).pack()
        ttk.Checkbutton(self.root, text="Traces (Browser Cache, Cookies)", variable=self.clean_traces).pack()
        ttk.Checkbutton(self.root, text="Windows Update Cache (SoftwareDistribution)", variable=self.clean_softwaredist).pack()
        ttk.Checkbutton(self.root, text="Common Junk Files (Prefetch, Logs, Recycle Bin)", variable=self.clean_junk).pack()
        ttk.Checkbutton(self.root, text="Old Driver Backups (DriverStore)", variable=self.clean_driverstore).pack()

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Scan", command=self.scan).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Delete", command=self.delete_selected).grid(row=0, column=1, padx=10)

        self.temp_result = tk.StringVar(value="Temp Files: Not scanned")
        self.traces_result = tk.StringVar(value="Traces: Not scanned")
        self.softwaredist_result = tk.StringVar(value="SoftwareDistribution: Ready")
        self.junk_result = tk.StringVar(value="Common Junk: Ready")
        self.driverstore_result = tk.StringVar(value="DriverStore: Ready")

        ttk.Label(self.root, textvariable=self.temp_result, font=("Arial", 10)).pack(pady=3)
        ttk.Label(self.root, textvariable=self.traces_result, font=("Arial", 10)).pack(pady=3)
        ttk.Label(self.root, textvariable=self.softwaredist_result, font=("Arial", 10)).pack(pady=3)
        ttk.Label(self.root, textvariable=self.junk_result, font=("Arial", 10)).pack(pady=3)
        ttk.Label(self.root, textvariable=self.driverstore_result, font=("Arial", 10)).pack(pady=3)

    def scan(self):
        if self.clean_temp.get():
            temp_count = self.cleaner.get_temp_file_count()
            self.temp_result.set(f"Temp Files: {temp_count} files found")
        else:
            self.temp_result.set("Temp Files: Skipped")

        if self.clean_traces.get():
            trace_count = self.cleaner.get_trace_file_count()
            self.traces_result.set(f"Traces: {trace_count} items found")
        else:
            self.traces_result.set("Traces: Skipped")

        if self.clean_softwaredist.get():
            self.softwaredist_result.set("SoftwareDistribution: Ready to clean")
        else:
            self.softwaredist_result.set("SoftwareDistribution: Skipped")

        if self.clean_junk.get():
            self.junk_result.set("Common Junk: Ready to clean")
        else:
            self.junk_result.set("Common Junk: Skipped")

        if self.clean_driverstore.get():
            self.driverstore_result.set("DriverStore: Ready to clean")
        else:
            self.driverstore_result.set("DriverStore: Skipped")

    def delete_selected(self):
        if self.clean_temp.get():
            self.cleaner.delete_temp_files()
            self.temp_result.set("Temp Files: Deleted")

        if self.clean_traces.get():
            self.cleaner.delete_trace_files()
            self.traces_result.set("Traces: Deleted")

        if self.clean_softwaredist.get():
            self.cleaner.delete_software_distribution_cache()
            self.softwaredist_result.set("SoftwareDistribution: Cleaned")

        if self.clean_junk.get():
            self.cleaner.delete_common_junk()
            self.junk_result.set("Common Junk: Deleted")

        if self.clean_driverstore.get():
            self.cleaner.delete_old_driver_backups()
            self.driverstore_result.set("DriverStore: Cleaned")

if __name__ == "__main__":
    root = tk.Tk()
    app = CleanerApp(root)
    root.mainloop()
