import csv
import random
import time

x_value = 0
total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0

attributes = ["Time", "lane_1", "lane_2", "lane_3", "lane_4"]




with open('data/data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=attributes)
    csv_writer.writeheader()

while True:

    with open('data/data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=attributes)
        x_value = time.strftime("%I:%M", time.localtime())
        total_1 = random.randint(15, 30)
        total_2 = random.randint(15, 30)
        total_3 = random.randint(15, 30)
        total_4 = random.randint(15, 30)

        info = {
            "Time": x_value,
            "lane_1": total_1,
            "lane_2": total_2,
            "lane_3": total_3,
            "lane_4": total_4
        }

        print(x_value, total_1, total_2, total_3, total_3)
        
        csv_writer.writerow(info)

    time.sleep(1)
