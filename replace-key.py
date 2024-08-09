import argparse
import yaml

parser = argparse.ArgumentParser()

parser.add_argument('--file', help='Filename', required=True)
parser.add_argument('--key', help='The key to update', required=True)
parser.add_argument('--value', help='New value as is. Add quotes if required', required=True)

args = parser.parse_args()
tag = args.key
newValue = args.value

print ("{} {} ".format(tag, newValue))
with open(args.file) as f:
   doc = yaml.safe_load(f)
   key_path_list = [int(e) if e.isdigit() else e for e in tag.split(".")]

   depth = len(key_path_list)
   for i in range(0, depth):
      if i == depth - 1:
         doc[key_path_list[i]] = newValue
      else:
         doc = doc[key_path_list[i]]

with open(args.file, 'w') as f:
   yaml.dump(doc, f)
