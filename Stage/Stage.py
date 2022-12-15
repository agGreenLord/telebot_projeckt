class Store:
    chat_id = list()
    data = dict()
    current_stage = dict()



    def create_new_record(self, user_id, state):
        self.chat_id.append(user_id)
        self.current_stage[self.chat_id] = state


    def date_record(self, phone, servis):
        self.data[self.chat_id] = [phone, servis]

    def delete_record(self):
        pass


