import time

segundos = 0

while True:
    print(f"\rTempo: {segundos} segundos", end="")
    time.sleep(1)
    segundos += 1