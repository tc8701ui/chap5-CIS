import random
import time
random.seed(time.time())

dice_rolls = 0
sums = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
print(sums)

dice_rolls = int(input("How many times to roll the dice?\n"))

while dice_rolls>1:
    sums = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
    for dice_roll in range(dice_rolls):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        sum_of_dice = dice1+dice2
        #print(sum_of_dice)
        sums[str(sum_of_dice)]+=1
    #print(sums)
    print("Dice roll histogram: \n")
    for number in sums:
        print('%ss:'%number,end=' ')
        for star in range(sums[number]):
            print('*',end=' ')
        print()
    dice_rolls = int(input("How many times to roll the dice?\n"))
    
