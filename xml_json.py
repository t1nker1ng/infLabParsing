import xmltodict , json, time
start_time= time.time()
with open("C:\\Users\\egorn\\PycharmProjects\\pythonProject\\lab4_rasp.xml",'r',encoding="utf8") as input_file:
    text = input_file.read()
t=xmltodict.parse(text)
with open("C:\\Users\\egorn\\PycharmProjects\\pythonProject\\out1.json",'w',encoding="utf8") as output_file:
    output_file.write(json.dumps(t))
print("--- %s seconds ---" % (time.time() - start_time))