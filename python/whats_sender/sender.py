import pywhatkit
from datetime import datetime, time

now = datetime.now()

chour = now.strftime("%H")
cminute = now.minute
print(chour)
print(cminute)
mobile = input('Enter Mobile No of Receiver : ')
message = input('Enter Message you wanna send : ')
hour = int(chour)
minute = int(cminute + 1)
print(minute)

pywhatkit.sendwhatmsg(mobile,message,hour,minute)