import pyautogui, time, datetime

time.sleep(2)  # Small delay to allow you to switch to the Telegram window

while True:
    # Display the time at which the message is sent
    print(datetime.datetime.now())

    # First reminder
    pyautogui.typewrite("Reminder: Drink water!")
    pyautogui.press("enter")
    time.sleep(31)  # Wait for 31 seconds

    # Second reminder
    print(datetime.datetime.now())
    pyautogui.typewrite("Reminder: Take medicine!")
    pyautogui.press("enter")
    time.sleep(31)  # Wait for 31 seconds

    # Third reminder
    print(datetime.datetime.now())
    pyautogui.typewrite("Reminder: Take the dog for a walk!")
    pyautogui.press("enter")
    time.sleep(31)  # Wait for 31 seconds

    # Fourth reminder
    print(datetime.datetime.now())
    pyautogui.typewrite("Reminder: Drink water!")
    pyautogui.press("enter")
    time.sleep(31)  # Wait for 31 seconds

    # Fifth reminder
    print(datetime.datetime.now())
    pyautogui.typewrite("Reminder: Drink water!")
    pyautogui.press("enter")
    time.sleep(31)  # Wait for 31 seconds
