import moviepy.editor as mpy
# 读取词云视频
my_clip = mpy.VideoFileClip('result.mp4')
# 截取背景音乐
audio_background = mpy.AudioFileClip('C:\\Users\\86150\\Desktop\\sh.mp3').subclip(0,14)#截取音频的时间片段长度
audio_background.write_audiofile('song1.mp3')
# 视频中插入音频
final_clip = my_clip.set_audio(audio_background)
# 保存为最终的视频   动听的音乐！漂亮小姐姐词云跳舞视频！
final_clip.write_videofile('final_video.mp4')

