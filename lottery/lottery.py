# -*- coding: utf-8 -*-

import random

"""
var a = new Array();
$('.comment-nickname > span').each(function(i, e) { a.push(e.innerHTML); });
"""
wechat_raw = ["里德", "冶。", "Everlasting", "Mira", "Naruto", "nvidi", "abc", "00oo00", "VC", "kyle", "田宏增", "czh", "DC", "Ybb", "Ninja go go go", "华仔", "Tim℃hEn", "TotorO", "HaKu", "哈哈哈", "Michaeljian", "x.xu", "Hornheim", "彩云", "Daniel", "张糖糖", "星星大魔王", "王勃", "帅的很糟心", "八九", "Vic", "iota", "沐龙凯", "%-2l,,,+358", "zc⊙_⊙", "Ting", "💤", "呆", "LJH", "芹沢多摩雄", "Clylonglonglive", "哈欠兔🐰", ":(", "张梓晟😄", "恒律", "dyj", "Jason", "Brandon", "林喵喵", "婿锤", "lin涛", "亦峰", "DoMINE™", "宋恩浩", "Bigred", "加菲汪", "Fan", "否", "lllModerato", "韬(￣▽￣)", "friend.ma", "Kai", "『Sherry』", "刘伟", "高梦然🤙🏿", "SR", "正版乔", "搬铁少年ai", "chen", "pedestrian_fire", "菠萝吹雪。", "徐文志程序猿", "丘丘", "Legend king", "onion", "林雨辉", "林雨辉", "Tommy", "Sparrowhawk", "like", "张若", "林雨辉", "Eason", "tmc~", "子想和你曰", "奶罐儿", "Yue Liang", "Danielhua", "geekerzp", "－o－", "默小佳", "杨天奇", "JamesYu", "ct", "MENG", "yellowstar", "李赟", "Mcewan", "😈", "zkd.re", "哒啦哒啦biu～", "李春燕", "五好幼儿", "某风", "Claire倩", "仰天翻白眼", "Harold", "马靖昆", "咖喱酱🍛", "Mira", "郝越", "大恒", "w", "Yue", "陈金鑫", "棋儿也要革命", "镁镁", "rao", "冥王星", "0X17", "Nate", "好想", "Fan Liu", "WYao ®", "Anler"]
wechat_unique = set(wechat_raw)
print('wechat total entries = ', len(wechat_unique))
wechat = [name + "_wechat" for name in wechat_unique]


"""
Bilibili
var a = new Array();
$('.item-user > a').each(function(i, e) { a.push(e.innerHTML);});
$('.name ').each(function(i, e) { a.push(e.innerHTML);});
"""
bili_repost = ["天高skyhigh", "funcall", "Askr0Yggdrasils", "长久_如云", "raindropha", "追随风吧", "_nokki", "小花的后厨", "VivianVKJ", "lykzuishuaile", "Youking96", "schecterwcy", "TARI、WZJ", "imyangs", "Retr0_4u", "maotouAAA", "UpRiddler", "长景Rivulet", "女神sama", "源木_lin", "虾子百菇和风杂炊", "llxxee", "SoulJuly", "Dtxp", "给你我的丁丁", "Lee有所为", "guyao", "yaoleo", "精豆哥哥", "ThunderXz", "ThunderXz", "单倍熊", "krinmal", "小胡野", "萌萱萱萱", "萌萱萱萱", "秀才阿萨", "danielwan1994", "MSP430G2553", "34177908463_bili", "笑一笑从容", "对面的你", "爱心天使123", "bi站走一回", "-寒河江KUMO", "LOVE小狼", "星煌的鼓动", "年度大萌新", "Kul0l0", "机智英俊小狼君", "Raraday", "Kisro", "bigbaby520", "nocti薄暮", "今时一", "BiBo1233", "辛子大大", "改名带来好运气", "banlu_master", "不求上进的鱼仔", "china-star", "野生苹果子", "净亭境停静听晴", "90223022079_bili", "青衫挽袖丶", "FloweringTree", "Dalen", "唐朝少年", "houhp", "桜抄丶", "sk8lele", "易饭Y", "墨耕666", "StardustOvO", "丿Bigboss丶", "木子三石吼", "longlongshot", "战士与小丑", "拾小一", "毛毛maoooo", "叫兽___", "仙级圣纹师", "eLinX", "里里里里里昂_Hoo", "竹智熊猫", "Kuo_君", "FrouFrou55", "小老弟往后稍", "周家三少ye", "stevenash0822", "鬼柳妙墨", "细心网友张先生", "pxj真实嗷", "蓬子米的夏天", "你你你的益达", "整日摸鱼的小黑猫", "我就改个昵称", "宇宙高冷", "约翰-高尔特", "miaodi_", "915927694", "915927694", "人参弟弟", "DonnaChil", "lovetoninght", "梓临", "CCCCeliaL", "比企谷小黑", "tryer789", "Katniss611", "tryer789", "Ramsey16k", "漫漫追梦路", "二木林叫森", "哔哔哔哔观众", "晃晃悠悠Zzz", "dgd天师", "公元2022", "Lee513QaQ", "P1nder", "HFarchbishop", "jediyoda", "在稻田里操草人", "我不信这个名字也被占用了", "大湿人徐志摩", "懒癌晚期患者", "旺角卡门里", "のんの你的烧酒", "自闭的话痨Roy", "拂苍云", "保大保小", "40862249776_bili", "皮了卡了秋", "摇晃的红酒杯24", "Impressivebro258", "呆呆-硕", "jingfutian", "money89757", "沙拉野子酱", "Gakkis", "mylittleZ", "bili_40373300902", "zxpdaye", "历史塞车王", "萨瓦Z迪卡", "一条咸鱼MOONJOJO", "拉格朗波", "nobitaw", "丁乙_Dingyi", "花花的小玄子", "丁乙_Dingyi", "空空果", "stephenzane", "名字改回萌姐了", "乔可可123", "CatQvQ", "CatQvQ", "我是一株犀牛花", "一定能上岸鸭", "挖了蘑菇累死啊", "gin丶ever", "拉克丝的蓝朋友", "大寒御寒", "刀马Dinary", "哲学大叔", "哲学大叔", "Letitaaa", "今天我没有学习", "a524rgy84e6", "新晴天panda", "魂の歌", "水灵灵的小葱", "庄黑子", "乐乐妹"]
bili_reply = ["噎牙嘻", "我的尾巴去哪了", "龙龙是小孩儿", "bigbaby520", "funcall", "Youking96", "schecterwcy", "TARI、WZJ", "不哇哇", "nocti薄暮", "今时一", "Retr0_4u", "maotouAAA", "辛子大大", "改名带来好运气", "banlu_master", "不求上进的鱼仔", "女神sama", "源木_lin", "虾子百菇和风杂炊", "llxxee", "山鹰shine", "Lee有所为", "净亭境停静听晴", "ThunderXz", "90223022079_bili", "krinmal", "小胡野", "青衫挽袖丶", "萌萱萱萱", "秀才阿萨", "danielwan1994", "34177908463_bili", "对面的你", "houhp", "爱心天使123", "过分贪花色", "bi站走一回", "以有涯随无涯殆矣", "星煌的鼓动", "Kul0l0", "MelonP10", "机智英俊小狼君", "易饭Y", "此账号不能注册", "丿Bigboss丶", "瞌睡瞌睡猫", "longlongshot", "拾小一", "毛毛maoooo", "潇洒的型男", "叫兽___", "宫崎骏的龙猫", "蘑菇香锅炖鱼", "里里里里里昂_Hoo", "ddghjvvg", "jayusSAWYER", "凉宫秋夜的忧郁", "Arthur000", "hutos丶", "竹智熊猫", "小老弟往后稍", "stevenash0822", "机智的丶Ming", "bijili", "bijili", "细心网友张先生", "pxj真实嗷", "千绫月", "蓬子米的夏天", "整日摸鱼的小黑猫", "某网友", "宇宙高冷", "miaodi_", "915927694", "人参弟弟", "扫码阅读", "DonnaChil", "lovetoninght", "梓临", "风逝cherish", "长渔歌", "tryer789", "dgd天师", "哔哔哔哔观众", "dgd天师", "Lee513QaQ", "全子么么哒", "旺角卡门里", "保大保小", "taoup", "40862249776_bili", "皮了卡了秋", "谜之鱼素", "呆呆-硕", "rAlex_c", "謎謎謎", "Gakkis", "格林匹思", "mylittleZ", "zxpdaye", "丁乙_Dingyi", "丁乙_Dingyi", "花花的小玄子", "stephenzane", "空空果", "名字改回萌姐了", "庄子23333", "icbob", "CatQvQ", "挖了蘑菇累死啊", "一定能上岸鸭", "gin丶ever", "拉克丝的蓝朋友", "噗噗小鱼", "NMfairyland", "哲学大叔", "Letitaaa", "今天我没有学习", "a524rgy84e6", "zhupyter", "_拟把疏狂图一醉_", "魂の歌", "庄黑子", "乐乐妹"]
bili_unique = set(bili_repost + bili_reply)
print('bili total entries = ', len(bili_unique))
bili = [name + "_bili" for name in bili_unique]

"""
YouTube
Sublime + multiple cursor
"""
youtube_raw = ["CC CONG","yang mona","ellen park","Zhiqiang Sun","Sijie Ren","Kazuma Yagami","Tianchu Xie","John Watson","ellen park","Haochen Yang","Shunqi Wang","Jp Wan","jinjia zhang","Evan Wang","Enhao Song","Zhijian Xu","Shouyue Wu","Shiyu Liu","StoneTube","Kai Ni","Hu Oliver","Klory Han","Klory Han","Terry L","Tianqi Gao","Raymond Qin","PINCHAO LIU","罗一凡","Yue Kang","Zihao Li","Jinlong Ji","zi0n","yu yu","Sam Cui","Renjie Yu","Jianbin Wen","闫福城","Jingwei Yan","Hongli Wang","Zhi Li","heihei","Esther Wang","Han Song","James Bond","Evan Tian","苏脑","贺大","Ye Zhao","Alina Wei","Chang Liu","Zuo Wang","李坤樸","celestial sirius","Horward","Hao Liu","Xin Zhang","Sally","Yvonne L","Po-Cheng Pan","NISSAYE WU","rongxin Ni","Ben Chen","Yan Kang","Yingyi Song","Hero Qi","M&amp;M Anshi","Jason Swift","stoneageme","Tony Chen","Joseph Chen","Vodka","Luke Lu","Xuanqi Li","Jason Yeh","kuang lu","正版乔","Junming Xu","Yue WANG","颜巾斌","Andrew Li","Rakin Cheung","Wei Zhan","Yifan Ding","Shucheng Chao","T","T Peter","Nikki Xie艾伶","Lei Sheng","Yanglu Piao","Qikun CHEN","j lock","空離戲時","Nelly L","Zhihao Zhang","陈浩庆","徐聖峰","Haoyang Chen","Ting Yan","Weizhi Xie","陳玟樺","Jiawei Yao","Jiachen Li","Pei Yulong","Billie Zhang","seasea 7","金宗穎","Yiding Yang","sj l","Gufeng Zhang","Zhao Ma","FINLEY Tei","Ronaldo Zhu","于华超","nokki T","许可","Long Sha","黑暗武士","昂李","Steve Song","Wang Olivia","Shitan Yang","Michelle M","Linh Chen","Cappuc Cino","Martin Meng","Weizhi li","Andy Wang","Ding Liao","鄭詠鴻","xian X","Chenguang Zhang","Huan W","Jack Z","Yang Xiao","Amy Yi","Match Devastated","huanhuan nd","LIHANG LIU","Alvicne","chaincain ash","snailgj","hui zhao","张鹏","Rui Li","Richard Wang","Wei Pan","Qing Cheng","Jingyu Tong","Fengchao Wang","Yachi","Dmtalen Ding","Tree C"]
youtube_unique = set(youtube_raw)
print('YouTube total entries = ', len(youtube_unique))
youtube = [name + "_youtube" for name in youtube_unique]


"""
ALL

export PYTHONHASHSEED = 0
python lottery.py
"""
all_names = wechat + bili + youtube
print('Total entries = ', len(all_names))

seed = "huahualeetcode"
random.seed(seed)
print(random.choice(all_names))
