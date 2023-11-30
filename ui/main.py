from reminders.reminder import Reminder
from reminders.scheduler import ReminderScheduler

def main():
    scheduler = ReminderScheduler()

    print("Welcome to the Daily Reminders App!")
    print("To set a reminder, type 1")
    print("To delete an existing reminder, type 2")
    print("To start the scheduler, type 3")
    print("To stop the scheduler, type 4")
    choice = input("Type your response here: ")

    if choice == '1':
        print("Certainly, let's start creating your reminder")
        task = input("Type in the name of your reminder: ")
        time = input("Now type in the time for your reminder to go off: ")
    elif choice == '2':
        print("Ok, let's start the deletion")
        task = input("Enter the name of an existing task you want to delete: ")
        time = input("Now enter the time of the existing task you want to delete:")
        myReminder = Reminder(task, time)
        myReminder.delete_reminder()

    elif choice == '3':
        scheduler.start_scheduler()

    elif choice == '4':
        scheduler.stop_scheduler()
    else:
        print("Oops, you inputted an invalid number, please enter one of the following numbers instead: 1, 2, 3, 4")

if __name__ == "__main__":
    main()