import time
import threading

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
        if self.scheduler_thread:
            self.scheduler_thread.join()
        print("Scheduler has been stopped.")