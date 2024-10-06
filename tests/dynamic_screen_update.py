import os
import platform

print("hello world")

# Waiting for input
input("Press any key...")

# Clear the screen
if platform.system() == "Windows":
    os.system('cls')  # Windows
else:
    os.system('clear')  # macOS/Linux

print("hello you too user")