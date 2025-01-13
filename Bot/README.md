# Spamming Bot with Keyboard Interrupt and File Input

This code provides a basic spamming functionality using keyboard and mouse automation libraries. It allows spamming a user-defined string or reading words from a text file.


## How it works

1. The code imports necessary libraries:
   - `pyautogui` for mouse and keyboard automation.
   - `keyboard` for detecting keyboard presses.
   - `time` for introducing delays between spam messages.
2. It prompts the user to enter a string to spam (`string = input("Enter Here What you want to spammm... : \n")`).
3. It defines a function `spammingBot(string)` that continuously spams the provided string until the 'q' key is pressed.
   - Inside the loop:
     - It checks if the 'q' key is pressed (`if(kbd.is_pressed('q')):`). If so, it breaks out of the loop and terminates the spamming.
     - It types the provided string using `pyautogui.typewrite(string)`.
     - It presses the "enter" key using `pyautogui.press("enter")`.
     - It introduces a 2-second delay between each spam message using `time.sleep(2)`.
4. It attempts to import the `spammingBot` function from a module named `bot1.py` (commented out line `from bot1 import spammingBot`). This suggests the possibility of using the function in another script.
5. It opens a text file named "text.txt" in read mode (`with open('D:\work\Projects\Bot\text.txt','r') as txt :`). This path might need adjustment based on your file location.
6. It reads the content of the text file (`content = txt.read()`).
7. It iterates over each word in the text file content (`for word in content.split(" ")`):
   - It prints each word for reference (`print(word)`)
   - It calls the `spammingBot(word)` function to spam the current word.

## Running the code

1. Save the code as a Python file (e.g., `spam_bot.py`).
2. Ensure you have the required libraries installed (`pyautogui`, `keyboard`). You can install them using `pip install pyautogui keyboard`.
3. Open a terminal or command prompt and navigate to the directory where you saved the file.
4. Make sure the "text.txt" file is present in the specified location (`D:\work\Projects\Bot\text.txt`). Adjust the path if needed.
5. Run the script using the following command:

```bash
python spam_bot.py