import yaml
with open('mocked_data/stages.yaml', 'r', encoding='utf-8') as read_yaml_file:
    cfg = yaml.safe_load(read_yaml_file)


class StageList:
    start_stage = 'start_stage'
    hello_stage = 'hello_stage'
    choose_service_stage = 'choose_service_stage'
    get_phone_stage = 'get_phone_stage'
    finish_stage = 'finish_stage'


STAGES = dict()

for idx, stage in enumerate(cfg):
    STAGES[stage['name']] = {'id': idx, **stage}

# print(StageList)
# print(STAGES['hello_stage'])

SERVICE_TYPES = [
    'Электроника',
    'Бытовая техника',
    'Проводка'
]