#convert seconds into hours,minutes and seconds
time=int(input("enter your seconds:"))
hour=time//3600
time%=3600
minutes=time//60
time%=60
second=time//1
time%=1
print("%d hour:%d minutes:%d seconds"%(hour,minutes,second))

