"""
Author: Pang Jin Jia
Last updated: 16 Jan 2021

this file gives you a quick overview of your total CPF contribution (employer + employee) based on age & monthly salary, 
and predict your basic retirement sum by the time you hit age of 55
"""

salary = float(input("Enter your gross salary: $"))
age = int(input("Enter your current age: "))

def calc_cpf(sal):
    if age <= 16:
        print("You are too young to work!")
        return
    elif sal <= 750:
        print("Your salary is too low for this calculator to compute!")
    elif age <= 35:
        OA = sal*0.23
        SA = sal*0.06
        MA = sal*0.08
    elif age <= 45:
        OA = sal*0.21
        SA = sal*0.07
        MA = sal*0.09
    elif age <= 50:
        OA = sal*0.19
        SA = sal*0.08
        MA = sal*0.1
    elif age <= 55:
        OA = sal*0.15
        SA = sal*0.115
        MA = sal*0.105
    elif age <= 60:
        OA = sal*0.12
        SA = sal*0.035
        MA = sal*0.105
    elif age <= 65:
        OA = sal*0.035
        SA = sal*0.025
        MA = sal*0.105
    else:
        OA = sal*0.01
        SA = sal*0.01
        MA = sal*0.105
    print(f"At your current age of {age}, your respective total employer + employee CPF contributions are:")
    print(f"Ordinary Account: ${OA:.2f}")
    print(f"Special Account: ${SA:.2f}")
    print(f"Medisave Account: ${MA:.2f}")
    
    retirementAge = 55
    x = retirementAge - age
    if x > 0:
        print(f"Your predicted Basic Retirement Sum needed is: ${x*3000+93000}")
    
calc_cpf(salary)
