import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import threading

class ReminderApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Reminder App")
        self.reminders = []  # List to store reminders
        self.reminders_lock = threading.Lock()  # Mutex to synchronize access to reminders list
        self.semaphore = threading.Semaphore(1)  # Semaphore to control access to check_reminders function
        self.thread_running = False  # Flag to track whether the check_reminders thread is running
        self.create_widgets()

    def create_widgets(self):
        # Set the initial size of the window
        self.root.geometry("1920x1080")

        # Main Frame
        main_frame = tk.Frame(self.root)
        main_frame.pack()

        # Welcome Text with added space
        tk.Label(main_frame, text="Welcome to your Reminder App", font=("Helvetica", 60), fg='dark blue', bg='light blue').pack(pady=75)

        # Frame for Name and Time
        entry_frame = tk.Frame(main_frame)
        entry_frame.pack()

        # Labels and Entry widgets using pack
        name_label = tk.Label(entry_frame, text="Enter Reminder Name:", font=("Helvetica", 40))
        name_label.pack(pady=10)

        self.name_entry = tk.Entry(entry_frame, font=("Helvetica", 35), width=20)
        self.name_entry.pack(pady=10)

        time_label = tk.Label(entry_frame, text="Enter Reminder Time (HH:MM):", font=("Helvetica", 35))
        time_label.pack(pady=10)

        self.time_entry = tk.Entry(entry_frame, font=("Helvetica", 40), width=20)
        self.time_entry.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack()

        # Buttons
        options = [
            ("Set Reminder", self.set_reminder),
            ("Show Reminders", self.show_reminders),
            ("Delete Reminder", self.delete_reminder),
            ("Exit", self.exit_app),
        ]

        for i, (text, command) in enumerate(options):
            tk.Button(button_frame, text=text, command=command, font=("Helvetica", 35), bg='pink').pack(pady=15)

    def set_reminder(self):
        # Function to set a new reminder
        name = self.name_entry.get()
        time_str = self.time_entry.get()

        if name and time_str:
            with self.reminders_lock:
                # Check if a reminder with the same name and time already exists
                if any(reminder["name"].lower() == name.lower() and reminder["time"].strftime('%H:%M') == time_str for reminder in self.reminders):
                    messagebox.showerror("Error", f"A reminder with the same name and time already exists.")
                else:
                    try:
                        # Convert input time string to datetime object
                        time = datetime.strptime(time_str, "%H:%M")
                        reminder = {"name": name, "time": time}

                        # Add the new reminder to the list
                        self.reminders.append(reminder)

                        # Start a separate thread to check for reminders
                        if not self.thread_running:
                            threading.Thread(target=self.check_reminders).start()
                            self.thread_running = True

                        messagebox.showinfo("Success", "Reminder set successfully!")
                    except ValueError:
                        messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
        else:
            messagebox.showerror("Error", "Please enter both name and time.")

    def show_reminders(self):
        # Function to show all reminders
        with self.reminders_lock:
            if not self.reminders:
                messagebox.showinfo("Reminders", "No reminders set.")
                return

            # Create a formatted string with all reminders
            reminder_list = "\n".join(
                [f"{reminder['name']} at {reminder['time'].strftime('%H:%M')}" for reminder in self.reminders])
            messagebox.showinfo("Reminders", reminder_list)

    def delete_reminder(self):
        # Function to delete a reminder
        with self.reminders_lock:
            if not self.reminders:
                messagebox.showinfo("No Reminders", "No reminders to delete.")
                return

            # Ask user for the name of the reminder to delete
            selected_name = simpledialog.askstring("Delete Reminder", "Enter the name of the reminder to delete:")
            if selected_name:
                found = False
                for reminder in self.reminders:
                    if reminder["name"].lower() == selected_name.lower():
                        # Remove the reminder from the list
                        self.reminders.remove(reminder)
                        messagebox.showinfo("Success", f"Reminder '{selected_name}' deleted successfully.")
                        found = True
                        break

                if not found:
                    messagebox.showinfo("Reminder Not Found", f"No reminder found with the name '{selected_name}'.")

    def check_reminders(self):
        # Function to check and show reminders when it's time
        with self.semaphore:
            while self.reminders:
                current_time = datetime.now().time()

                with self.reminders_lock:
                    for reminder in self.reminders:
                        if current_time >= reminder["time"].time():
                            # Display a reminder message
                            messagebox.showinfo("Reminder", f"It's time for {reminder['name']}!")
                            # Remove the triggered reminder from the list
                            self.reminders.remove(reminder)

                # Check every 1 minute
                threading.Event().wait(60)

    def exit_app(self):
        # Function to exit the application
        # Add any necessary cleanup code here before quitting
        self.thread_running = False  # Stop the check_reminders thread
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
