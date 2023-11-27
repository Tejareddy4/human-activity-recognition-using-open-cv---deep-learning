# human-activity-recognition-using-open-cv-deep-learning

Requirements:

Above Python 3.10.11 : pip install python 3.10.11  <br />
At least OpenCV 4.1.2 : pip install OpenCv  <br />
imutils : pip install imutils  <br />
cv2 : pip install cv2  <br />

Download Trained DataSet :


<u>Structure of the Directory:</u>  <br />
$ Parent Directory <br />
.<br />
├── action_recognition_kinetics.txt <br />
├── resnet-34_kinetics.onnx <br />
├── example_activities.mp4 <br />
├── human_activity_main.py  <br />
<br />

Run the code from the Project Directory <br />
 #for input video "python human-activity-main.py --model resnet-34_kinetics.onnx --classes Actions.txt --input example_activities.mp4 --gpu 1 --output output.mp4" <br />
#For Live can use this command : "python HAR.py --model resnet-34_kinetics.onnx --classes Actions.txt" <br />

