import gigachat as giga
from gigachat.models import ChatCompletion
from typing import List, Dict

class Payload:
    def __init__(self, system_message: str, user_message: str, function_list: List[Dict] = None):
        self.system_message = system_message
        self.user_message = user_message
        self.function_list = function_list

class LlmClient:
    def __init__(self, token: str, model: str):
        self.llm = giga.GigaChat(credentials=token, model=model, verify_ssl_certs=False)
            
    def request(self, payload: Payload) -> ChatCompletion:
        sysm, usrm, flist = payload.system_message, payload.user_message, payload.function_list

        messages = []
        if sysm:
            messages.append(
                {
                    "role":"system",
                    "content":sysm
                }
            )
        messages.append(
            {
                "role":"user",
                "content":usrm
            }
        )
        
        chat_params = {
            "messages": messages
        }
        
        if flist:
            chat_params["function_calling"] = "auto"
            chat_params["function_list"] = flist
            
        payload_obj = chat_params
        
        response = self.llm.chat(payload_obj)
        return response