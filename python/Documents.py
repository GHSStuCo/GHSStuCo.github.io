def main():
  committees = []
  with open('text/Documents.txt') as input_file:
    for line in input_file:
      line = unicode(line.strip(), 'utf8')
      if(line.startswith('*')):
        name, chair = line.lstrip('*').lstrip().split('|')
        committees.append({'name': name, 'chair': chair, 'members': []})
      elif(line != ''):
        committees[-1]['members'].append(line)
  for committee in committees:
    committee['members'].sort(key = lambda a: tuple(a.split(" ")[::-1]))
  return {'committees': committees}
