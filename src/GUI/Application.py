import tkinter as tk
from tkinter import filedialog
import Utilities.Get as get
import Utilities.Post as post
from CLI.CommandLine import check_http
import requests
from bs4 import BeautifulSoup
from Utilities.Save import save_data

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

REQUEST_OPTIONS = [
    'Get',
    'Post'
]

current_header_option = HEADER_OPTIONS[0]
current_request_option = REQUEST_OPTIONS[0]

HEADER_OPTIONS_SET_DEFAULT = {
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

payload = {}

data = requests.Response


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Get and Post")
        self.pack(fill=tk.BOTH, expand=True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.pages = {}
        self.create_pages(container)
        self.show_page(EntryPage)

    def create_pages(self, container):
        for P in (EntryPage, DataPage):
            page = P(container, self)
            self.pages[P] = page
            page.grid(row=0, column=0, sticky="nsew")

    def show_page(self, page):
        to_page = self.pages[page]
        to_page.tkraise()

    def get_page(self, page):
        return self.pages[page]


class EntryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.create_url_widgets()
        self.create_header_widgets()
        self.create_payload_widgets()
        self.create_submit_widgets()

    def create_url_widgets(self):
        url_frame = tk.Frame(self)
        url_frame.pack(fill=tk.X)

        # Init
        self.label_url = tk.Label(url_frame, text="Url: ")
        self.entry_url = tk.Entry(url_frame)

        # Layout
        self.label_url.pack(side=tk.LEFT, padx=15, pady=15)
        self.entry_url.pack(fill=tk.X, padx=15, expand=True)

    def create_header_widgets(self):
        header_frame = tk.Frame(self)
        header_frame.pack(fill=tk.X)
        option_variables = tk.StringVar(self)
        option_variables.set(HEADER_OPTIONS[0])

        # Init
        self.set_option_variables = tk.StringVar()
        self.options_headers = tk.OptionMenu(header_frame, option_variables, *HEADER_OPTIONS,
                                             command=self.update_option_header_index)
        self.options_headers.configure(width=25)
        self.entry_header = tk.Entry(header_frame, width=75)
        self.button_header = tk.Button(header_frame, text="Submit", command=self.header_submit_callback)
        self.message_header = tk.Message(header_frame, textvariable=self.set_option_variables)
        self.label_message_header = tk.Label(header_frame, text="Current Header Values:")

        # Layout
        self.options_headers.grid(row=0, column=0)
        self.entry_header.grid(row=0, column=1, sticky=tk.W)
        self.button_header.grid(row=0, column=2, sticky=tk.W)
        self.label_message_header.grid(row=1, column=0, sticky=tk.E)
        self.message_header.grid(row=1, column=1, sticky=tk.W)

        self.set_option_variables.set(dict_to_string(Header_Options_Set))

    def create_payload_widgets(self):
        payload_frame = tk.Frame(self)
        payload_frame.pack(fill=tk.X)

        # Init
        self.label_payload_key = tk.Label(payload_frame, text="Key: ")
        self.label_payload_value = tk.Label(payload_frame, text="Value: ")
        self.label_payload_remove = tk.Label(payload_frame, text="Remove Key: ")
        self.entry_payload_key = tk.Entry(payload_frame, width=85)
        self.entry_payload_value = tk.Entry(payload_frame, width=85)
        self.entry_payload_remove = tk.Entry(payload_frame, width=85)
        self.button_payload_submit = tk.Button(payload_frame, text="Submit Payload", command=self.add_payload)
        self.button_payload_remove = tk.Button(payload_frame, text="Remove Payload", command=self.remove_payload)
        self.text_payload = tk.Text(payload_frame)
        self.text_payload.config(state=tk.DISABLED)

        # Layout
        self.label_payload_key.grid(row=0, column=0, sticky=tk.E)
        self.entry_payload_key.grid(row=0, column=1, sticky=tk.W)
        self.label_payload_value.grid(row=1, column=0, sticky=tk.E)
        self.entry_payload_value.grid(row=1, column=1, sticky=tk.W)
        self.button_payload_submit.grid(row=0, column=2, rowspan=2)
        self.label_payload_remove.grid(row=2, column=0, sticky=tk.E)
        self.entry_payload_remove.grid(row=2, column=1, sticky=tk.W)
        self.button_payload_remove.grid(row=2, column=2)
        self.text_payload.grid(row=3, column=0, columnspan=4)

    def create_submit_widgets(self):
        submit_frame = tk.Frame(self)
        submit_frame.pack(expand=1, fill=tk.BOTH)

        request_option_variables = tk.StringVar(self)
        request_option_variables.set(REQUEST_OPTIONS[0])

        # Init
        self.request_options = tk.OptionMenu(submit_frame, request_option_variables, *REQUEST_OPTIONS,
                                             command=self.update_request_header_index)
        self.request_options.configure(width=6)
        self.button_submit_query = tk.Button(submit_frame, text="Submit Query", command=self.submit_query)

        # Layout
        self.request_options.place(relx=.38, rely=.25)
        self.button_submit_query.place(relx=.50, rely=.26)

    def header_submit_callback(self):
        Header_Options_Set[current_header_option] = self.entry_header.get()
        self.update_set_option_variables()
        self.entry_header.delete(0, 'end')

    def update_option_header_index(self, value):
        global current_header_option
        current_header_option = value

    def update_set_option_variables(self):
        self.set_option_variables.set(dict_to_string(Header_Options_Set))

    def add_payload(self):
        global payload
        payload[self.entry_payload_key.get()] = self.entry_payload_value.get()
        self.entry_payload_key.delete(0, 'end')
        self.entry_payload_value.delete(0, 'end')
        self.render_payload()

    def remove_payload(self):
        try:
            global payload
            del payload[self.entry_payload_remove.get()]
            self.entry_payload_remove.delete(0, 'end')
            self.render_payload()
        except KeyError:
            print("Cannot find " + self.entry_payload_remove.get() + " to delete!")

    def clear_payload(self):
        global payload
        payload.clear()
        self.render_payload()

    def render_payload(self):
        self.text_payload.config(state=tk.NORMAL)
        self.text_payload.delete(1.0, "end")
        self.text_payload.insert(1.0, get_payload_string())
        self.text_payload.config(state=tk.DISABLED)

    def submit_query(self):
        global data
        address = check_http(self.entry_url.get())
        # print(address)
        if current_request_option == "Get":
            data = get.get_website(address, get_filled_header_fields())
        if current_request_option == "Post":
            data = post.get_post_response(address, get_filled_header_fields(), payload)
        self.controller.show_page(DataPage)

    def update_request_header_index(self, value):
        global current_request_option
        current_request_option = value


class DataPage(tk.Frame):
    modes = [
        'Body',
        'Cookies',
        'Headers'
    ]
    current_mode_selected = modes[0]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
        self.display_body()

    def create_widgets(self):
        self.create_button_header_widgets()
        self.create_text_widgets()
        self.create_save_widgets()

    def create_button_header_widgets(self):
        button_header_frame = tk.Frame(self)
        button_header_frame.pack(fill=tk.X)

        # Init
        self.button_body = tk.Button(button_header_frame, text="Body", width=32, command=self.display_body)
        self.button_cookies = tk.Button(button_header_frame, text="Cookies", width=32, command=self.display_cookies)
        self.button_headers = tk.Button(button_header_frame, text="Headers", width=32, command=self.display_headers)
        self.button_raw = tk.Button(button_header_frame, text="Raw", width=32, command=self.raw_body)
        self.button_pretty = tk.Button(button_header_frame, text="Pretty", width=32, command=self.pretty_body)

        # Layout
        self.button_body.grid(row=0, column=0, sticky='nesw')
        self.button_cookies.grid(row=0, column=1, sticky='nesw')
        self.button_headers.grid(row=0, column=2, sticky='nesw')
        self.button_raw.grid(row=1, column=0)
        self.button_pretty.grid(row=1, column=1)

    def create_text_widgets(self):
        text_frame = tk.Frame(self)
        text_frame.pack(fill=tk.X)

        # Init
        self.text_data = tk.Text(text_frame, height=35)

        # Layout
        self.text_data.grid(row=1, column=0, sticky="nsew")
        text_frame.grid_columnconfigure(0, weight=1)

    def create_save_widgets(self):
        save_frame = tk.Frame(self)
        save_frame.pack(fill=tk.X)
        save_frame.place(relx=.20, rely=.85)

        self.label_save = tk.Label(save_frame, text="Save Location:")
        self.entry_save = tk.Entry(save_frame, width=50)
        self.button_file_explorer = tk.Button(save_frame, text="...", command=self.open_file_explorer)
        self.button_save = tk.Button(save_frame, text="Save", command=self.save_data_func)
        self.button_back = tk.Button(save_frame, text="Return", command=self.return_to_front)

        self.label_save.grid(row=0, column=0)
        self.entry_save.grid(row=0, column=1)
        self.button_file_explorer.grid(row=0, column=2)
        self.button_save.grid(row=0, column=3)
        self.button_back.grid(row=1, column=1)

    def update_text_data(self, text):
        self.text_data.config(state=tk.NORMAL)
        self.text_data.delete(1.0, "end")
        self.text_data.insert(1.0, text)
        self.text_data.config(state=tk.DISABLED)

    def display_body(self):
        self.current_mode_selected = self.modes[0]
        self.update_text_data(data.text)

    def display_cookies(self):
        self.current_mode_selected = self.modes[1]
        self.update_text_data(data.cookies)

    def display_headers(self):
        self.current_mode_selected = self.modes[2]
        self.update_text_data(data.headers)

    def raw_body(self):
        if self.current_mode_selected == self.modes[0]:
            self.update_text_data(data.text)

    def pretty_body(self):
        if self.current_mode_selected == self.modes[0]:
            self.update_text_data(BeautifulSoup(data.text))

    def open_file_explorer(self):
        filename = filedialog.asksaveasfilename(initialdir="/",
                                                title="Select where to save",
                                                filetypes=(("Text files",
                                                            "*.txt*"),
                                                           ("all files",
                                                            "*.*")))
        self.entry_save.delete(0, 'end')
        self.entry_save.insert(0, filename)

    def save_data_func(self):
        save_data(data, self.entry_save.get())

    def return_to_front(self):
        self.controller.get_page(EntryPage).clear_payload()
        global Header_Options_Set
        Header_Options_Set = HEADER_OPTIONS_SET_DEFAULT
        self.controller.get_page(EntryPage).update_set_option_variables()
        self.controller.show_page(EntryPage)


def dict_to_string(dictionary):
    s = ""
    # print(type(dictionary))
    for key, value in dictionary.items():
        s += key + ": " + value + '\n'
    return s


def get_payload_string():
    # print(payload)
    string = '{\n' + "{payload}\n".format(payload=dict_to_string(payload) + '}')
    return string


def get_filled_header_fields():
    headers = None
    for key, value in Header_Options_Set.items():
        if value is not None and value != "":
            headers[key] = value
    return headers
