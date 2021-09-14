hours = str(input('How many hours did you work?'))
rate = float(input('Input the rate:'))
hrs = float(hours)
if hrs <= 40:
    pay = (hrs) * (rate)
    print(pay)
else:
    half_hours = (rate / 2) + rate
    hlf_hrs = float(half_hours)
    extra_pay = (hrs - 40)
    pay = (40 * rate) + (extra_pay * half_hours) 
    print(f'your pay: {pay}')