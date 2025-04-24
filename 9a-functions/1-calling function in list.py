def fun():
    print("fun()")
def disp():
    print("disp()")
def msg():
    print("msg()")

function_list = [fun, disp, msg]

for func in function_list:
    func()  
