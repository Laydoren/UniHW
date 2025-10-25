data = {input(f"Name of company №{i+1}: "): list(map(float, input(f"Enter planned and real voluem with space: ").split())) for i in range(int(input("Num of companies: ")))}
bad_res = []
print()

for name, stats in data.items():
    plan, real = stats
    percentage = (real / plan) * 100
    if percentage < 90:
        bad_res.append(name)

    print(f"Company: {name}")
    print(f"Plan: {plan}")
    print(f"Real: {real}")
    print(f"Implementation of the plan: {percentage:.2f}%")
    print()

if bad_res:
    print("List of companies underperforming the plan by 10% or more:")
    for name in bad_res:
        print(f"- {name}")