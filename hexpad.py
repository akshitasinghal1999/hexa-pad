import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

matrix = [ [1 , 2 , 3 , 'A'],
         [4 , 5 , 6 , 'B'],
         [7 , 8 , 9 , 'C'],
         ['*' , 0 , '#' , 'D'] ]

row = [ 11 , 13 , 15 , 19]
col = [18 , 22 , 24 , 26]

for j in range(4):
    GPIO.setup(col[j] , GPIO.OUT)
    GPIO.output(col[j] , 1)
    
for i in range(4):
    GPIO.setup(row[i] , GPIO.IN , pull_up_down = GPIO.PUD_UP)
    
try:
    while True:
        for j in range(4):
            GPIO.output(col[j] , 0)
            
            for i in range(4):
                    if GPIO.input(row[i]) == 0:
                        print(matrix[i][j])
                        while GPIO.input(row[i]) == 0:
                            pass
            GPIO.output(col[j],1)
    
    
       
        
        
                        
                    
        
except KeyboardInterrupt:
    GPIO.cleanup(( 11 , 13 , 15 ,19 , 18 , 22 , 24 , 26))
