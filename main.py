#Imports
import tkinter as tk
import pydoc
import importlib
import os
import sys

#Declare Functions
def scan_for_libraries():
    """Scans the hard drive for Python libraries and returns a list of module names."""
    sys.path.append(os.getcwd())  # Add current directory to search path
    modules = []
    for module_name in sys.modules:
        if module_name.startswith('_') or module_name.startswith('__'):
            continue
        modules.append(module_name)
    return modules

def display_info(module_name):
    """Displays information about a module in a scrollable window."""
    root = tk.Tk()
    root.title(f"Information about {module_name}")

    text_widget = tk.ScrolledText(root, wrap=tk.WORD)
    text_widget.pack(fill=tk.BOTH, expand=True)

    try:
        info = pydoc.render_doc(module_name)
        text_widget.insert(tk.END, info)
    except ImportError:
        text_widget.insert(tk.END, f"Module '{module_name}' not found.")

    root.mainloop()

def main():
    root = tk.Tk()
    root.title("Python Library Information")

    library_list = tk.Listbox(root)
    library_list.pack(fill=tk.BOTH, expand=True)

    for library in scan_for_libraries():
        library_list.insert(tk.END, library)

    def on_select(event):
        selected_library = library_list.get(library_list.curselection())
        display_info(selected_library)

    library_list.bind('<<ListboxSelect>>', on_select)

    root.mainloop()

if __name__ == "__main__":
    main()
