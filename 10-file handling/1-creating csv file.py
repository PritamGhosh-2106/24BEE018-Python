import csv
data = [
    ["Name", "Roll no."],  
    ["Pritam", "24BEE018"]
]

with open("Student_data.csv", mode='w', newline='') as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)

print("CSV file has been created successfully")
