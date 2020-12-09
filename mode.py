from collections import Counter
import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
newdata =[]
for i in range(len(filedata)):
    num = filedata[i][1]
    newdata.append(num)

    
data = Counter(newdata)
mode = {
        "50-60":0,
        "60-70":0,
        "70-80":0
}

for height, occurance in data.items():
    if 50 < float(height)< 60:
        mode["50-60"] += occurance
    if 60 < float(height)< 70:
        mode["60-70"] += occurance
    if 70 < float(height)< 80:
        mode["70-80"] += occurance

mode_range, mode_occurence = 0, 0
for range, occurence in mode.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")