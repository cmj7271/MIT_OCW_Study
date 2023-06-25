# total_cost : 집가격
# portion_down_payment : 계약금으로 집가격의 0.25로 고정
# current_savings : 사기 위해 모은 돈 0부터 시작
# r : savings의 이자(?)금, 연간 기준임, 0.04로 고정
# annual_salary : 연봉
# portion_saved : 계약금을 위해 투자할 월급 비율. 10% == 0.10 식으로 입력
# monthly salary : 일정비율이 saving됨, 현재 투자금도 투자이익으로 조금 증가

# input 은 초기 연봉(annual_salary), 수익에서 투자할 비용(portion_saved), 집가격(total_cost)

def return_float(str) :
    str = str[1:]
    length = len(str)
    integer = int(str)
    return integer / (10**length)


annual_salary = int(input("Enter your annual salary "))

portion_saved = input("Enter the percent of your salary to save, as a decimal ")
portion_saved = return_float(portion_saved)

total_cost = int(input("Enter the cost of your dream home "))

portion_down_payment = 0.25
current_saving = 0
r = 0.04
monthly_salary = 0

month = 0
monthly_r = r/12
monthly_salary = annual_salary/12

cost_to_pay = total_cost * portion_down_payment
while current_saving < cost_to_pay :
    monthly_save = monthly_salary * portion_saved
    current_saving *= (1 + monthly_r)
    current_saving += monthly_save

    month += 1

print("Number of months", month)