import yaml
import pip._vendor.requests as requests
 
#with open(r'/Users/ljpdb/Documents/GitHub/DockerFile_examples/pod.yaml') as file:
#    config_list = yaml.load(file, Loader=yaml.FullLoader)
 
#print(config_list)

response = requests.get('https://gist.githubusercontent.com/chriscowley/8598119/raw/8f671464f914320281e5e75bb8dcbe11285d21e6/nfs.example.lan.yml')

#print(response.text)
config_list2 = yaml.load(response.text, Loader=yaml.FullLoader)
print(config_list2)