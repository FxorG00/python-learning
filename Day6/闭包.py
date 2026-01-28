def outer(logo) :
    def inner(msg) :
        nonlocal logo
        print(f"<{logo}>msg<{logo}>")
        logo='你好'
    return inner
outer('黑马程序员') # 单独 outer ，它并不会调用 inner 这个函数啊！只是返回 inner
fn1=outer('黑马程序员')
fn1('大家好')
fn1('晚上好')
fn2=outer('尚硅谷')
fn2('下午好')
fn1('早上好')