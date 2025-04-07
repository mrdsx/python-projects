import customtkinter as ctk
import translate
import pyperclip
from threading import Thread
from time import sleep

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.languages = ['Azerbaijani', 'Chinese', 'English', 'French', 'German',
                          'Italian', 'Japanese', 'Korean', 'Russian', 'Spanish',
                          'Turkish', 'Ukrainian', 'Vietnamese']

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.x = int((self.width - 1000) / 2)
        self.y = int((self.height - 450) / 2)

        self.title('Translator App')
        self.geometry(f'1000x350+{self.x}+{self.y}')
        self.resizable(False, False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, width=1000, height=400)
        self.main_frame.rowconfigure(3, weight=1)
        self.main_frame.grid(row=0, column=0, sticky='nsew')

        self.application_label = ctk.CTkLabel(self.main_frame, text='Translator', font=('Calibri', 30), width=1000)
        self.application_label.grid(row=0, column=0, sticky='nsew', pady=(50, 0))

        self.menu_widgets_frame = ctk.CTkFrame(self.main_frame, width=1000, fg_color='transparent')
        self.menu_widgets_frame.columnconfigure(1, weight=1)
        self.menu_widgets_frame.grid(row=1, column=0, sticky='nsew', pady=20)

        self.input_lang = ctk.StringVar(value='en')
        self.input_text_menu = ctk.CTkOptionMenu(self.menu_widgets_frame,
                                                 dynamic_resizing=False,
                                                 values=self.languages,
                                                 command=self.update_input_lang)
        self.input_text_menu.grid(row=0, column=0, sticky='w', padx=(50, 0))
        self.input_text_menu.set('English')

        self.output_lang = ctk.StringVar(value='ru')
        self.output_text_menu = ctk.CTkOptionMenu(self.menu_widgets_frame,
                                                  dynamic_resizing=False,
                                                  values=self.languages,
                                                  command=self.update_output_lang)
        self.output_text_menu.grid(row=0, column=1, sticky='e', padx=(0, 50))
        self.output_text_menu.set('English')

        self.entry_widgets_frame = ctk.CTkFrame(self.main_frame, width=1000, fg_color='transparent')
        self.entry_widgets_frame.columnconfigure(1, weight=1)
        self.entry_widgets_frame.grid(row=2, column=0, sticky='nsew', pady=20)

        self.input_text_entry = ctk.CTkEntry(self.entry_widgets_frame, width=400)
        self.input_text_entry.grid(row=0, column=0, sticky='w', padx=(50, 0))

        self.output_text_entry = ctk.CTkEntry(self.entry_widgets_frame, width=400)
        self.output_text_entry.grid(row=0, column=1, sticky='e', padx=(0, 50))
        self.output_text_entry.configure(state='disabled')

        self.third_row_frame = ctk.CTkFrame(self.main_frame, width=1000, fg_color='transparent')
        self.third_row_frame.columnconfigure(1, weight=1)
        self.third_row_frame.grid(row=3, column=0, sticky='nsew', pady=(0, 50))

        self.translate_button = ctk.CTkButton(self.third_row_frame, text='Translate', command=self.translate)
        self.translate_button.grid(row=3, column=0, sticky='w', padx=(50, 0))

        self.copy_button = ctk.CTkButton(self.third_row_frame, text='Copy translation', command=self.copy)
        self.copy_button.grid(row=3, column=1, sticky='e', padx=(0, 50))

    def translate(self):
        t1 = Thread(target=self.translate_process)
        t1.start()

    def translate_process(self):
        self.translate_button.configure(state='disabled', text='Translating...')
        input_text = self.input_text_entry.get()
        translating = translate.Translator(from_lang=self.input_lang.get(), to_lang=self.output_lang.get())
        output_text = translating.translate(input_text)
        self.output_text_entry.configure(state='normal')
        self.output_text_entry.delete(0, len(self.output_text_entry.get()))
        self.output_text_entry.insert(0, output_text)
        self.output_text_entry.configure(state='disabled')
        self.translate_button.configure(state='normal', text='Translate')

    def copy(self):
        t2 = Thread(target=self.copy_process)
        t2.start()

    def copy_process(self):
        pyperclip.copy(self.output_text_entry.get())
        fg_color = self.copy_button.cget('fg_color')
        hover_color = self.copy_button.cget('hover_color')
        self.copy_button.configure(text='Copied!', fg_color='#009900', hover_color='#006600')
        sleep(1)
        self.copy_button.configure(text='Copy translation', fg_color=fg_color, hover_color=hover_color)

    def update_input_lang(self, value):
        if value == 'Azerbaijani':
            self.input_lang.set('az')
        elif value == 'Chinese':
            self.input_lang.set('zh')
        elif value == 'English':
            self.input_lang.set('en')
        elif value == 'French':
            self.input_lang.set('fr')
        elif value == 'German':
            self.input_lang.set('de')
        elif value == 'Italian':
            self.input_lang.set('it')
        elif value == 'Japanese':
            self.input_lang.set('ja')
        elif value == 'Korean':
            self.input_lang.set('ko')
        elif value == 'Russian':
            self.input_lang.set('ru')
        elif value == 'Spanish':
            self.input_lang.set('es')
        elif value == 'Turkish':
            self.input_lang.set('tr')
        elif value == 'Ukrainian':
            self.input_lang.set('uk')
        elif value == 'Vietnamese':
            self.input_lang.set('vi')

    def update_output_lang(self, value):
        if value == 'Azerbaijani':
            self.output_lang.set('az')
        elif value == 'Chinese':
            self.output_lang.set('zh')
        elif value == 'English':
            self.output_lang.set('en')
        elif value == 'French':
            self.output_lang.set('fr')
        elif value == 'German':
            self.output_lang.set('de')
        elif value == 'Italian':
            self.output_lang.set('it')
        elif value == 'Japanese':
            self.output_lang.set('ja')
        elif value == 'Korean':
            self.output_lang.set('ko')
        elif value == 'Russian':
            self.output_lang.set('ru')
        elif value == 'Spanish':
            self.output_lang.set('es')
        elif value == 'Turkish':
            self.output_lang.set('tr')
        elif value == 'Ukrainian':
            self.output_lang.set('uk')
        elif value == 'Vietnamese':
            self.output_lang.set('vi')


if __name__ == '__main__':
    app = App()
    app.mainloop()
