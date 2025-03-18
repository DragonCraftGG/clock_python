import time
from datetime import datetime

def print_clock():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"+-----------+")
        print(f"| {current_time}  |")
        print(f"+-----------+")
        time.sleep(1)
        print("\033[H\033[J")  # Очистка консоли (для Windows)

print_clock()