import io
import time
import picamera
from PIL import Image
import pyzbar.pyzbar as pyzbar
import requests

while(True)
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    pil = Image.open(stream)
    #
    #########################################
    #
    # create a reader
    texts = pyzbar.decode(pil)
    for text in texts:
    tt = text.data.decode("utf-8")
    print(tt)

    # clean up
    del(image)
    camera.close()

