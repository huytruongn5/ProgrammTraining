import csv


o = open('test.csv')

# with open('test.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


with open('test.csv', 'r') as r:
    with open('result.csv', 'w') as w:
        fieldnames=['last_name', 'first_name']
        reader = csv.DictReader(r)
        writer = csv.DictWriter(w, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            print(row)
            writer.writerow(row)


