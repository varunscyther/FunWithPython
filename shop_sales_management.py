"""
Database of sales of some online shop is given. Each line of the input file is a record of the following view:
(customer item quantity), customer and item are strings without spaces.

Create a list of all customers, and for each customer, calculate the number of units of each item type.

Input format: Shopping information is entered in the specified format.

Output format: Print the list of all customers in the lexicographical order, after the name of each customer,
print a colon, then print the list of names of all products purchased by this customer in the lexicographical order,
after the name of each product, print the number of units purchased by this customer.
Information about each item is printed on a separate line.

Possible test cases :
--------------------------------------------
Input data:
Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5


Program output:
Ivanov:
envelope 5
marker 3
paper 17
Petrov:
envelope 20
pens 5

--------------------------------------------

Input data:
Ivanov aaa 1
Petrov aaa 2
Sidorov aaa 3
Ivanov aaa 6
Petrov aaa 7
Sidorov aaa 8
Ivanov bbb 3
Petrov bbb 7
Sidorov aaa 345
Ivanov ccc 45
Petrov ddd 34
Ziborov eee 234
Ivanov aaa 45


Program output:
Ivanov:
aaa 52
bbb 3
ccc 45
Petrov:
aaa 9
bbb 7
ddd 34
Sidorov:
aaa 356
Ziborov:
eee 234

-------------------------------------------
Input data:
TKSNUU FKXYPUGQ 855146
TKSNUU FKXYPUGQ 930060
TKSNUU FKXYPUGQ 886973
TKSNUU FKXYPUGQ 59344
TKSNUU FKXYPUGQ 296343
TKSNUU FKXYPUGQ 193166
TKSNUU FKXYPUGQ 211696
TKSNUU FKXYPUGQ 821064
TKSNUU FKXYPUGQ 672846
TKSNUU FKXYPUGQ 820341
TKSNUU FKXYPUGQ 350693
TKSNUU FKXYPUGQ 469538
TKSNUU FKXYPUGQ 849069
TKSNUU FKXYPUGQ 502007
TKSNUU FKXYPUGQ 961595
TKSNUU FKXYPUGQ 747271
TKSNUU FKXYPUGQ 863648
TKSNUU FKXYPUGQ 952069
TKSNUU FKXYPUGQ 286019
TKSNUU FKXYPUGQ 364841
TKSNUU FKXYPUGQ 455930
TKSNUU FKXYPUGQ 100486
TKSNUU FKXYPUGQ 335026
TKSNUU FKXYPUGQ 197672
TKSNUU FKXYPUGQ 217640
TKSNUU FKXYPUGQ 612549
TKSNUU FKXYPUGQ 622501
TKSNUU FKXYPUGQ 96554
TKSNUU FKXYPUGQ 327166
TKSNUU FKXYPUGQ 425399
TKSNUU FKXYPUGQ 362309
TKSNUU FKXYPUGQ 78477
TKSNUU FKXYPUGQ 258916
TKSNUU FKXYPUGQ 297923
TKSNUU FKXYPUGQ 8891
TKSNUU FKXYPUGQ 13639
TKSNUU FKXYPUGQ 77308
TKSNUU FKXYPUGQ 707620
TKSNUU FKXYPUGQ 68205
TKSNUU FKXYPUGQ 256702
TKSNUU FKXYPUGQ 668334
TKSNUU FKXYPUGQ 968673
TKSNUU FKXYPUGQ 138125
TKSNUU FKXYPUGQ 222904
TKSNUU FKXYPUGQ 214091
TKSNUU FKXYPUGQ 500231
TKSNUU FKXYPUGQ 19611
TKSNUU FKXYPUGQ 491343
TKSNUU FKXYPUGQ 404307
TKSNUU FKXYPUGQ 68367
TKSNUU FKXYPUGQ 287107
TKSNUU FKXYPUGQ 794935
TKSNUU FKXYPUGQ 254217
TKSNUU FKXYPUGQ 206370
TKSNUU FKXYPUGQ 202761
TKSNUU FKXYPUGQ 929017
TKSNUU FKXYPUGQ 843359
TKSNUU FKXYPUGQ 955269
TKSNUU FKXYPUGQ 134139
TKSNUU FKXYPUGQ 946168
TKSNUU FKXYPUGQ 967781
TKSNUU FKXYPUGQ 856474
TKSNUU FKXYPUGQ 465070
TKSNUU FKXYPUGQ 580526
TKSNUU FKXYPUGQ 172109
TKSNUU FKXYPUGQ 191703
TKSNUU FKXYPUGQ 207916
TKSNUU FKXYPUGQ 512264
TKSNUU FKXYPUGQ 533081
TKSNUU FKXYPUGQ 577208
TKSNUU FKXYPUGQ 831389
TKSNUU FKXYPUGQ 439158
TKSNUU FKXYPUGQ 565633
TKSNUU FKXYPUGQ 452643
TKSNUU FKXYPUGQ 164426
TKSNUU FKXYPUGQ 540743
TKSNUU FKXYPUGQ 880704
TKSNUU FKXYPUGQ 868529
TKSNUU FKXYPUGQ 240742
TKSNUU FKXYPUGQ 868865
TKSNUU FKXYPUGQ 910442
TKSNUU FKXYPUGQ 146737
TKSNUU FKXYPUGQ 820984
TKSNUU FKXYPUGQ 660948
TKSNUU FKXYPUGQ 957975
TKSNUU FKXYPUGQ 135847
TKSNUU FKXYPUGQ 401865
TKSNUU FKXYPUGQ 982859
TKSNUU FKXYPUGQ 748454
TKSNUU FKXYPUGQ 354734
TKSNUU FKXYPUGQ 525638
TKSNUU FKXYPUGQ 119140
TKSNUU FKXYPUGQ 484816
TKSNUU FKXYPUGQ 616539
TKSNUU FKXYPUGQ 682553
TKSNUU FKXYPUGQ 841541
TKSNUU FKXYPUGQ 713063
TKSNUU FKXYPUGQ 433453
TKSNUU FKXYPUGQ 465340
TKSNUU FKXYPUGQ 985635


Program output:
TKSNUU:
FKXYPUGQ 49769497


"""


def collect_data() :
    global formatted_data_lst
    user_data = []
    while True :
        line = input().split()
        if line :
            user_data.append(line)
        else :
            break
    formatted_data_lst = list(user_data)


def maintain_customer_detail() :
    global customer_details
    customer_details = {}
    for x in formatted_data_lst :
        if not customer_details :
            customer_items = {x[1] : x[2]}
        elif customer_details.get(x[0]) is not None :
            customer_items = customer_details[x[0]]
            if customer_items.get(x[1]) is not None :
                existing_customer_item_quantity = customer_items[x[1]]
                updated_items = {x[1] : int(existing_customer_item_quantity) + int(x[2])}
                customer_items.update(updated_items)
            else :
                new_customer_items = {x[1] : x[2]}
                customer_items.update(new_customer_items)
        else :
            customer_items = {x[1] : x[2]}
        customer_details[x[0]] = customer_items
    print(customer_details)


collect_data()
maintain_customer_detail()
