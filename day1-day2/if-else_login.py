import getpass

usename=input('请输入用户名：')
password=input('请输入密码：')

if usename=='admin'and password=='123456':
    print('登陆成功')
else:
    print('登陆失败')

