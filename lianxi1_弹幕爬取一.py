# -*- coding: UTF-8 -*-
#在B站网站钱加i可以获取相关的api
"""
@File    ：spider.py
@Author  ：叶庭云
@CSDN    ：https://yetingyun.blog.csdn.net/
"""
import requests
import pandas as pd
import re
import time
import random
def Grab_barrage(date):
	# 伪装请求头
	headers = {
		"cookie": "_uuid=2F73E606-C80F-3013-0EF1-5E83CE0F4DDF02246infoc; buvid3=C7B1ADC3-AEB3-4170-A585-F24A0F9621E713423infoc; buvid_fp_plain=C7B1ADC3-AEB3-4170-A585-F24A0F9621E713423infoc; rpdid=|(J|)lJJmYuJ0J'uYu)YkJ|uk; LIVE_BUVID=AUTO4716229750078067; DedeUserID=334433953; DedeUserID__ckMd5=ecd7cd14c16b5e99; SESSDATA=42bb5153,1649846079,d9f9c*a1; bili_jct=71435eb50825399e9498fbdebbb97af4; video_page_version=v_old_home; fingerprint3=2a5a7be7b1cf46a215e1571923898208; fingerprint_s=153ac7c8c30253516faad2610ca43036; CURRENT_BLACKGAP=0; blackside_state=0; i-wanna-go-back=-1; b_ut=5; buvid_fp=5f02aadd81818ec230e1e06ed76de39f; buvid4=63832B80-16D2-580A-9220-99CC669D485B42256-022012118-ho21+qF6LZpQSWY96sgbctCGICgispogWm9iyofhw9jxl+lZ3oScCA==; fingerprint=5f02aadd81818ec230e1e06ed76de39f; nostalgia_conf=-1; CURRENT_QUALITY=80; bp_t_offset_334433953=639552228535828481; bp_video_offset_334433953=642897243547893800; b_lsid=10757F65E_17FDA21A16E; sid=9bzo0h3s; innersign=1; CURRENT_FNVAL=4048; PVID=1",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
	}

	params = {
		'date': date
	}
	# 发送请求  获取响应
	response = requests.get(url,params=params,headers=headers)
	# print(response.encoding)   重新设置编码
	response.encoding = 'utf-8'
	# print(response.text)
	with open('shi.txt', 'a', encoding='utf-8') as ff:
		ff.write(response.text)

	# 正则匹配提取数据
	comment = re.findall('.*?([\u4E00-\u9FA5]+).*?', response.text)#参数匹配的东西，在哪去匹配
	print(comment)
	# 将每条弹幕数据写入txt
	with open('barrages.txt', 'a',encoding='utf-8') as f:
		for con in comment:
			f.write(con + '\n')
	time.sleep(random.randint(1, 3))  # 休眠



if __name__ == '__main__':
	# 目标url
	url = "https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=551252064&"
	start = '20220316'
	end = '20220330'
	# 生成时间序列
	date_list = [x for x in pd.date_range(start, end).strftime('%Y-%m-%d')]
	print(date_list)
	count = 0
	# 调用主函数
	for i in date_list:
		Grab_barrage(i)



