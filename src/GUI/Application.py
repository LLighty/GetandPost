import tkinter as tk

HEADER_OPTIONS = [
    'Host',
    'User-Agent',
    'Accept',
    'Accept-Language',
    'Accept-Encoding',
    'Referer',
    'Connection',
    'Upgrade-Insecure-Requests',
    'If-Modified-Since',
    'If-None-Match',
    'Cache-Control'
]

Header_Options_Set = {
    'Host': '',
    'User-Agent': '',
    'Accept': '',
    'Accept-Language': '',
    'Accept-Encoding': '',
    'Referer': '',
    'Connection': '',
    'Upgrade-Insecure-Requests': '',
    'If-Modified-Since': '',
    'If-None-Match': '',
    'Cache-Control': ''
}


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Get and Post")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.create_url_widgets()
        self.create_header_widgets()

    def create_url_widgets(self):
        url_frame = tk.Frame(self)
        url_frame.pack(fill=tk.X)
        self.label_url = tk.Label(url_frame, text="Url: ")
        self.entry_url = tk.Entry(url_frame)
        self.label_url.pack(side=tk.LEFT, padx=15, pady=15)
        self.entry_url.pack(fill=tk.X, padx=15, expand=True)

    def create_header_widgets(self):
        header_frame = tk.Frame(self)
        header_frame.pack(fill=tk.X)
        option_variables = tk.StringVar(self)
        option_variables.set(HEADER_OPTIONS[0])
        set_option_variables = tk.StringVar()
        self.options_headers = tk.OptionMenu(header_frame, option_variables, *HEADER_OPTIONS)
        self.entry_header = tk.Entry(header_frame)
        self.button_header = tk.Button(header_frame, text="Submit")
        self.message_header = tk.Message(header_frame, textvariable=set_option_variables)
        self.options_headers.grid(row=0, column=0)
        self.entry_header.grid(row=0, column=1)
        self.button_header.grid(row=0, column=2)
        self.message_header.grid(row=1, column=1)

        set_option_variables.set(Header_Options_Set)

    def create_payload_widgets(self):
        return None

    def create_submit_widgets(self):
        return None