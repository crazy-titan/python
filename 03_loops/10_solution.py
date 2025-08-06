# this is seen when you tries to open you lock screen or any password and if your password is
# wrong scheduled time increase and we have to wait for that much time, then we can attempt pass again

import time

wait_time = 1 # lets assume first its just 1 sec , we will update this 
max_attempt = 5 # i limit the number of attempt a user can have, we will update 
current_attempt = 0 # initially no attempt recorded, we will update

# for these type of situation we use while loops

while current_attempt < max_attempt: # comman sense
    print("Attempt:",current_attempt+1,"Wait-time:",wait_time)
    time.sleep(wait_time)
    wait_time *= 2 # double the wait-time
    current_attempt += 1

# best for learing experience, it is used is API also and many more,