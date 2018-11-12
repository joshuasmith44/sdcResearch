import json, io
home_dir = '/Users/joshuasmith/Programming/LightResearch/light-detection/Yolo/smallTestData/'
with open(home_dir + 'singleAnnotationTest.json') as data_file:
    myData = json.load(data_file)

for image in myData:
    print(image['name'])
    i = 0
    while i < len(image['labels']):
        if(image['labels'][i]['category'] == 'drivable area' or image['labels'][i]['category'] == 'lane'):
            del image['labels'][i]
        else:
            print image['labels'][i]['category']
            i += 1;

with io.open('modifiedAnnotationTest.json', 'w') as output_file:
    output_file.write(json.dumps(myData, ensure_ascii = False, sort_keys=True, indent=4))
