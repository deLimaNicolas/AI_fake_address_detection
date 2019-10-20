import re
import urllib.request
import geocoder

from constants import GOOGLE_KEY, MAP_BOX_URL, MAP_BOX_KEY


def has_letter(string):
    return re.search('[a-zA-Z]', string)


def remove_number(data_frame):
    for idx, elm in enumerate(data_frame):
        if(has_letter(str(elm))):
            data_frame[idx] = ' '


def concat_addr(row): return row['End_Atual_B2k'] + ' ' + str(
    row['Nr_Atual_B2k']) + ',' + row['Cidade_Atual_B2k'] + ' ' + row['Estado_Atual_B2k']


def concat_addr_step(row): return row['End_Atual_B2k'] + ' ' + \
    str(row['Nr_Atual_B2k']) + ',' + row['Cidade_Atual_B2k']


def get_data_addr(data_frame, rule):
    return data_frame.apply(rule, axis=1).to_list()


def get_coords_and_accuracy(adresses, adresses_step):
    coords = []
    accuracy = []
    for idx, ad in adresses:
        response = geocoder(ad, key=GOOGLE_KEY)
    if(response.status == 'OK'):
        coords.append(str(response.latlng[1]) + ',' + str(response.latlng[0]))
        accuracy.append(response.json["accuracy"])
    else:
        response = geocoder(adresses_step[idx], key=GOOGLE_KEY)
        coords.append(str(response.latlng[1]) + ',' + str(response.latlng[0]))
        accuracy.append(response.json["accuracy"])
    return coords, accuracy


def get_addr_images(coords):
    for idx, elm in enumerate(coords):
        image = urllib.request.urlopen(
            f'{MAP_BOX_URL}{str(elm)},18,0/300x300?access_token={MAP_BOX_KEY}').read()
    with open(f'../images/image{idx}.jpg', 'wb') as f:
        f.write(image)
