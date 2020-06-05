# flask demo
<br />

<pre>
# flask项目结构参考如下（flask核心开发者推荐）：
https://lepture.com/en/2018/structure-of-a-flask-project
</pre>

<pre>
# 这个命令会在当前目录下生成一个migrations文件夹。一般只用在项目初始化的时候执行一次
$ flask db init

# 此命令会在migrations下生成一个version文件夹，下面包含了对应版本的数据库操作py脚本。每次变更models，都需要执行
$ flask db migrate

# 此命令相当于执行了version文件夹下的相应py版本，对数据库进行变更操作。每次变更models，都需要执行
$ flask db upgrade
</pre>




<pre>
# 生成requirements.txt文件
$ pip freeze > requirements.txt
</pre>
