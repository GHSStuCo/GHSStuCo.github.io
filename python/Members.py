from os.path import exists

def main():
  members = {}
  groups = []
  with open('text/Members.txt') as input_file:
    for line in input_file:
      line = line.strip()
      if(line.startswith('#')):
        title, id = line.lstrip('#').lstrip().split('\t')
        groups.append({'title': title, 'id': id})
        members[id] = []
      elif(line != ''):
        image, position, name, bio = unicode(line, "utf8").split('\t')
        if(not exists('People/' + image + '.png')):
          image = 'default'
        members[id].append({'image': image, 'position': position, 'name': name, 'bio': bio})
  return {'members': members, 'groups': groups}
