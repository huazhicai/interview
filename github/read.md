### python requests模拟登陆github

需求：模拟登陆github,登陆后才能看到动态和简介绍

- **思路**
    - 通过Chrome Devtool可以看到github登录的URL是：https://github.com/session，方法是POST, 使用邮箱进行登录。
    - 既然是post提交表单数据，那么我们就要看Form Data数据， 庆幸可以看到是明文数据。
    - 分析表单数据，可以看到有个authenticity_token， 认证码。
    - 可以从登陆页面（https://github.com/login）获取此值。写个函数从登陆页面获取此值
    - 使用session登陆，可以保持登陆会话 session=requests.Session(), session.post(url,data=data)
    - 登陆后的操作，写函数，在login()  里执行就可以了