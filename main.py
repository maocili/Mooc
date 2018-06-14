import  Login
# acc = input('输入用户名密码，以空格区分'+'\n').split()
# head =  Login.requests_interface.login(acc[0],acc[1])
# Login.requests_interface.start('xxdgaeiojkdp4a39rqtp1q')
# Begin.begin_interface.get_allId()

with open('F:\\1.txt')as f:
    for i in f:
        acc = i.split()
        print(i)
        head =  Login.requests_interface.login(acc[0],acc[1])
        Login.requests_interface.start('xxdgaeiojkdp4a39rqtp1q')

f.close()
