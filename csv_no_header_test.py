import csv

with open('test_no_header.csv', 'r') as read:
    with open('result_no_header.csv', 'w') as write:
        reader = csv.reader(read)
        writer = csv.writer(write)

        for row in reader:
            print(row)
            writer.writerow([row[1], row[0]]) # make sure you pass in as a list
