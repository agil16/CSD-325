#Arely Gil
#Assignment 2.2

def calculate_years_to_double(initial_investment, annual_interest_rate):
  years = 0
  current_amount = initial_investment
  target_amount = initial_investment * 2

  while current_amount < target_amount:
      current_amount += current_amount * (annual_interest_rate / 100)
      years += 1

  return years

annual_interest_rate = int(input("Please enter interest rate. Note: Only enter the rate as a whole number. Example: If rate is 2% only enter 2: "))
initial_investment = float (input("Now enter your initial investment. Note please only enter the initial investment as a whole number. Example: If the initial investment is $10,000 only enter 10000: ")) 


years_to_double = calculate_years_to_double(initial_investment, annual_interest_rate)

print(f"It will take {years_to_double} year(s) for the investment to double.")