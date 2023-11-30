class Reminder:
    def __init__(self, task, time):
        self.task = task
        self.time = time
        self.isSet = False

    def set_reminder(self):
        self.isSet = True
        print(f"Reminder has been set for {self.task} at {self.time}")

    def delete_reminder(self):
        self.isSet = False
        print(f"Reminder for {self.task} has been deleted")