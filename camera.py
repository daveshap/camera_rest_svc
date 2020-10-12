import requests
import json
import cv2
import time
import numpy


def send_msg(data, meta, ip, port):
    payload = {'data':data, 'meta':meta}
    response = requests.request(method='POST', url='http://%s:%s' % (ip, port), json=payload)
    print(response.url, response.ok, response.status_code, meta)


def main(camera):
    print('STARTING: video publish loop')
    while True:
        try:
            time.sleep(1)  # TODO parameterize this
            s, img = camera.read()
            lists = img.tolist()
            json_str = json.dumps(lists)
            meta = {'time':time.time()}  # TODO add image metadata (numpy, dimensionality, etc)
            send_msg(json_str, meta, '127.0.0.1', 9999)  # TODO parameterize this
        except Exception as oops:
            print('ERROR:', oops)


if __name__ == '__main__':
    print('Instantiating camera index 0')
    cam = cv2.VideoCapture(0)  # TODO parameterize this
    main(cam)