#
import value_return

hour = value_return.get_hour(3800)
minutes = value_return.get_minutes(3800)
seconds = value_return.get_seconds(3800)

add_zero_hr = True
add_zero_mins = True
add_zero_secs = True
if(hour > 10):
    add_zero_hr = False

if(minutes > 10):
    add_zero_mins = False

if(seconds > 10):
    add_zero_secs = False

colon_hr = ''
if(add_zero_hr):
    colon_hr = '0'

colon_mins = ':'
if(add_zero_mins):
    colon_mins = ':0'

colon_secs = ':'
if(add_zero_secs):
    colon_secs = ':0'

print(colon_hr + str(hour) + colon_mins + str(minutes) + colon_secs + str(seconds))
