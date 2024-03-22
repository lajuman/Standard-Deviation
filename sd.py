# Import libraries
import numpy as np

print ('\n--- Mean, Variance, Standard Deviation ---')

#Sample or Population
while True:
    sp = input('Data from Sample or Population ( S / P )? ')
    if sp=='s' or sp=='S':
        sp = 'Sample'
        break
    elif sp=='p' or sp=='P':
        sp = 'Population'
        break
    else :
        print('Input S or P!')
        continue

# How many data
ni = int(input('How many data? '))

# Input data
print(f'Input {ni} numbers from {sp}')
data = []
for i in range(ni):
    a = float(input(f'  Data #{i+1}: '))
    data.append(a)  
    i += 1
n = len(data)
print(f'{data} contains {n} data')

# Mean from numpy
mean = np.mean(data)

# Make sure mean from numpy
sum_squared_diff = np.sum((data - mean)**2)

# Variance and SD from Sample
sds = np.sqrt(sum_squared_diff / (n - 1))
vs = sds**2

# Variance and SD from Population
sdp = np.sqrt(sum_squared_diff / n)
vp = sdp**2

# Print Mean, Variance and SD
print(f'Mean\t\t\t: {round(mean,4)}')
if sp == 'Sample':
    print(f'Variance of {n} {sp}\t: {round(vs,4)}')
    print(f'SD of {n} {sp}\t\t: {round(sds,4)}')
elif sp == 'Population':
    print(f'Variance ({sp})\t: {round(vp,4)}')
    print(f'SD ({sp})\t\t: {round(sdp,4)}')
else:
    pass
print ('-'*40+'\n')
