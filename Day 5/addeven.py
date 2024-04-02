target = int(input()) # Enter a number between 0 and 1000

evensum = 0

for a in range (0,target+1,2):
    evensum += a

print(evensum)
