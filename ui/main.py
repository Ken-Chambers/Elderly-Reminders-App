import time
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog


class Reminder:
    def __init__(self, task, time):
        self.task = task
        self.time = time
        self.isSet = True  # Initially set to True, modify as needed


class ReminderScheduler:
    def __init__(self):
        self.activeReminders = []
        self.running = False
        self.scheduler_thread = None

    def schedule_reminder(self, reminder):
        self.activeReminders.append(reminder)
        print(f"Reminder has been scheduled for {reminder.task} at {reminder.time}")

    def start_scheduler(self):
        print("Scheduler started!")
        self.running = True
        while self.running:
            currTime = time.strftime("%H:%M")
            for reminder in self.activeReminders:
                if reminder.time == currTime and reminder.isSet:
                    print(f"Hi there! It's time to {reminder.task}.")
            time.sleep(60)

    def stop_scheduler(self):
        self.running = False
        if self.scheduler_thread and self.scheduler_thread.is_alive():
            self.scheduler_thread.join()
        print("Scheduler has been stopped.")


class DailyReminderApp:
    def __init__(self):
        self.scheduler = ReminderScheduler()
        self.reminders = []
        self.reminders_lock = threading.Lock()
        self.scheduler_semaphore = threading.Semaphore(1)

        self.root = tk.Tk()
        self.root.title("Daily Reminders App")

        # Set the initial size of the window
        self.root.geometry("1920x1080")

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        self.create_menu()

    def create_menu(self):
        tk.Label(self.menu_frame, text="Welcome to the Daily Reminders App!", font=("Helvetica", 75)).pack()

        options = [
            ("Set a reminder", self.set_reminder),
            ("Delete an existing reminder", self.delete_reminder),
            ("Start the scheduler", self.start_scheduler),
            ("Stop the scheduler", self.stop_scheduler),
            ("List all reminders", self.list_reminders),
            ("Exit", self.exit_app),
        ]

        for text, command in options:
            tk.Button(self.menu_frame, text=text, command=command, font=("Helvetica", 50), bg="light blue",
                      fg="black").pack(pady=15)

    def set_reminder(self):
        task = simpledialog.askstring("Set Reminder", "Type in the name of your reminder:")
        time = simpledialog.askstring("Set Reminder", "Type in the time for your reminder to go off:")

        with self.reminders_lock:
            new_reminder = Reminder(task, time)
            self.reminders.append(new_reminder)

        messagebox.showinfo("Reminder Set", "Reminder set successfully!")

    def delete_reminder(self):
        task = simpledialog.askstring("Delete Reminder", "Enter the name of an existing task you want to delete:")

        with self.reminders_lock:
            for reminder in self.reminders:
                if reminder.task == task:
                    reminder.delete_reminder()
                    self.reminders.remove(reminder)
                    messagebox.showinfo("Reminder Deleted", f"Reminder for '{task}' deleted.")
                    break
            else:
                messagebox.showwarning("Reminder Not Found", f"No reminder found for '{task}'.")

    def start_scheduler(self):
        self.scheduler_semaphore.acquire()

        if not self.scheduler.running:
            self.scheduler_thread = threading.Thread(target=self.scheduler.start_scheduler)
            self.scheduler_thread.start()
        else:
            messagebox.showwarning("Scheduler Already Started", "Scheduler is already running.")

        self.scheduler_semaphore.release()

    def stop_scheduler(self):
        try:
            if self.scheduler.running:
                self.scheduler.stop_scheduler()
                messagebox.showinfo("Scheduler Stopped", "Scheduler stopped.")
            else:
                messagebox.showwarning("Scheduler Not Started",
                                       "Scheduler not started. Please start the scheduler first.")
        except AttributeError:
            messagebox.showwarning("Scheduler Not Started", "Scheduler not started. Please start the scheduler first.")

    def list_reminders(self):
        with self.reminders_lock:
            if not self.reminders:
                messagebox.showinfo("No Reminders", "There are no reminders.")
                return

            reminder_list = "\n".join(
                [f"{i + 1}. {reminder.task} - Time: {reminder.time}" for i, reminder in enumerate(self.reminders)])
            messagebox.showinfo("All Reminders", reminder_list)

    def exit_app(self):
        if self.scheduler.running:
            self.scheduler.stop_scheduler()

        self.root.destroy()


def main():
    app = DailyReminderApp()
    app.root.mainloop()


if __name__ == "__main__":
    main()
