import jieba
seg_list = jieba.cut("甲状腺大小正常包膜完整右叶腺体内可见0.2*0.3厘米的低回声结节边界清内部回声尚均cdfi未见异常血流信号", cut_all = False)
print ("Full Mode:", ' '.join(seg_list))

'''
seg_list = jieba.cut("我来到北京清华大学")
print ("Default Mode:", ' '.join(seg_list))
'''