# --- Exercise 1 : Call History ---
class Phone():
    def __init__(self, phone_number:str, messages:str = "", call_history = None, msg_history = None, ):
        self.phone_number = phone_number
        self.messages = messages 
        self.call_history = [] if call_history == None else list(call_history)
        self.msg_history = [] if msg_history == None else list(msg_history)

    def call(self, phone_number:str, incall:bool = False):
        if incall:
            print(f"{phone_number} is calling you({self.phone_number})")
            self.call_history.append({phone_number: self.phone_number})
        else:
            print(f"you({self.phone_number}) are calling {phone_number}")
            self.call_history.append({self.phone_number: phone_number})
        return self

    def show_call_history(self):
        for call in self.call_history:
            for k,v in call.items():
                print(f"{k} -> {v}")

    def show_msg_history(self):
        for call in self.msg_history:
            print("***************")
            for k,v in call.items():
                print(f"{k} -> {v}")

    def send_message(self, phone_number:str, msg:str, incoming:bool = False):
        if incoming:
            print(f"{phone_number} send you: {msg}")
            a_dict = {
                "to": phone_number,
                "from": self.phone_number,
                "content": msg
            }
        else:
            print(f"you({self.phone_number}) send: {msg}")
            a_dict = {
                "to": self.phone_number,
                "from": phone_number,
                "content": msg
            }
        self.msg_history.append(a_dict)
        return self

    def show_outgoing_messages(self):
        for message in self.msg_history:
            if message["from"] != self.phone_number:
                print("***************")
                for k,v in message.items():
                    print(f"{k}: {v}")

    def show_incoming_messages(self):
        for message in self.msg_history:
            if message["from"] == self.phone_number:
                print("***************")
                for k,v in message.items():
                    print(f"{k}: {v}")

    def show_messages_from(self, phone_number):
        for message in self.msg_history:
            if message["from"] == phone_number:
                print("***************")
                for k,v in message.items():
                    print(f"{k}: {v}")

Avi_phone = Phone("0689612058")
Dad_phone = Phone("0666653966")
Avi_phone.call(Dad_phone.phone_number).call(Dad_phone.phone_number)
Avi_phone.send_message(Dad_phone.phone_number, "Coucou")
Avi_phone.send_message(Dad_phone.phone_number, "Ca va?")
Avi_phone.send_message(Dad_phone.phone_number, "... combien?", True)
# Avi_phone.show_msg_history()
# Avi_phone.show_outgoing_messages()
# Avi_phone.show_incoming_messages()
print("--------------------------")
