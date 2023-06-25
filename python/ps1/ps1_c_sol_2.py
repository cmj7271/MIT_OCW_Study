# 이번엔 3년안에 달성하기 위한 saving 비율을 구하자
# semi_annual_raise == .07, 투자이익 (r) == 0.04
# 계약금은 0.25, 집 비용은 백만달러(1,000,000)
# 100달러 이내 오차 허용
# 이분탐색 사용, b의 코드 재사용 및 탐색 횟수도 출력해야함
# 정확도는 소수 셋째자리까지 --> 0 부터 10000 사이로 찾기 (정수 나누기 활용해서)
# 3년안에 안된다면 안된다고 출력해주어야 함.

# b번을 활용하되, saving_rates 를 0 ~ 10000 으로 표현
# 일단 10000 --> 5000 --> 2500 --> ...
# 탈출 조건은 내야할 돈과 오차가 100 안 일때
# 혹은 처음 10000 으로 해도 부족할 때.

def get_total_saving(cost_to_pay, monthly_salary, portion_saved, monthly_r, semi_annual_raise) :
    current_saving = 0
    month = 0
    while current_saving - cost_to_pay < -100 and month <= 36 :
        monthly_save = monthly_salary * portion_saved
        current_saving *= (1 + monthly_r)
        current_saving += monthly_save
    
        month += 1
        if month % 6 == 0 :
            monthly_salary *= (1 + semi_annual_raise)
    
    return current_saving

# 변수 너무 많은 것에 대해 class 로 처리 가능함을 언급해도 상관없을 듯.

annual_salary = int(input("Enter your annual salary "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
monthly_salary = 0
monthly_r = r/12
monthly_salary = annual_salary/12

portion_saved_max = 10000
portion_saved_min = 0
portion_saved = 10000

cost_to_pay = total_cost * portion_down_payment
cnt = 0

total_saving = get_total_saving(cost_to_pay, monthly_salary, portion_saved / 10000, monthly_r, semi_annual_raise)

if cost_to_pay - total_saving > 100 :
    print("It is not possible to pay the down payment in three years.")

else :
    portion_saved = 5000
    while total_saving - cost_to_pay >= 100 or total_saving - cost_to_pay <= -100 :
        portion = portion_saved / 10000
        total_saving = get_total_saving(cost_to_pay, monthly_salary, portion, monthly_r, semi_annual_raise)
        cnt += 1

        if total_saving - cost_to_pay > 100 :
            portion_saved_max = portion_saved
        #elif total_saving - cost_to_pay < -100 :
        else :
            portion_saved_min = portion_saved

        portion_saved = (portion_saved_max + portion_saved_min) // 2

    best_saving_rates = portion_saved

    print(cnt, best_saving_rates/10000)