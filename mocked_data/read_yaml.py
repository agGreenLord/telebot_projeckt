import yaml


with open('stages.yaml', 'r', encoding='utf-8') as read_yaml_file:
    cfg = yaml.safe_load(read_yaml_file)

# for i_line in cfg:
#     STAGES[i_line] = i_line['name']


STAGES_TYPES = [i_line['name'] for i_line in cfg]
print(STAGES_TYPES)

STAGES = dict()
for i_line in cfg:
    STAGES[i_line['name']] = i_line
print(STAGES)
