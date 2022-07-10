# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )

melon_cost = 1.00
oders_log = open("customer-orders.txt")



def underpaid_customers(oders_log):
    negative_balance = 0
    positive_balance = 0
    

    for line in oders_log:
        line = line.rstrip()
        columns = line.split('|')

        customer_name = columns[1]
        number_of_items = float(columns[2])
        customer_paid = float(columns[3])

        customer_expected = number_of_items * melon_cost
        if customer_expected != customer_paid:
            print(f"{customer_name} paid ${customer_paid:.2f}",
                  f"expected ${customer_expected:.2f}"
                 )
            
            if customer_expected > customer_paid:
                customer_underpaid = customer_expected - customer_paid
                negative_balance += customer_underpaid
                # print(customer_underpaid)
            
            elif customer_expected < customer_paid:
                customer_overpaid = customer_paid - customer_expected
                positive_balance += customer_overpaid
                print(customer_overpaid)
    
    total_balance = positive_balance - negative_balance
    print(f"We have negative balance of {negative_balance}")
    print(f"We have positive balance of {positive_balance}")
    print(f"Total balance is {total_balance:.2f}")
                


underpaid_customers(oders_log)