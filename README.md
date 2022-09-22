# kotti_ai
结合Pyramid Kotti web框架和AI serving框架，通过构建kotti_ai软件项目，打通AI部署最后一公里！

kotti_ai是AI+互联网企业级应用软件包，通过web技术，将基于飞桨Paddle Serving框架和 MindSpore Serving的AI应用更好的呈现出来，解决AI实际部署落地难、AI技术提供商与最终用户互通难的问题，实现AI部署、落地、上线以及推广一条龙解决方案！

当前飞桨Paddle Serving框架部分已经调通， MindSpore Hub 部分已调通，MindSpore Serving 还没测试。

## kotti_ai的特点：
易部署

易上线

易使用

## 构建企业级AI+互联网应用的功能分解
企业级级AI+互联网应用服务由三部分组成，其中前两部分业内有成熟解决方案，即部署和web服务，增加的工作是通过第三部分 kotti_ai软件包，将前两部分联通在一起，组成整体解决方案。

### 1、飞桨Paddle Serving企业级部署
Paddle Serving 依托深度学习框架 PaddlePaddle 旨在帮助深度学习开发者和企业提供高性能、灵活易用的工业级在线推理服务。Paddle Serving 支持 RESTful、gRPC、bRPC 等多种协议，提供多种异构硬件和多种操作系统环境下推理解决方案，和多种经典预训练模型示例。 https://github.com/PaddlePaddle/Serving/

### 2 MindSpore Serving企业级部署
MindSpore Serving是一个轻量级、高性能的服务模块，旨在帮助MindSpore开发者在生产环境中高效部署在线推理服务。支持gRPC和RESTful接口。https://gitee.com/mindspore/serving

### 3、企业级WEB服务
采用Pyramid和Kotti提供企业级web服务。

Pyramid 是基于Python的企业级web框架，Kotti是基于Pyramid的企业级CMS web框架。

Pyramid：The Start Small, Finish Big Stay Finished Framework https://www.trypyramid.com/

Kotti is a high-level, Pythonic web application framework based on Pyramid and SQLAlchemy. It includes an extensible Content Management System called the Kotti CMS (see below). https://github.com/Kotti/Kotti

### 4、kotti_ai 企业级AI+互联网应用组件
kotti_ai是本项目的主角，刚刚面市不久，还在功能完善中...https://git.openi.org.cn/skywalk163/kotti_ai

kotti_ai基于Kotti框架，将飞桨Paddle Serving提供的推理服务，使用web技术呈现给最终用户。

我们这样简单理解：

飞桨Paddle Serving提供企业级推理服务，但不提供终端用户界面。
PaddleHub提供推理服务，提供终端用户界面，但只适合个人用户使用，无法提供企业级服务。
kotti_ai既有终端用户界面，又通过飞桨Paddle Serving提供企业级推理服务。

MindSpore Serving提供企业级推理服务，但不提供终端用户界面。不支持CPU
MindHub提供推理服务，无法提供企业级服务。支持CPU
MindSpore Lite 支持的硬件种类多，支持安卓和CPU，但CPU下示例较少。需要一定的C语言基础。
kotti_ai目标是通过Serving提供企业级推理服务，有良好的终端用户界面。目前看需要昇腾芯片硬件的支持。

# 项目展示
本项目以pp-shitu模型为例，已经在移动云测试主机：http://ww3.airoot.org:6543/ 进行部署展示，预计展示时间到2022.11月停止。 在此感谢移动云苏州区的大力支持！

大家可以点击上面的网址，使用账户admin密码qwerty登录。登录之后可以选择菜单：add-AImage上传图片，图片上传后就会进行分类识别，打印出类似这样的识别结果：[{'bbox': [345, 95, 524, 585], 'rec_docs': '红牛-强化型', 'rec_scores': 0.8073724}]

MindSpoe的展示在http://ww3.airoot.org:8765/ ，同样使用账户admin密码qwerty登录。
可以看到每个图片都识别出一个分类号码。

# AI+互联网应用项目实践
以下步骤仅为参考展示，因为Paddle Serving本身安装就会碰到很多坑，尤其是在AIStudio下一般不会太顺利，更要命的是c++ serving更加困难（我都忘记自己是否安装成功过了）。 索性Paddle Serving是服务器版，不需要安装很多遍，另外其负载能力强大，值得我们花费的时间。

安装并启动Paddle Serving c++之后，就可以安装kotti_ai了。kotti_ai源代码写死了会跟本机9400端口通信，所以不启动c++ serving 是无法正常启动kotti_ai的。

## 1、安装飞桨Paddle Serving
安装Paddle Serving c++服务器，服务端口号是9400

具体请参照官方文档：https://github.com/PaddlePaddle/PaddleClas/blob/release/2.5/docs/zh_CN/inference_deployment/recognition_serving_deploy.md

## 2、安装Kotti软件包
直接使用pip安装即可。Kotti包含了PYramid web框架的软件包。


pip install kotti
## 3、安装kotti_ai
首先需要下载kotti_ai源代码，然后需要安装相关库，安装相关库需要较长时间。

大家直接在kotti_ai目录可以查阅源代码，也欢迎志同道合的朋友一起来建设这个项目。

```
# 下载kotti_ai源代码
%cd ~/
!git clone https://git.openi.org.cn/skywalk163/kotti_ai

# 安装kotti_ai
!pip install kotti_image kotti_tinymce pyramid_debugtoolbar plone
!cd ~/kotti_ai && python setup.py develop 
```
如果是在控制台，需要把前面的% 和 ！ 去掉！

## 4、启动web服务
kotti_ai是基于Kotti框架，Kotti基于Pyramid框架，但是使用起来并不会感到层级关系，直接在kotti_ai目录启动web服务即可。

在控制台进入kotti_ai目录，执行pserve developmnet.ini --reload

kotti_ai需要本地启动Paddle Serving c++服务，也就是需要启动9400端口才行。所以目前我们在AIStudio下无法正常运行。

ps：大家也可以学习下Kotti和Pyramid框架，他们都相当优秀。

## 5、浏览器测试
打开浏览器，默认是5000端口 http://127.0.0.1:5000


项目安装流程在AIStudio有展示，见链接：https://aistudio.baidu.com/aistudio/projectdetail/252773

# AI+互联网应用项目实践 MindSpore框架
## 部署，安装MindSpore Serving
需要昇腾平台。

如果是cpu，可以使用MindSpore Lite或者MindSpore Hub部署

## kotti_ai代码等待合入中
现在的问题是：如何加入一个变量标志，让kotti_ai软件包能自动识别飞桨还是MindSpore环境，这样就不需要用户再手工修改代码了。

基本思路是使用pkg_resources包来判断在哪个环境。也可以加上一个标志变量AIclass
```
>>> import pkg_resources as pr
>>> pr.get_distribution("paddlepaddle")
paddlepaddle 2.3.2 (/home/pyramid/py39/lib/python3.9/site-packages)
```
把所有两个框架的代码都独立出来，以便灵活切换。 
记得有个框架可以调用飞桨和MindSpore等，可以参考下。
