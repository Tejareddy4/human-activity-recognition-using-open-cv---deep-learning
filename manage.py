import os

try:
    os.system('cmd /k "python human-activity-main.py --model resnet-34_kinetics.onnx --classes Actions.txt --input test/youtube/test3.mp4 --gpu 1 --output output/output4.mp4"')

except:
    print('could not execute the command')
