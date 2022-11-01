import string
import secrets
from time import sleep

n = 0
while True:
        n = n + 1
        total = string.digits + string.ascii_letters + string.punctuation
        random = secrets.choice(total)
        print(random, end='', flush=True)
        sleep(0.05) # Seconds needed for printing a character
        if n == 75: # Change line length
            print('')
            n = 0
        