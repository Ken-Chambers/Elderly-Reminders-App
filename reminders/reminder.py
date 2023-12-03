import threading
from datetime import datetime

class Reminder:
    def __init__(self, task, time):
        self.task = task
        self.time = time
        self.is_set = False
        self.lock = threading.Lock()  # Mutex for protecting critical sections
        self.semaphore = threading.Semaphore(1)  # Semaphore to control access to a resource

    def set_reminder(self):
        with self.lock:
            self.semaphore.acquire()  # Acquire the semaphore
            self.is_set = True
            print(f"Reminder has been set for {self.task} at {self.time}")
            self.semaphore.release()  # Release the semaphore

    def delete_reminder(self):
        with self.lock:
            self.semaphore.acquire()  # Acquire the semaphore
            self.is_set = False
            print(f"Reminder for {self.task} has been deleted")
            self.semaphore.release()  # Release the semaphore


    def display_reminder(self):
        with self.lock:
            status = "Set" if self.is_set else "Not Set"
            print(f"Task: {self.task}, Time: {self.reminder_time.strftime('%H:%M')}, Status: {status}")
