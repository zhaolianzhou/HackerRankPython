import sys

time='12:05:45PM'
def timeConvert(time):
    post = time[-2:]
    pre = time[0:2]
    if post=='PM' and pre != '12':
        pre=int(pre)+12
        return str(pre)+time[2:-2]
    elif post=='AM' and pre=='12':
        return '00'+time[2:-2]
    else:
        return time[:-2]

print(timeConvert(time))