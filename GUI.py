import complete
from complete import get_best_k_completions

from tkinter import *
from init import completion_data_struct


class MyApp:
    def __init__(self, root):
        self._root = root
        root.title("Auto Complete")
        self._base_frame = Frame(root)
        self._base_frame.pack(side=TOP)
        self._label = Label(self._base_frame, text="Enter Text To Search")
        self._label.pack(side=LEFT)
        self._entry = Entry(self._base_frame)
        self._entry.pack(side=LEFT)
        self._entry.bind("<Return>", self.run)
        self._search = Button(self._base_frame, text='search', command=self.run)
        self._search.pack(side=LEFT)
        self._results = Frame(root)
        self._results.pack(side=BOTTOM)

    def fix_string(self, string_to_fix):
        return string_to_fix

    def run(self, event):
        for widget in self._results.winfo_children():
            widget.destroy()
        string_to_complete = self._entry.get()
        if string_to_complete[len(string_to_complete) - 1] != '#':
            best_five = get_best_k_completions(string_to_complete)
            self.print_match_completions(best_five)
            self._entry.icursor(len(string_to_complete))
        else:
            self._entry.delete(0, len(string_to_complete))

    def print_match_completions(self, best_five):
        # self._results.pack(side=BOTTOM)
        lb = Listbox(self._results, width=100, height=6)
        for i in range(len(best_five)):
            lb.insert(i,
                      f'* {best_five[i].completed_sentence}.  ({best_five[i].source_text}, line {best_five[i].offset}, score {best_five[i].score})')
        lb.pack(side=TOP)


root = Tk()
MyApp(root)
root.mainloop()
