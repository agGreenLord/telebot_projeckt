from dataclasses import dataclass
from mocked_data import StageList, SERVICE_TYPES
from typing import List


@dataclass
class ClientData:
    phone_number: str
    selected_service: SERVICE_TYPES


@dataclass
class RecordType:
    chat_id: str
    data: ClientData
    current_stage: StageList


class Record(RecordType):
    def __init__(self, chat_id: str, data: ClientData, current_stage: StageList) -> None:
        self.chat_id = chat_id
        self.data = data
        self.current_stage = current_stage

    @property
    def chat_id(self) -> str:
        return self._chat_id

    @property
    def data(self) -> ClientData:
        return self._data

    @property
    def current_stage(self) -> StageList:
        return self._current_stage

    @chat_id.setter
    def chat_id(self, chat_id: str) -> None:
        self._chat_id = chat_id

    @data.setter
    def data(self, data: ClientData) -> None:
        self._data = data

    @current_stage.setter
    def current_stage(self, current_stage: StageList) -> None:
        self._current_stage = current_stage


class Store:
    storage: List[RecordType]

    def __init__(self):
        self.storage = []

    @property
    def storage(self) -> List[RecordType]:
        return self._storage

    @storage.setter
    def storage(self, value: list) -> None:
        self._storage = value

    def add_new_record(self, record: Record) -> None:
        self.storage.append(record)

    def get_record_by_chat_id(self, our_chat_id) -> RecordType:
        print('get record')
        for i_record in self.storage:
            if i_record.chat_id == our_chat_id:
                return i_record

    def delete_record(self, our_chat_id: int) -> None:
        tempRecord = self.get_record_by_chat_id(our_chat_id)
        if tempRecord:
            print('delete record: ', tempRecord.chat_id)
            self.storage.remove(tempRecord)

    def update_stage(self, our_chat_id: int, stage: str) -> None:
        print('get record')
        self.get_record_by_chat_id(our_chat_id).current_stage = stage

    def update_phone(self, our_chat_id: int, number: str) -> None:
        print('get record')
        self.get_record_by_chat_id(our_chat_id).data.phone_number = number

    def update_service(self, our_chat_id: int, service: str) -> None:
        print('get record')
        self.get_record_by_chat_id(our_chat_id).data.selected_service = service







