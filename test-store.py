from mocked_data import STAGES
from state import Store, ClientData, Record

user_storage = Store()

empty_client_data = ClientData('', '')
# record = Record('123243', empty_client_data, STAGES[0])
# user_storage.add_new_record(record)
print(user_storage.storage)
