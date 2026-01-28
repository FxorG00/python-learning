def outer(account_amount=0) :
    def inner(num,deposit=True) :
        nonlocal account_amount
        if deposit :
            account_amount+=num
            print(f'存款：+{num}，目前余额为 {account_amount}')
        else :
            account_amount-=num
            print(f'取款：-{num}，目前余额为 {account_amount}')
    return inner
atm=outer()
atm(10)
atm(20,True)
atm(25,False)
