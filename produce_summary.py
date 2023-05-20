delivery_report =["um-deliveries-day-1.txt","um-deliveries-day-2.txt","um-deliveries-day-3.txt"]
def delivery_msg(day, filename):
        print(f"Day {day}")
        the_file = open(filename)
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')

            melon = words[0]
            count = words[1]
            amount = words[2]

            print(f"Delivered {count} {melon}s for total of ${amount}")
        the_file.close()

for x,file in enumerate(delivery_report):
    delivery_msg(x+1, file)
