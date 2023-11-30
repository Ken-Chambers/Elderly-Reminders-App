import time

class ReminderScheduler:
    def __init__(self):
        self.activeReminders = []

    def schedule_reminder(self, reminder):
        self.activeReminders.append(reminder)
        print(f"Reminder has be scheduled for {reminder.task} at {reminder.time}")

    def start_scheduler(self):
        print("Scheduler started!")
        while True:
            currTime = time.strftime("%H:%M")
            for reminder in self.activeReminders:
                if reminder.time == currTime and reminder.isSet:
                    print(f"Hi there! It's time to {reminder.task}.")
            time.sleep(60)

    def stop_scheduler(self):
        print("Scheduler has been stopped.")