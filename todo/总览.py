'''
一个简单 todo 程序项目, 包含的文件如下
    routes_todo.py 包含了项目的所有路由函数
        显示所有todo
        增加todo 
        更新todo 
        删除todo 
    todo.py
        包含了 Todo Model, 用于处理数据
    templates/todo_index.html
        显示所有 todo 的页面
    templates/todo_edit.html
        显示编辑 todo 的界面 

点击添加按钮增加一个新的 todo 的时候, 程序的流程如下(包含原始 HTTP 报文)
    1, 浏览器提交一个表单给服务器(发送 POST 请求)
POST /todo/add HTTP/1.1
Content-Type: application/x-www-form-urlencoded

title=heuv
    2, 服务器解析出表单的数据, 并且增加一条新数据, 并返回 302 响应
HTTP/1.1 302 REDIRECT
Location: /todo

    3, 浏览器根据 302 中的地址, 自动发送了一条新的 GET 请求
GET /todo HTTP/1.1
Host: ....

    4, 服务器给浏览器一个页面响应
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: ...

<html>
    ....
</html>
    5, 浏览器把新的页面显示出来

"""
