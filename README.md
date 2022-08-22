<<<<<<< HEAD
因采购人员操作不当，购置的服务器带宽仅1Mbps，导致部分功能卡顿，还请谅解，下次一定。
- 本项目基于Nonebot2跨平台 PYTHON 异步机器人框架开发，前端是[go-cqhttp](https://link.zhihu.com/?target=https%3A//docs.go-cqhttp.org/)，后端是[NoneBot2](https://link.zhihu.com/?target=https%3A//v2.nonebot.dev/)
- 本项目配置命令起始字符为** "!"  or  "/"**
- 在群聊环境中使用需手动@机器人

# 功能01 复读
- **新建bot自带的基础功能**

## 使用
- **!echo 想让机器人复读的话 **
- **/echo 想让机器人复读的话**

## 维护
- **无**



# 功能02 基于和风天气api的天气查询
## 使用
- 天气+地区 或 地区+天气
- **例：无锡天气天气历城区**

## 维护
#.env
QWEATHER_APIKEY = xxx #和风天气申请api
QWEATHER_APITYPE = #api类型 0 = 普通版(3天天气预报) 1 = 个人开发版(7天天气预报) 2 = 商业版 (7天天气预报)
- 
- 



# 功能03 疫情信息查询
## 使用
### **查询地方疫情信息**（风险等级 新增 目前确诊）
指令: 城市名 + 疫情
事例: 天津疫情
### **查询地方出入政策**
指令: 城市名 + 疫情政策
事例: 广州疫情政策
### **查询城市风险地区**
- **只限查询大陆地级市或直辖市**

指令: 城市名 + 风险地区
### **疫情信息更新推送**
指令: 关注疫情 + 城市名
事例: 关注疫情 北京
### **取消推送**
指令: 取消疫情 + 城市名 / 取消关注疫情 + 城市名 / 取消推送疫情 + 城市名
## 维护
- **无**



# 功能04 emoji合成
- **将两个emoji合成一个，不会有人不知道什么是emoji吧**

## 使用
![](d3ceaf1e-bf64-4a6a-82e6-dfac092ee1ba)
## 维护
- **API = "https://www.gstatic.com/android/keyboard/emojikitchen/"**



# 功能05 随机猫猫图**【卡顿严重】**
- **谁不喜欢猫猫呢？**
- **有隐藏功能**

## 使用
- **!来个猫猫**
- **/来个猫猫**

## 维护
- **无**



# 功能06 R6S战绩查询
## 使用




**指令**
**别名**
**可接受参数**
**功能**
r6s
彩六，彩虹六号，r6，R6
昵称
查询玩家基本信息
r6spro
r6pro，R6pro
昵称
查询玩家进阶信息
r6sops
r6ops，R6ops
昵称
查询玩家干员信息
r6sp
r6p，R6p
昵称
查询玩家近期对战信息
r6sset
r6set，R6set
昵称
设置玩家昵称，设置后其余指令可以不带昵称即查询已设置昵称信息
- **需要加上命令起始字符"!" 或 "/"**
- **示例 !r6s GC_TIME_MASTER**

## 维护
- **无**



# 功能07 网易云无损下载**【卡顿非常严重】**
- **默认下载最高音质的音乐**
- **仅限群聊使用**
- **链接/卡片/卡片转发均已支持**

## 使用
**​**

**命令**
**备注**
/ncm
获取命令菜单
/ncm t
开启解析
/ncm f
关闭解析
- **默认不开启解析，需超级管理员在群里手动开启或者添加群聊白名单**
- **示例**

![](8e1b2f5f-cf5f-472b-a1eb-782103eeee5c)
## 维护
#.env
ncm_admin=["owner", "admin"] # 设置命令权限（非解析下载，仅解析功能开关设置）
ncm_phone= #手机登录
ncm_password= #密码
ncm_song=True  # 单曲解析开关
ncm_list=True  # 歌单解析开关
ncm_priority=2  # 解析优先级(ncm插件解析的优先级,1最高)
white_list=[]  # 白名单一键导入
- **建议priority设置高一些**



# 功能08 服务器状态查看
- **仅限超级管理员使用**

## 使用
- **向机器人发送戳一戳表情**
- **双击机器人头像戳一戳**

## 维护
#.env.dev
SUPERUSERS=["your qq id"]
###############################
server_status_only_superusers=True #是否仅允许超级用户使用
server_status_cpu=True #是否显示 CPU 占用百分比
server_status_per_cpu=True #是否显示每个 CPU 核心占用百分比
server_status_memory=True #是否显示 Memory 占用百分比
server_status_disk=True #是否显示磁盘占用百分比


# 功能09 力扣刷题提醒
- **不要内卷啊（哭腔**

## 使用
- **每天自动提醒无需操作**

## 维护
#.env
LEETCODE_QQ_FRIENDS=[948125001,123456]
LEETCODE_QQ_GROUPS=[238112475]

LEETCODE_INFORM_TIME=[{"HOUR":19,"MINUTE":33},{"HOUR":19,"MINUTE":34},{"HOUR":19,"MINUTE":35}]
- **时间不能以0开头，可以存在个位数**



# 功能10 60s读世界
- **世界那么大，我只想宅着**

## 使用
- **每天自动提醒无需操作**

## 维护
#.env
read_qq_friends=[3143799170] #设定要发送的QQ好友
read_qq_groups=[308304552,1021079474,1147623997,159795677,615871431] #设定要发送的群
read_inform_time=[{"HOUR":9,"MINUTE":1}] #在输入时间的时候 不要 以0开头如{"HOUR":06,"MINUTE":08}是错误的


# 功能11 定时提醒任务
- **需自己编写**

## 使用
- **每天自动提醒无需操作**

## 维护



# 功能12 每日群聊总结
- 仍旧待部署
- 阿巴阿巴



# 功能13 简易群管
- **踢 改 禁.......**
- **不太靠谱的违规图片自动检测**

## 使用
【初始化】：
  群管初始化 ：初始化插件

【群管】：
权限：permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER
  禁言:
    禁 @某人 时间（s）[1,2591999]
    禁 @某人 缺省时间则随机
    禁 @某人 0 可解禁
    解 @某人
  全群禁言（好像没用？）
    /all 
    /all 解
  改名片
    改 @某人 名片
  改头衔
    头衔 @某人 头衔
    删头衔
  踢出：
    踢 @某人
  踢出并拉黑：
   黑 @某人
   
【管理员】permission=SUPERUSER | GROUP_OWNER
  管理员+ @xxx 设置某人为管理员
  管理员- @xxx 取消某人管理员
  
【加群自动审批】：
群内发送 permission=GROUP_ADMIN | GROUP_OWNER | SUPERUSER
  查看词条 ： 查看本群审批词条   或/审批
  词条+ [词条] ：增加审批词条 或/审批+
  词条- [词条] ：删除审批词条 或/审批-

【superuser】：
  所有词条 ：  查看所有审批词条   或/su审批
  指定词条+ [群号] [词条] ：增加指定群审批词条 或/su审批+
  指定词条- [群号] [词条] ：删除指定群审批词条 或/su审批-
  自动审批处理结果将发送给superuser

【分群管理员设置】*分管：可以接受加群处理结果消息的用户
群内发送 permission=GROUP_ADMIN | GROUP_OWNER | SUPERUSER
  分管+ [user] ：user可用@或qq 添加分群管理员
  分管- [user] ：删除分群管理员
  查看分管 ：查看本群分群管理员

群内或私聊 permission=SUPERUSER
  所有分管 ：查看所有分群管理员
  群管接收 ：打开或关闭超管消息接收（关闭则审批结果不会发送给superusers）
  
【群词云统计】
该功能所用库 wordcloud 未写入依赖，请自行安装
群内发送：
  记录本群 ： 开始统计聊天记录 permission=GROUP_ADMIN | GROUP_OWNER | SUPERUSER
  停止记录本群 ：停止统计聊天记录
  群词云 ： 发送词云图片
  
【被动识别】
涩图检测：将禁言随机时间

违禁词检测：已支持正则表达式，可定义触发违禁词操作(默认为禁言+撤回)
定义操作方法：用制表符分隔，左边为触发条件，右边为操作定义($禁言、$撤回)
群内发送：
  简单违禁词 ：简单级别过滤
  严格违禁词 ：严格级别过滤(不建议)
  更新违禁词库 ：手动更新词库
    违禁词库每周一自动更新
    
【功能开关】
群内发送：
  开关xx : 对某功能进行开/关  permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER
  开关状态 ： 查看各功能的状态
  xx in ：
    ['管理', '踢', '禁', '改', '基础群管']  #基础功能 踢、禁、改、管理员+-
    ['加群', '审批', '加群审批', '自动审批'] #加群审批
    ['词云', '群词云', 'wordcloud'] #群词云
    ['违禁词', '违禁词检测'] #违禁词检测
    ['图片检测', '图片鉴黄', '涩图检测', '色图检测'] #图片检测
所有功能默认开

## 维护
- **鉴黄配置：**

腾讯云图片安全，开通地址：[https://console.cloud.tencent.com/cms](https://console.cloud.tencent.com/cms)
文档：[https://cloud.tencent.com/document/product/1125](https://cloud.tencent.com/document/product/1125) 注意，在beta2中，若不进行预先配置，启动时会无法导入，请安下方格式配置，若暂时不使用此功能，可以直接复制粘贴下面的内容 **.env.***:
# 腾讯云图片安全api
tenid="xxxxxx"
tenkeys="xxxxxx"


# 功能14 代码在线运行
- **支持-i参数输入**
- **运行于https://glot.io/**

## 使用
code [语言] [-i] [inputText]
[代码]

-i：可选 输入 后跟输入内容

运行代码示例(python)(无输入)：
    code py
        print("Hello world!")
运行代码示例(python)(有输入)：
    code py -i 你好
        print(input())
![](f5074cb9-c703-4581-ad1a-45c35bc7f259)
## 维护
- **无**



# 功能15 群聊反闪照
- **由于该功能过于危险，需指定特定群聊启用反闪照功能。**

## 使用
- **无需指令**

## 维护
#.env
ANTI_FLASH_ON=true                          # 开启或关闭
ANTI_FLASH_GROUP=["123456789", "987654321"] # 指定群聊
=======
# QQ_BOT
本项目基于Nonebot2跨平台 PYTHON 异步机器人框架开发，含开发手册。
>>>>>>> 3b30c21d75efae1f9dbe9bc77e3d63c6af03ba4b
