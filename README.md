# Elderly-Reminders-App by Fern Martins and Ken Chambers

## Project Goals: 
### The primary objective of this project was to create a user-friendly reminder application specifically designed for the elderly. The app aims to assist them in managing their daily tasks and appointments effectively.

## Significgance of Project:
### For this project, we wanted to find something that elderly people might be struggling with and do our part to make a good effort to fix a common problem. As we get older, some things start to go and you might need help doing things. The approach that we took to trying our best to help was to create an accessible reminder app to help the elderly people remember various things that may need to remember throughout their day.

## Installation and Usage: 
### One of the greatest aspects of this code is how it's basically ready to use fresh out of the box. After simply extracting the code and then importing it to your Python complier of choice, simply hit the run button and the GUI will open. Once in the app, users will have the following options: set reminders with a name and a time at which to go off at, view reminders that have previously been created, delete reminders that are no longer needed by imputting the name of said reminder and exiting the app.

## Code Structure:
### This app was created primaryly using the Tkinter library to accomplish the GUI side of the code which was then built upon with various classes and functions such as our set, display and delete methods for the reminders. Along with this, we implemented threading and the usage of semaphore and mutexes. By implementing threading, the program checks the time every minute to see if it is time for a user-created reminder to go off and with the help of semaphores and mutexes, we were able to make sure everything stays in synch with one other for optimal performance.

## Functionalities and Test Results:
### The basic functionality that we added to this app are the following:
  - Setting reminders: By including a name for the reminder and a time for it to trigger using a 24-Hour clock system, users can create reminders along with error handling for incorrectly inputing names and times plus error handling for adding duplicate reminders.
  - Displaying reminders: Once the specified time for a reminder approaches, by the use of a pop-up window, a message displaying the reminder will appear.
  - Deleting reminders: By typing in the name of an existing reminder, the specific reminder will be deleted
  - Triggering reminders: Reminders are triggered by the use of threading to check every minute to make sure it is time for the reminder to go off.

## Discussion and Conclusion:
### One of the biggest issues with our current system is that it solely operates on the user's current system time and is only for the current day so reminders cannot be set for the future. ALong with this, we currently have no way to save reminders after the app has be closed so in order for the reminder to trigger, the user would have to leave the app open. Another issue is that there is choice for what time system the user wants to use and only allows the 24-hour clock system.

### As for what we used specific from what was learned in-class, we made use of threading, semaphores and mutexes to allow for the app to work efficiently and properly with end goal of having a successful reminder app. By implementing threading, the program checks the time every minute to see if it is time for a user-created reminder to go off and with the help of semaphores and mutexes, we were able to make sure everything stays in synch with one other for optimal performance.




