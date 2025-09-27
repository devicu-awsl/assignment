# from jetson_inference import detectNet
# from jetson_utils import videoSource, videoOutput
import jetson.inference
import jetson.utils

# Opening the camera stream
net = detectNet("ssd-mobilenet-v2", threshold=0.5)

# Display loop
camera = videoSource("/dev/video0") # '/dev/video0' for V4L2
while display.IsStreaming(): # main loop will go here

# Camera capture
display = videoOutput("display://0") # 'my_video.mp4' for file
while display.IsStreaming(): # main loop will go here
	img = camera.Capture()
	if img is None: # capture timeout
		continue
	
	detections = net.Detect(img)
	
	for detection in detections:
		print(detection)
	
	# Rendering
	display.Render(img)
	display.SetStatus("Object Detection | {:.0f} FPS".format{net.GetNetworkFPS()})
