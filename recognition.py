import requests, base64
import time
import datetime
import os
import json

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '7dc0a1103c3744fa80e5b1f8d72d8442',
    'Prediction-Key': '3cf083a425934f9eb7a63b8ce459ab3a',
}

params = {
    # optional
    'visualFeatures': 'Categories',
    'language': 'en',
}

PHOTOS_DIRECTORY = "yolo/darknet/output"

def get_latest_filename():
    return (sorted(os.listdir(PHOTOS_DIRECTORY)))[-1]

def get_timestamp_from_filename():
    latest_filename = (sorted(os.listdir(PHOTOS_DIRECTORY)))[-1]
    latest_times = ' '.join(((((latest_filename.split('.'))[0]).split('_'))[1:]))
    datetime_object = datetime.datetime.strptime(latest_times, '%Y %m %d %H %M %S')
    return datetime_object

def get_latest_logged_timestamp():
    food_log = json.load(open('food_log.json'))
    latest_logged_time = food_log[-1]['datetime']
    datetime_object = datetime.datetime.strptime(latest_logged_time, '%Y_%m_%d_%H_%M_%S')
    return datetime_object

def is_there_a_new_image():
    delta_seconds = get_timestamp_from_filename() - get_latest_logged_timestamp()
    return delta_seconds > datetime.timedelta(0)

def get_calories_from_label(label):
    with open('nutritional_info.json') as f:
        data = json.load(f)
        return data[label]['energy']
    return -1

def get_sugar_from_label(label):
    with open('nutritional_info.json') as f:
        data = json.load(f)
        return data[label]['sugar']
    return -1


while True:

    if is_there_a_new_image():

        image = open(PHOTOS_DIRECTORY + '/' + get_latest_filename(), 'rb').read()

        label, probability = 'none', 0

        try:
            response = requests.post(url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/6ff322bf-f381-432a-88fb-1cd46474f39a/image?iterationId=669f7fbf-a7ed-4afe-9ce1-4f668c802e98',
                                     headers = headers,
                                     params = params,
                                     data = image)
            data = response.json()
            #print(data)
            label = data['Predictions'][0]['Tag']
            probability = data['Predictions'][0]['Probability']

            #print(label, probability)
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


        #print(get_latest_filename(), label, probability)

        # write to file
        new_json_row = {"label": label, "energy": get_calories_from_label(label), "sugar": get_sugar_from_label(label), "datetime": datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}
        with open('food_log.json') as f:
            data = json.load(f)
        data.append(new_json_row)
        with open('food_log.json', 'w') as f:
            json.dump(data, f)



    time.sleep(1)