import psycopg2 as psyc
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import datetime

def seconds_to_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))



class gui:
    def __init__(self, cursor):
        self.entry = None
        self.entered_text = None
        self.state = 'main'
        self.cursor = cursor
        self.record = None

    def show_error_popup(self, error_message):
        error_popup = tk.Toplevel(root)
        error_popup.title("Error")
        error_popup.geometry("400x100")

        # Display the error message
        error_label = tk.Label(error_popup, text=error_message, font=("Helvetica", 12))
        error_label.pack(pady=20)

        # Add a button to close the popup
        close_button = tk.Button(error_popup, text="Close", command=error_popup.destroy)
        close_button.pack(pady=10)

    def retrieve_text(self):
        self.entered_text = self.entry.get()
        print(self.entered_text)
        self.entry.delete(0, tk.END)
        
        if self.state == 'search_person':
            self.cursor.execute(f"SELECT * from events WHERE LOWER(person) = LOWER('{self.entered_text}')")
            self.record = cursor.fetchall()
            
            # Display the results in the text widget
            self.output_text.delete(1.0, tk.END)  # Clear previous content
            for row in self.record:
                self.output_text.insert(tk.END, f"Time: {seconds_to_time(row[0])} | Type: {row[1]} | LinkID: {row[2]}\n\n")
        
        if self.state == 'search_link':
            self.cursor.execute(f"SELECT * from events WHERE LOWER(linkid) = LOWER('{self.entered_text}')")
            self.record = cursor.fetchall()
            
            # Display the results in the text widget
            self.output_text.delete(1.0, tk.END)  # Clear previous content
            for row in self.record:
                self.output_text.insert(tk.END, f"Time: {seconds_to_time(row[0])} | Type: {row[1]} | LinkID: {row[2]}\n\n")
                
        if self.state == 'search_link_details':
            self.cursor.execute(f"SELECT * from links WHERE LOWER(linkid) = LOWER('{self.entered_text}')")
            self.record = cursor.fetchall()
            
            # Display the results in the text widget
            self.output_text.delete(1.0, tk.END)  # Clear previous content
            for row in self.record:
                self.output_text.insert(tk.END, f"From Node: {row[1]} | To Node: {row[2]} | Length: {row[3]} | Capacity: {row[4]} | Freespeed: {row[5]}\n\n")
    
    # Implement the logic for retreiving events by a time interval.
    def retrieve_interval(self):
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()
        
        try:
            # Convert user input to datetime objects
            start_time = datetime.datetime.strptime(start_time, "%H:%M:%S").time()
            end_time = datetime.datetime.strptime(end_time, "%H:%M:%S").time()

            # Convert datetime objects to seconds
            start_seconds = start_time.hour * 3600 + start_time.minute * 60 + start_time.second
            end_seconds = end_time.hour * 3600 + end_time.minute * 60 + end_time.second

            self.cursor.execute(f"SELECT * FROM events WHERE time BETWEEN {start_seconds} AND {end_seconds}")
            self.record = self.cursor.fetchall()

            # Display the results in the text widget
            self.output_text.delete(1.0, tk.END)  # Clear previous content
            for row in self.record:
                self.output_text.insert(tk.END, f"Time: {seconds_to_time(row[0])} | Type: {row[1]} | LinkID: {row[2]}\n\n")

        except ValueError:
            error_message = "Invalid time format. Please enter time in HH:MM:SS."
            self.show_error_popup(error_message)



    # Main Menu Button Functions
    def search_events_by_person(self):
        # Implement the logic for 'Search Events by Person'
        self.state = 'search_person'
        print("Searching events by person")
        window = tk.Toplevel(root)
        window.title("Search Events by Person")
        window.geometry("300x400")
        
        # Title
        label = tk.Label(window, text="Search Events by Person", font=("Helvetica", 16))
        label.pack(pady=10)
        
        # Create an Entry widget for text input
        self.entry = tk.Entry(window, width=30)
        self.entry.pack(pady=10)

        # Create a button to trigger text retrieval
        retrieve_button = tk.Button(window, text="Retrieve Text", command=self.retrieve_text)
        retrieve_button.pack(pady=10)
        
        # Create a text widget to display the results
        self.output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
        self.output_text.pack(pady=10)
        
        

    def search_events_by_link_id(self):
        # Implement the logic for 'Search Events by LinkID'
        self.state = 'search_link'
        print("Searching events by LinkID")
        window = tk.Toplevel(root)
        window.title("Search Events by Link ID")
        window.geometry("300x400")
        
        # Title
        label = tk.Label(window, text="Search Events by Link ID", font=("Helvetica", 16))
        label.pack(pady=10)
        
        # Create an Entry widget for text input
        self.entry = tk.Entry(window, width=30)
        self.entry.pack(pady=10)

        # Create a button to trigger text retrieval
        retrieve_button = tk.Button(window, text="Retrieve Text", command=self.retrieve_text)
        retrieve_button.pack(pady=10)
        
        # Create a text widget to display the results
        self.output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
        self.output_text.pack(pady=10)

    def search_link_details_by_link_id(self):
        # Implement the logic for 'Search Link Details by LinkID'
        self.state = 'search_link_details'
        print("Searching link details by LinkID")
        window = tk.Toplevel(root)
        window.title("Search Link Details by Link ID")
        window.geometry("300x400")
        
        # Title
        label = tk.Label(window, text="Search Link Details by Link ID", font=("Helvetica", 16))
        label.pack(pady=10)
        
        # Create an Entry widget for text input
        self.entry = tk.Entry(window, width=30)
        self.entry.pack(pady=10)

        # Create a button to trigger text retrieval
        retrieve_button = tk.Button(window, text="Retrieve Text", command=self.retrieve_text)
        retrieve_button.pack(pady=10)
        
        # Create a text widget to display the results
        self.output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
        self.output_text.pack(pady=10)

    def get_events_during_time(self):
        # Implement the logic for 'Get Events during a Time'
        self.state = 'search_time'
        print("Searching events by a given time interval")
        window = tk.Toplevel(root)
        window.title("Search Events by Time Interval")
        window.geometry("300x400")

        # Title
        label = tk.Label(window, text="Search Events by Time Interval\nUse Format HH:MM:SS", font=("Helvetica", 16))
        label.pack(pady=10)

        # Create entry widgets for start and end times
        self.start_time_entry = tk.Entry(window, width=30)
        self.start_time_entry.pack(pady=10)
        self.end_time_entry = tk.Entry(window, width=30)
        self.end_time_entry.pack(pady=10)

        # Create a button to trigger text retrieval
        retrieve_button = tk.Button(window, text="Retrieve Text", command=self.retrieve_interval)
        retrieve_button.pack(pady=10)

        # Create a text widget to display the results
        self.output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
        self.output_text.pack(pady=10)




# Connect to the database
try:
    connection = psyc.connect(
        host="localhost",
        database="tevents2",
        user="postgres",
        password="password"
    )
    
    cursor = connection.cursor()
    
    print("Connection successful.\n")


except (Exception, psyc.Error) as error:
    print("Error while connecting to PostgreSQL.")
    quit()

print("Connected to the PostgreSQL database.")

# Create the main window
root = tk.Tk()
root.title("CSCI411 Event Database")
root.geometry("400x300")

container = gui(cursor)

# Main Title
label = tk.Label(root, text="Event Search Main Menu", font=("Helvetica", 16))
label.pack(pady=10)

# Create buttons
button1 = tk.Button(root, text="Search Events by Person", command=container.search_events_by_person)
button2 = tk.Button(root, text="Search Events by LinkID", command=container.search_events_by_link_id)
button3 = tk.Button(root, text="Search Link Details by LinkID", command=container.search_link_details_by_link_id)
button4 = tk.Button(root, text="Get Events during a Time", command=container.get_events_during_time)

# Pack buttons to the window
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()