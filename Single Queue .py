
random_digit = [0] #take a empty list and enter 1st element 0
inter_arrival_time = [0] #take a empty list and enter 1st element 0
arrival_time = []
random_digit_service = []
service_time_begin = []
service_time = []
service_time_end = []
wating_time = []
idel_time = [0] #take a empty list and enter 1st element 0
spend_in_system = []
cust_no =[]
customer_size = int(input('Enter Queue Size: '))

print("Enter Random Digit For Arrival Time For each Customer: \n")


for i in range(int(customer_size)):
        cust_no.append(i+1)
        n = input("RD Arrival :")
        random_digit.append(int(n))

for i in range (int(customer_size)):
        if random_digit[i]>0 and random_digit[i]<126:
                inter_arrival_time.append(1)
        elif random_digit[i]>125 and random_digit[i]<251:
                inter_arrival_time.append(2)
        elif random_digit[i]>250 and random_digit[i]<376:
                inter_arrival_time.append(3)
        elif random_digit[i]>375 and random_digit[i]<501:
                inter_arrival_time.append(4)
        elif random_digit[i]>500 and random_digit[i]<626:
                inter_arrival_time.append(5)
        elif random_digit[i]>625 and random_digit[i]<751:
                inter_arrival_time.append(6)
        elif random_digit[i]>750 and random_digit[i]<876:
                inter_arrival_time.append(7)
        elif random_digit[i]>875 and random_digit[i]<=1000:
                inter_arrival_time.append(8)
        elif random_digit[i]>1000:
                print("You Enter the value more then 1000 please enter less then 1000 or equal")

print("Enter Random Digit For Service Time For each Customer: \n")

for i in  range (int(customer_size)):
        rd_service = int(input("Random Digit For Service Time: "))
        random_digit_service.append(int(rd_service))

for i in range (int(customer_size)):
        if random_digit_service[i]>0 and random_digit_service[i]<=10:
                service_time.append(1)
        elif random_digit_service[i]>10 and random_digit_service[i]<=30:
                service_time.append(2)
        elif random_digit_service[i] > 30 and random_digit_service[i]<= 60:
                service_time.append(3)
        elif random_digit_service[i]>60 and random_digit_service[i]<=85:
                service_time.append(4)
        elif random_digit_service[i]>85 and random_digit_service[i]<=95:
                service_time.append(5)
        elif random_digit_service[i] > 95 and random_digit_service[i] <= 100:
                service_time.append(6)
        else:
                print("Please Enter Less Then 100")

cumulative = 0
for i in inter_arrival_time:
        cumulative += i
        arrival_time.append(cumulative)


ser_beg = arrival_time[0]
service_time_begin.append(int(ser_beg))
ser_end = service_time[0]+service_time_begin[0]
service_time_end.append(int(ser_end))
service = 0


for i in range (1,int(customer_size)):
        if arrival_time[i] >= service_time_end[i-1]:
                service = arrival_time[i]
                service_time_begin.append(service)
                ste = service_time[i]+service_time_begin[i]
                service_time_end.append(ste)
        else:
            service = service_time_end[i-1]
            service_time_begin.append(service)
            ste = service_time[i]+service_time_begin[i]
            service_time_end.append(ste)


for i in range (int(customer_size)):
    wait = service_time_begin[i] - arrival_time[i]
    wating_time.append(wait)


for i in range(int(customer_size)):
    spend = service_time_end[i]-service_time_begin[i]
    spend_in_system.append(spend)

for i in range(1,int(customer_size)):
    idel = service_time_begin[i]-service_time_end[i-1]
    idel_time.append(idel)

#Print All Value

print("Customer No |\tRD for AT |\tTime since last Arrival |\tArrival Time |\tRD for ST |\tST Begin |\tService Time |\tService time End |\t   Waiting time |\t   Time Spend |\tLdel Time |\n")
for i in range (int(customer_size)):
        print("\t",cust_no[i],"\t\t\t",random_digit[i],"\t\t\t",inter_arrival_time[i],"\t\t\t\t\t\t\t",arrival_time[i],"\t\t\t\t",random_digit_service[i],"\t\t",service_time_begin[i],"\t\t\t",service_time[i],"\t\t\t\t",service_time_end[i],"\t\t\t\t\t",wating_time[i],"\t\t\t\t\t      ",spend_in_system[i],"\t\t\t\t\t      ",idel_time[i])
