import picamera

camera = picamera.PiCamera(resolution=(1640, 1232), framerate=30)
camera.start_recording('1.h264')
camera.wait_recording(30)
for i in range(2, 100):
    camera.split_recording('%d.h264' % i)
    camera.wait_recording(30)
camera.stop_recording()
