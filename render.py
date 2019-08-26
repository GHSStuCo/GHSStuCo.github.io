from jinja2 import Environment, PackageLoader, select_autoescape
import sys
from importlib import import_module

env = Environment(
  loader=PackageLoader('html', ''),
  autoescape=select_autoescape(['html'])
)

filename = sys.argv[1]

with open(filename + '.html', 'w') as output:
  variables = import_module('python.' + filename).main()
  template = env.get_template(filename + '.html')
  output.write(template.render(**variables).encode("utf8"))
