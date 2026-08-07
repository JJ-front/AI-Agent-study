"""
实现一个函数 create_account(initial_balance)，返回两个函数：

deposit(amount): 存款，返回新余额
withdraw(amount): 取款，余额不足返回 "余额不足"，否则返回新余额
要求使用闭包保存余额状态，不要暴露余额变量。
"""
def create_account(initial_balance):
    result_balance = initial_balance
    def deposite(amount):
        nonlocal result_balance
        result_balance += amount
        result = result_balance
        return result
    def withdraw(amount):
        nonlocal result_balance
        if amount > result_balance:
            return '余额不足'
        else:
            result_balance -= amount
            result = result_balance
            return result
    return deposite, withdraw


deposit, withdraw = create_account(100)
print(deposit(50))    # 150
print(withdraw(30))   # 120
print(withdraw(200))  # 余额不足