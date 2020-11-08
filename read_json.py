import json

with open('Resources/image_info.txt') as json_file:
    data = json.load(json_file)
    json_file.close()
    print(data["image_name"])
    print(data["image_no"])
    image_no = int(data["image_no"])
    image_no = image_no + 1
    data["image_no"] = str(image_no)

with open('Resources/image_info.txt', 'w') as outfile:
    json.dump(data, outfile)
    outfile.close()
