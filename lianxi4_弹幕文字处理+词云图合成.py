import re
import os
from wordcloud import WordCloud
import collections
import jieba
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import codecs
from jieba import analyse

stopwords = set()
fr = codecs.open('C:\\Users\\86150\\Desktop\\stopWord.txt', 'r', 'utf-8')#选择停词表
for word in fr:
	stopwords.add(str(word).strip())
fr.close()

kk=open('./wang1.txt','a',encoding='utf-8')

text = []

with open('barrages.txt',encoding='utf-8') as fileTrainRaw:
	i = 0
	for line in fileTrainRaw:  # 按行读取文件
		# 去除非中文符号并进行jieba分词，并过滤停用词
		line = " ".join(re.findall(u'[\u4e00-\u9fa5]+', line))
		line = list(jieba.cut(line, cut_all=False, HMM=True))
		line = list(filter(lambda x: x not in stopwords, line))
		line = [str(i) for i in line if i != ' ']
		if len(line) != 0:
			text.append(' '.join(line))
			kk.write("".join(line))
			kk.write('\n')
print(text)

f = open('./wang1.txt',encoding='utf-8').read()
#使用jieba对其进行分词
f_c = " ".join(jieba.cut(f))

path = './wordcloud/'
word_counts = collections.Counter(text)
img_files = os.listdir('./pictures')
print(img_files)
for num in range(336, len(img_files) + 1):
	img = fr'.\mask_img\mask_'+str(num)+'.png'
	# 获取蒙版图片
	mask_ = 255 - np.array(Image.open(img))
	# 绘制词云
	plt.figure(figsize=(8, 5), dpi=200)
	my_cloud = WordCloud(
		background_color='white',  # 设置背景颜色  默认是black
		mask=mask_,      # 自定义蒙版
		mode='RGBA',
		max_font_size=500,  # 字体最大值
		max_words=2000,     #字体最小值
		font_path='simhei.ttf',# 设置字体  显示中文
		margin=2,#设置字体间隙
	).generate_from_frequencies(word_counts)

	# 显示生成的词云图片
	plt.imshow(my_cloud)
	# 显示设置词云图中无坐标轴
	plt.axis('off')
	word_cloud_name = path + 'wordcloud_{}.png'.format(num)
	my_cloud.to_file(word_cloud_name)    # 保存词云图片
	print(f'======== 第{num}张词云图生成 ========')




