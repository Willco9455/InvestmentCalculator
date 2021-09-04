# could be user inputs 
pdsPerYr = 60
yrsInvesting = 13
fundPct = 10
fundChrg = 2
startAmount = 260


pctPerYear = fundPct - fundChrg
total = startAmount

# finds the multipler to times the total by 
pctMultiplier = float('1.0' + (str(pctPerYear)).replace('.',''))

for i in range(1, yrsInvesting + 1):
    total = pdsPerYr + (total * (pctMultiplier))
    print(f'Year{i} £' + str(round(total, 2)))
    

 
