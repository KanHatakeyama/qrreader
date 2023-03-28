import cv2


class QRReader:
    def __init__(self, model_dir):
        self.qr = cv2.wechat_qrcode.WeChatQRCode(
            model_dir+"detect.prototxt",
            model_dir+"detect.caffemodel",
            model_dir+"sr.prototxt",
            model_dir+"sr.caffemodel")

    def read(self, img, n=3):
        h, w, c = img.shape
        h1 = h // n
        w1 = w // n

        data_list = []
        point_list = []

        for i in range(n):
            for j in range(n):
                split_img = img[i*h1:(i+1)*h1, j*w1:(j+1)*w1]

                data, points = self.qr.detectAndDecode(split_img)
                if data:
                    for s, p in zip(data, points):
                        data_list.append(s)
                        point_list.append(p+(j*w1, i*h1))

        return data_list, point_list
