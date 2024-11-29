turpinat=True

import random

dilers=0
speletajs=0

for i in range (0,2):
   
    speletajs+=random.randint(1,11)
    dilers+=random.randint(1,11)
    

        
if dilers < 16:
    dilers += random.randint(1,11)
    
if dilers == 21:
    print('Dilers uzvareja :D')
elif dilers > 21:
    print('Dilers zaudeja!:D')
    
    print(dilers)

    
while turpinat:
    user = input('Panemt vel vienu karti?[Y/N]')
    if user=='N' or user =='n':
        break
    speletajs += random.randint(11)
     y
    if dilers == 21:
        print('speletajs  zaudeja D:')
        break
    elif dilers > 21:
        print('Dilers uzvarēja:D')
        break