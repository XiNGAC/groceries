import re
import os

list_ = [("赵紫斌", "赵*斌"), ("李方雪", "李**"), ("罗进", "罗*"), ("何林波", "何**"), ("周星", "周**"),
         ("凌超", "凌**"),("吴俊杰", "*国平"), ("蔡业浩", "*浩"), ("王立军", "*立*"), ("倪钦钦", "倪**"),
         ("黄旭官", "**官"), ("李小燕", "xx燕"), ("贺长", "xx长"), ("瞿宏平", "瞿xx"), ("吴俊", "x俊"),      
         ("魏贤刚", "x贤**"), ("程文昌", "**昌"), ("蔺刚龙", "蔺刚龙"), ("王保林", "王保林"), 
         ("伍贤军", "伍贤军"), ("陈孝顺", "陈孝顺"), ("赵丹", "赵丹"), ("石义才", "石才"), 
         ("刘海良", "傅海良"), ("希锋", "伊希"), ("陈碧婷", "彭百凌"), ("郝华丽", "杨勇"), 
         ("杨雪", "*雪*"), ("戴森杰", "*戴**"), ("赵紫斌", "赵斌*"), ("王志刚", "*志*"), 
         ("邓君", "**"), ("刘学智", "")]

def judge_name(data, judge_data):
    """
    0--无法匹配；
    1--匹配一致；
    2--匹配不一致；
    3--模糊匹配一致
    """
    pat = u"([\u4e00-\u9fff]+)"
    if not data or data == u'运营商未透露' or not judge_data:
        return 0
    # if len(data) != len(judge_data):
    #     return 2
    pattern = re.compile(pat)
    results = pattern.findall(data)
    if not results:
        return 0
    ret = [len(list(filter(None, data.split(i)))) == len(list(
        filter(None, judge_data.split(i)))) for i in results if (i in judge_data)]
    if not ret or False in ret:
        return 2
    if '*' in data or 'x' in data:
        return 3
    return 1

print (os.path.dirname(os.path.abspath("__file__")))
print (os.path.pardir)
print (os.path.join(os.path.dirname("__file__"),os.path.pardir))
print (os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir)))
