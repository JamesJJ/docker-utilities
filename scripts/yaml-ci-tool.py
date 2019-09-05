import sys
import re
from ruamel.yaml import YAML
from pprint import pprint as pp

image_match = sys.argv[1]
image_new = sys.argv[2]

# TODO: input validation
# TODO: check for file exist
# TODO: handle other than 'deployment' / 'CronJob'
# TODO: let the match be a regex match, instead of the escaped match (safely)

with YAML(output=sys.stdout) as yaml:
    yaml.explicit_start = True
    yaml.allow_unicode = True
    for data in yaml.load_all(sys.stdin):
        if data is not None:
            if (data['kind'] == 'Deployment'):
                for i,c in enumerate(data['spec']['template']['spec']['containers']):
                    if re.search(re.escape(image_match), c['image']):
                        data['spec']['template']['spec']['containers'][i]['image'] = image_new
            if (data['kind'] == 'CronJob'):
                for i,c in enumerate(data['spec']['jobTemplate']['spec']['template']['spec']['containers']):
                    if re.search(re.escape(image_match), c['image']):
                        data['spec']['jobTemplate']['spec']['template']['spec']['containers'][i]['image'] = image_new
            yaml.dump(data)

