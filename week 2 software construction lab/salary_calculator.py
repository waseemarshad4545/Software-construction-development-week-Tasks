# ==========================================
# Task 2: Employee Salary Calculator
# Principles Applied: Single Responsibility Principle (SRP)
# ==========================================

# 1. Calculates Gross Salary (Basic Salary + Allowance)
def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


# 2. Calculates Tax Amount based on Tax Rate percentage
def calculate_tax(gross_salary, tax_rate):
    return gross_salary * (tax_rate / 100)


# 3. Calculates Net Salary (Gross Salary - Tax)
def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax


# Presentation Function: Displays Payslip
def generate_payslip(emp_name, basic_salary, allowance, tax_rate):
    gross_salary = calculate_gross_salary(basic_salary, allowance)
    tax = calculate_tax(gross_salary, tax_rate)
    net_salary = calculate_net_salary(gross_salary, tax)

    print("\n" + "-" * 35)
    print(f"        EMPLOYEE PAYSLIP        ")
    print("-" * 35)
    print(f" Employee Name : {emp_name}")
    print(f" Basic Salary  : ${basic_salary:,.2f}")
    print(f" Allowance     : ${allowance:,.2f}")
    print(f" Gross Salary  : ${gross_salary:,.2f}")
    print(f" Tax ({tax_rate}%)   : ${tax:,.2f}")
    print(f" Net Salary    : ${net_salary:,.2f}")
    print("-" * 35 + "\n")


# Execution Entry Point
if __name__ == "__main__":
    employee_name = "Muhammad Ali"
    basic = 5000.00
    allowance_amount = 1200.00
    current_tax_rate = 10.0  # 10%

    generate_payslip(
        emp_name=employee_name,
        basic_salary=basic,
        allowance=allowance_amount,
        tax_rate=current_tax_rate,
    )