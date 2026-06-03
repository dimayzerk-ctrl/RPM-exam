import time

from sim import contains_wake_word

start = time.time()

for _ in range(100):
    contains_wake_word("сим открой браузер")

end = time.time()

print(end - start)