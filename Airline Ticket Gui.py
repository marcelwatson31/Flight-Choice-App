from tkinter import *
from tkinter import ttk


from selenium import webdriver
from selenium.webdriver.common.keys import Keys




class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title('Airline Ticket App')
        self.minsize(400,400)
        self.wm_iconbitmap('kirbyicon.ico')
        self.config(bg='orange')
        
        self.siteused()

        self.leaving_airport_textbox()

        self.destination_textbox()

        self.departure_day_textbox()

        self.returning_day_textbox()

        self.submit_button()

             

    def siteused(self):
        site = Label(self, text = "Powered by: Expedia", font = "Times" )
        site.grid(column = 0, row = 0)

    def leaving_airport_textbox(self):
        self.airport_leave = StringVar()
        airport_box = Entry(self, width = 20, textvariable = self.airport_leave)
        airport_box.grid(column = 0, row = 1)
        airport_box.focus()

        airport_label = Label(self, text = "Enter what airport you would like to leave from", font = "Times")
        airport_label.grid(column = 1, row =1 )

    def destination_textbox(self):
        self.destination = StringVar()
        destination_box = Entry(self, width = 20, textvariable = self.destination)
        destination_box.grid(column = 0, row = 2)

        destination_label = Label(self, text = "Where would you like to go?", font = "Times")
        destination_label.grid(column = 1, row = 2)


    def departure_day_textbox(self):
        self.departure_day = StringVar()
        departure_day_box = Entry(self, width = 20, textvariable = self.departure_day)
        departure_day_box.grid(column = 0, row = 3)

        departure_day_label = Label(self, text = "When would you like to leave? mm/dd/yyyy", font = "Times")
        departure_day_label.grid(column = 1 , row = 3)


    def returning_day_textbox(self):
        self.returning_day = StringVar()
        returning_day_box = Entry(self, width = 20, textvariable = self.returning_day)
        returning_day_box.grid(column = 0, row = 4)

        returning_day_label = Label(self, text = "When would you like to come back? mm/dd/yyyy", font = "Times")
        returning_day_label.grid(column = 1 , row = 4)

    def submit_button(self):
        submit = Button(self, text ="Submit", height = 2, width = 20, padx = 3, pady = 3, command = self.submit_button_clicked)
        submit.grid(column = 1, row = 5)
        
    def submit_button_clicked(self):
        browser = webdriver.Chrome('C:\\chromedriver')
        browser.get('https://www.expedia.com/')

        flights = browser.find_element_by_xpath('//*[@id="tab-flight-tab-hp"]')
        flights.send_keys(Keys.ENTER)

        airport = browser.find_element_by_xpath('//*[@id="flight-origin-hp-flight"]')
        airport.send_keys(self.airport_leave.get())

        arriving_airport = browser.find_element_by_xpath('//*[@id="flight-destination-hp-flight"]')
        arriving_airport.send_keys(self.destination.get())

        when = browser.find_element_by_xpath('//*[@id="flight-departing-hp-flight"]')
        when.send_keys(self.departure_day.get())

        till = browser.find_element_by_xpath('//*[@id="flight-returning-hp-flight"]')
        till.send_keys(self.returning_day.get())

        search_button = browser.find_element_by_xpath('//*[@id="gcw-flights-form-hp-flight"]/div[8]/label/button')
        search_button.send_keys(Keys.ENTER)



window = Window()
window.mainloop()
