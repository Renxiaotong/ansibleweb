#template 用以存放静态网页

#ansi_cfg 中存放ansible配置与ansible主机清单可执行程序

#static 中存放html网页所需静态资源

#apis 是后端应用接口文件夹

#myansible 中存放系统配置可在里面修改数据库的配置


#Before you start, make sure you have installed mysqld and ansible controls.

#Open setting File, modify the link of the database and ensure that it is linked to your database.


#Execute
#python manager. py runserver 0:80
#The port number can be arbitrary



#Finally, remember to execute Update database data
#python manager. py makemigrations && python manager. py migrate
