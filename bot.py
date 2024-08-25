import pyautogui
import time

def spammer(message: str, n: int) -> None:
    """Sends a message multiple times using pyautogui."""
    # List of messages to send
    messages = [f"{message}" for i in range(1, n + 1)]

    print("Spam starting in seconds:")

    # Small delay to switch to WhatsApp Web tab
    for i in range(5, 0, -1):
        print(i, end="..")
        time.sleep(1)  # Adjust based on how long you need to switch to the tab
    print("\nSpam started!")

    # Continuously send messages
    for i,msg in enumerate(messages):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
        time.sleep(1)  # Wait 2 seconds before sending the next message
        print(f"message {i+1} sent!")


