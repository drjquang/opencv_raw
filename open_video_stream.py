import json
import cv2

with open('Resources/camera_cred.txt') as json_file:
    data = json.load(json_file)
    username = data["username"]
    password = data["password"]
    ip_address = data["ip_address"]

stream = "rtsp://{0}:{1}@{2}/Streaming/Channels/301/httpPreview".format(username, password, ip_address)
cap = cv2.VideoCapture(stream)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    key_stroke = cv2.waitKey(1)
    if key_stroke & 0xFF == ord('q'):
        break
    elif key_stroke & 0xFF == ord('s'):
        # read json file to retrieve image_info
        with open('Resources/image_info.txt') as json_file:
            data = json.load(json_file)
            json_file.close()
            image_name = data["image_name"]
            image_no = int(data["image_no"])
        # save image
        img_name = "Snapshot_ipcam/{0}_{1}.jpg".format(image_name, image_no)
        cv2.imwrite(img_name, img)
        print("Successfully take snapshot {}".format(img_name))
        # write json file
        image_no = image_no + 1
        data["image_no"] = str(image_no)
        with open('Resources/image_info.txt', 'w') as outfile:
            json.dump(data, outfile)
            outfile.close()
