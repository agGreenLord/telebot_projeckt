from dataclasses import dataclass
from mocked_data import STAGES, SERVICE_TYPES
from typing import List


@dataclass
class ClientData:
    phone_number: str
    selected_service: SERVICE_TYPES


@dataclass
class RecordType:
    chat_id: str
    data: ClientData
    current_stage: STAGES


class Record(RecordType):
    def __init__(self, chat_id: str, data: ClientData, current_stage: STAGES) -> None:
        self.chat_id = chat_id
        self.data = data
        self.current_stage = current_stage

    @property
    def chat_id(self) -> str: return self._chat_id

    @property
    def data(self) -> ClientData: return self._data

    @property
    def current_stage(self) -> STAGES: return self._current_stage

    @chat_id.setter
    def chat_id(self, chat_id: str) -> None: self._chat_id = chat_id

    @data.setter
    def data(self, data: ClientData) -> None: self._data = data

    @current_stage.setter
    def current_stage(self, current_stage: STAGES) -> None: self._current_stage = current_stage


class Store:
    storage: List[RecordType]

    def __init__(self): self.storage = []

    @property
    def storage(self) -> List[RecordType]: return self._storage

    @storage.setter
    def storage(self, value):
        self._storage = value

    def add_new_record(self, record: Record) -> None:
        self.storage.append(record)

    def get_record_by_chat_id(self, phone, servis) -> Record:
        print('get record')
        # TODO create search  by chat_id field and return record

    def delete_record(self):
        print('get record')
        # TODO create search  by chat_id field and remove this item

    def update_record(self):
        print('get record')
        # TODO create logic to update rerord
