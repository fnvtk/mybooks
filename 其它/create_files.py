#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 目录结构
structure = [
    # PART 1
    {
        "folder": "PART1",
        "title": "PART 1：我少年时期的互联网启蒙 (1998-2005年)",
        "chapters": [
            {"id": "1.1", "title": "有希望的人生会有阳光"},
            {"id": "1.2", "title": "我的第一台电脑"},
            {"id": "1.3", "title": "网吧里的巨大诱惑"},
            {"id": "1.5", "title": "沉迷网游后的创业萌芽：第一次做虚拟物品交易"},
            {"id": "1.6", "title": "学校里的互联网小王子：用技术赚取第一桶金"},
            {"id": "1.7", "title": "E123.COM域名为什么能卖1万美金：圈子的重要性"},
            {"id": "1.8", "title": "暑假社会体验后的重要决定：选择改变命运的轨迹"},
            {"id": "1.9", "title": "新环境的\"化学反应\"：人脉资源的意外链接"},
            {"id": "1.10", "title": "我骨子里就不是个纯粹的商人，就是想搞点事情"},
            {"id": "1.11", "title": "脑子里开始冒出各种不靠谱的创业点子"},
        ]
    },
    # PART 2
    {
        "folder": "PART2",
        "title": "PART 2：从0-1的过程 (2005-2016年)",
        "chapters": [
            {"id": "2.1", "title": "建成第一个网站：从0到1的探索之路", "note": "开网吧的日子"},
            {"id": "2.2", "title": "用28K收了2万元开始：网吧的一次经历"},
            {"id": "2.3", "title": "钻研SEO推广网站：流量为王的时代", "note": "电影服务器100万的投资"},
            {"id": "2.4", "title": "打游戏真的能赚钱吗？游戏知识付费", "note": "2008"},
            {"id": "2.5", "title": "别以为自己做的东西很牛，该卖就卖：创业路上的选择与放弃"},
            {"id": "2.6", "title": "彻底撕掉蓝图，追求落地盈利：务实的创业哲学"},
            {"id": "2.7", "title": "第一个盈利模型的建立：找到通往成功的钥匙"},
            {"id": "2.8", "title": "我是隐形冠军：深耕细分领域"},
            {"id": "2.9", "title": "为什么Hao123能卖5000万，我却只能卖400块：商业模式的差距"},
            {"id": "2.10", "title": "我的推广策略：流量为王，内容为皇"},
            {"id": "2.11", "title": "第一个一百万的意义：财富自由的起点"},
            {"id": "2.12", "title": "对钱的态度必须如履薄冰：谨慎与胆识的平衡"},
            {"id": "2.13", "title": "第一桶金后坚决不做的投资：坚守原则，不忘初心"},
            {"id": "2.14", "title": "资产倍增的投资：比特币", "note": "2013"},
            {"id": "2.15", "title": "资产倍增的投资：圈子"},
            {"id": "2.16", "title": "资产倍增的投资：自己"},
            {"id": "2.17", "title": "我抓住的机会（上）：把握机遇"},
            {"id": "2.18", "title": "我抓住的机会（下）：抓住机遇，乘势而上", "note": "倒卖金币"},
            {"id": "2.19", "title": "讨厌的羊毛党：淘宝80%利润被仅退款", "note": "2014年"},
            {"id": "2.20", "title": "我解决焦虎的方法：冥想"},
            {"id": "2.21", "title": "我的第一个量化交易系统：上帝之眼"},
            {"id": "2.22", "title": "和行业大佬的下午茶：受益终生的交流", "note": "2015"},
            {"id": "2.23", "title": "游戏行业的最后一个项目（上）：为梦想画上圆满句号"},
            {"id": "2.24", "title": "游戏行业的最后一个项目（下）：青春不散场"},
        ]
    },
    # PART 3
    {
        "folder": "PART3",
        "title": "PART 3：我的创业旅程 (2016-2020年)",
        "chapters": [
            {"id": "3.1", "title": "说干就干的新旅程：淘宝店"},
            {"id": "3.2", "title": "刚到厦门后的选择：在迷茫中寻找方向"},
            {"id": "3.3", "title": "在职场快速进步的日子：不断学习，提升自我"},
            {"id": "3.4", "title": "互联网创业最火的时候到了：站在时代的风口浪尖"},
            {"id": "3.5", "title": "发现淘宝流量密码：浏览量和刷单"},
            {"id": "3.6", "title": "狗被偷了：事件和标签是引流方式"},
            {"id": "3.7", "title": "在微信上赚了很多很多钱：私域流量的爆发"},
            {"id": "3.8", "title": "为自己的性格买单：公司倒闭"},
            {"id": "3.9", "title": "破产之后旅程路上的思考：不忘初心，砥砺前行"},
            {"id": "3.10", "title": "做一家天塌下来都赚钱的公司（一）：打造企业的护城河"},
            {"id": "3.11", "title": "做一家天塌下来都赚钱的公司（二）：构建可持续发展的商业模式"},
        ]
    },
    # PART 4
    {
        "folder": "PART4",
        "title": "PART 4：正在做的事情 (2020-至今)",
        "chapters": [
            {"id": "4.1", "title": "私域是互联网地产：构建私域流量池"},
            {"id": "4.2", "title": "影响力是未来货币：打造个人品牌"},
            {"id": "4.3", "title": "团队背叛后的反思"},
            {"id": "4.4", "title": "写作即编程：用文字构建思想体系"},
            {"id": "4.5", "title": "我在私域领域的布局：构建账号矩阵", "note": "碎片时间"},
            {"id": "4.6", "title": "警惕黑产：比黑客更黑的人"},
            {"id": "4.7", "title": "加速原始积累，步入私域基础设施建设"},
            {"id": "4.8", "title": "卡若私董会，是诈骗集团吗？"},
        ]
    },
    # PART 5
    {
        "folder": "PART5",
        "title": "PART 5：未来的一些思考",
        "chapters": [
            {"id": "5.1", "title": "超级个体"},
            {"id": "5.2", "title": "超级企业"},
        ]
    },
]

# 创建总目录文件
with open("目录.md", "w", encoding="utf-8") as f:
    f.write("# 《卡若的IP财富旅程》\n\n")
    
    for part in structure:
        f.write(f"## {part['title']}\n\n")
        
        for chapter in part["chapters"]:
            note = f" - {chapter.get('note')}" if 'note' in chapter else ""
            f.write(f"- [{chapter['id']} {chapter['title']}]({part['folder']}/{chapter['id']}.md){note}\n")
        
        f.write("\n")

# 创建每个章节的文件
for part in structure:
    # 确保文件夹存在
    os.makedirs(part["folder"], exist_ok=True)
    
    # 为每个部分创建一个介绍文件
    with open(f"{part['folder']}/README.md", "w", encoding="utf-8") as f:
        f.write(f"# {part['title']}\n\n")
        f.write("## 本部分章节\n\n")
        
        for chapter in part["chapters"]:
            note = f" - {chapter.get('note')}" if 'note' in chapter else ""
            f.write(f"- [{chapter['id']} {chapter['title']}]({chapter['id']}.md){note}\n")
    
    # 为每个章节创建文件
    for chapter in part["chapters"]:
        with open(f"{part['folder']}/{chapter['id']}.md", "w", encoding="utf-8") as f:
            f.write(f"# {chapter['id']} {chapter['title']}\n\n")
            if 'note' in chapter:
                f.write(f"*{chapter['note']}*\n\n")
            f.write("<!-- 在此处填写章节内容 -->\n\n")
            f.write("## 内容概要\n\n")
            f.write("## 正文\n\n")
            f.write("## 关键收获\n\n")
            f.write("## 行动指南\n\n")

print("所有文件已创建完成！") 