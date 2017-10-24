Score = [87, 99, 90, 65, 70]
Total_Score = 0
for count in range(5):
    print('The %d Student\'s score is %d' %(count+1, Score[count]) )
    Total_Score+=Score[count]

print('=====================')
print('Total score: %d' %Total_Score)

