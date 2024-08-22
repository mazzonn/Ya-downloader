import customtkinter as CTk
from customtkinter import filedialog
import downloader
import database  

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('500x450')
        self.title('Ya downloader')
        self.resizable(False, False)

        database.create_table()  

        self.log = CTk.CTkFrame(master=self, fg_color='transparent')
        self.log.grid(row=1, column=0, padx=85, pady=20, sticky='nsew')

        self.log_out = CTk.CTkTextbox(master=self.log, width=300, corner_radius=10)
        self.log_out.grid(row=0, column=1, pady=10)
        self.log_out.configure(state='disabled')

        self.location_button = CTk.CTkButton(master=self, text='Выбрать папку для сохранения', command=self.update_folder_path)
        self.location_button.grid(row=4, column=0)

        self.start_button = CTk.CTkButton(master=self, text='Скачать', command=self.download_music)
        self.start_button.grid(row=3, column=0, pady=10)

        self.out_location = CTk.CTkEntry(master=self)
        self.out_location.grid(row=2, column=0)
        self.out_location.configure(state='disabled')

        self.id_entry = CTk.CTkEntry(master=self, placeholder_text="ID")
        
        self.category = CTk.CTkOptionMenu(master=self, values=["Плейлист \"Мне нравится\"",
                                                                "Альбом по id", "Песня по id"],
                                                                command=self.option_changed)
        self.category.grid(row=0, column=0, pady=10)

        self.token_entry = CTk.CTkEntry(master=self, placeholder_text="Токен")
        self.token_entry.place(x=165, y=420)
        self.load_token() 

    def load_token(self):
        token = database.load_token()
        if token:
            self.token_entry.insert(0, token)

    def disable_all(self):
        self.start_button.configure(state='disabled')
        self.location_button.configure(state='disabled')
        self.id_entry.configure(state="disabled")
        self.out_location.configure(state='disabled')
    
    def enable_all(self):
        self.start_button.configure(state='normal')
        self.location_button.configure(state='normal')
        self.id_entry.configure(state="normal")
        self.out_location.configure(state='normal')
    
    def option_changed(self, choice):
        if choice in ["Альбом по id", "Песня по id"]:
            self.id_entry.place(x=165, y=45)
        else:
            self.id_entry.place(x=-100, y=-100)

    def update_folder_path(self):
        global folder_path
        global path

        folder_path = filedialog.askdirectory()
        path = folder_path.replace("\\", "\\\\")

        self.out_location.configure(state='normal')
        self.out_location.delete(0, CTk.END)
        self.out_location.insert(0, folder_path)
        self.out_location.configure(state='disabled')

    def download_music(self):
        database.save_token(self.token_entry.get())

        selected_option = self.category.get()
        if selected_option == "Плейлист \"Мне нравится\"":
            self.disable_all()
            downloader.download_like(self.token_entry.get(), path),
            self.enable_all()
            self.log_out.configure(state='normal')
            self.log_out.insert('0.0', f'Скачивание завершено в папку {path}')
            self.log_out.configure(state='disabled')
        elif selected_option == "Альбом по id":
            self.disable_all()
            id_value = self.id_entry.get()
            downloader.album_download(self.token_entry.get(), id_value, path)
            self.enable_all()
            self.log_out.configure(state='normal')
            self.log_out.insert('0.0', f'Скачивание завершено в папку {path}')
            self.log_out.configure(state='disabled')
        elif selected_option == "Песня по id":
            self.disable_all()
            id_value = self.id_entry.get()
            downloader.song_download(self.token_entry.get(), id_value, path)
            self.enable_all()
            self.log_out.configure(state='normal')
            self.log_out.insert('0.0', f'Скачивание завершено в папку {path}')
            self.log_out.configure(state='disabled')


if __name__ == "__main__":
    app = App()
    app.mainloop()
