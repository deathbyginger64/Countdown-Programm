import time

tottime = int(input("Please enter the time (in seconds) : "))

for x in reversed(range(0,tottime + 1)):
    hours = x // 3600
    minutes = (x % 3600) // 60
    seconds = x % 60
    print(f"00:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!!!")






# for x in reversed(range(0,tottime + 1)):  since if only tottime had been written then the time printed would be whole -1 , thus we did +1
# minutes = x // 60  // is the floor division operator , it removes the decimal part after the division
# (x % 3600) gives us the leftover seconds
