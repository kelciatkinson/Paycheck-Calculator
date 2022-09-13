#Enter values for week 1 of pay period
weekday_1_hrs = input("Enter Monday-Saturday Hours for Week 1: ")
weekday_1_hrs = float(weekday_1_hrs)
sunday_1_hrs = input("Enter Sunday Hours for Week 1: ")
sunday_1_hrs = float(sunday_1_hrs)

#Enter values for week 2 of pay period
weekday_2_hrs = input("Enter Monday-Saturday Hours for Week 2: ")
weekday_2_hrs = float(weekday_2_hrs)
sunday_2_hrs = input("Enter Sunday Hours for Week 2: ")
sunday_2_hrs = float(sunday_2_hrs)

#Enter rate for weekday and Sunday
weekday_rate = input("Enter Monday-Saturday Rate: ")
weekday_rate = float(weekday_rate)
sunday_rate = weekday_rate + 10

#print(weekday_hrs, weekday_rate)
reg = (weekday_rate * weekday_1_hrs) + (weekday_rate * weekday_2_hrs)
sunday_ot = (sunday_1_hrs * sunday_rate) + (sunday_2_hrs * sunday_rate)
tax_rate = .8
pay = (reg + sunday_ot) * tax_rate

print("Paycheck after Tax:", pay)
