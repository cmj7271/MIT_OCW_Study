# a에서 임금 변화가 없었음 --> 
# 이를 6개월마다 일정 비율로 증가하는 것으로 바꾼다.

# semi_annual_raise : 10진수(.10)로 입력받는다.
# 이 비율에 따라 6개월마다 월급이 증가한다.

def return_float(str) :
    str = str[1:]
    length = len(str)
    integer = int(str)
    return integer / (10**length)


annual_salary = int(input("Enter your annual salary "))

portion_saved = input("Enter the percent of your salary to save, as a decimal ")
portion_saved = return_float(portion_saved)

total_cost = int(input("Enter the cost of your dream home "))

semi_annual_raise = input("Enter the semi-annual raise, as a deciaml. : ")
semi_annual_raise = return_float(semi_annual_raise)

portion_down_payment = 0.25
current_saving = 0
r = 0.04
monthly_salary = 0

month = 0
monthly_r = r/12
monthly_salary = annual_salary/12

cost_to_pay = total_cost * portion_down_payment
while current_saving < cost_to_pay :
    #if month != 0 and month % 6 == 0 :
    #    monthly_salary *= (1 + semi_annual_raise)
    monthly_save = monthly_salary * portion_saved
    current_saving *= (1 + monthly_r)
    current_saving += monthly_save
    
    month += 1
    if month % 6 == 0 :
        monthly_salary *= (1 + semi_annual_raise)

print("Number of months", month)