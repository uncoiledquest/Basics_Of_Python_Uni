sec= int(input("Enter seconds: "))
hours= 0
minutes=0
days=0

days= sec//86400
sec= sec%86400
    
hours= sec//3600
sec= sec%3600

minutes= sec//60
sec= sec%60

print(f"Days: {days} Hours: {hours} Minutes: {minutes} Seconds: {sec}")
