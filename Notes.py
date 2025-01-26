import customtkinter as ctk
import os

class NoteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Заметки")
        ctk.set_default_color_theme("blue")
        self.note_text = ctk.CTkTextbox(master, width=400, height=200)
        self.note_text.pack(pady=10)

        self.save_button = ctk.CTkButton(master, text="Готово", command=self.save_note)
        self.save_button.pack(pady=10)

        self.notes_textbox = ctk.CTkTextbox(master, width=400, height=200, state="normal")
        self.notes_textbox.pack(pady=10)
        self.notes_textbox.bind("<ButtonRelease-1>", self.load_selected_note)

        self.delete_button = ctk.CTkButton(master, text="Удалить", command=self.delete_note)
        self.delete_button.pack(pady=10)

        self.load_notes()

    def load_notes(self):
        if os.path.exists("notes.txt"):
            with open("notes.txt", "r") as file:
                notes = file.readlines()
                for note in notes:
                    self.notes_textbox.insert(ctk.END, note.strip() + "\n")

    def save_note(self):
        note = self.note_text.get("1.0", ctk.END).strip()
        if note:
            with open("notes.txt", "a") as file:
                file.write(note + "\n")

            self.notes_textbox.insert(ctk.END, note + "\n")

            self.note_text.delete("1.0", ctk.END)

    def delete_note(self):
        selected_note_index = self.notes_textbox.index("insert").split('.')[0]
        selected_note_index = int(selected_note_index)

        if selected_note_index > 0:
            all_notes = self.notes_textbox.get("1.0", ctk.END).strip().splitlines()
            all_notes.pop(selected_note_index - 1)
            self.notes_textbox.delete("1.0", ctk.END)
            self.notes_textbox.insert(ctk.END, "\n".join(all_notes) + "\n")

            with open("notes.txt", "w") as file:
                file.write("\n".join(all_notes) + "\n")

    def load_selected_note(self, event):
        index = self.notes_textbox.index("insert").split('.')[0]
        try:
            selected_note = self.notes_textbox.get(f"{index}.0", f"{index}.end").strip()
            self.note_text.delete("1.0", ctk.END)
            self.note_text.insert("1.0", selected_note)
        except Exception as e:
            pass

if __name__ == "__main__":
    ctk.set_appearance_mode("blue")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = NoteApp(root)
    root.mainloop()