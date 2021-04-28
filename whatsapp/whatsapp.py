from defcon_utils import BaseAPI
from enum import Enum 

class MessageType(Enum): 
    TEXT_MESSAGE = "TEXT_MESSAGE"
    FILE = "FILE"
    PTT_AUDIO = "PTT_AUDIO"
    LINK = "LINK"
    CONTACT = "CONTACT"
    LOCATION = "LOCATION"
    VCARD = "VCARD"
    PRODUCT = "PRODUCT"
    

class APIStatus(Enum):
    INIT = "INITIAL_STATUS"
    LOADING = "Loading, try again in 1 minute"
    QR_CODE = "Got QR code that needs to be scanned on the app"
    AUTHENTICATED = "Authorized successfully"
    CONFLICT = "WhatsApp is open on another computer or browser."
    
    
    @classmethod
    def parse_status(cls, data): 
        data = data.lower().strip()
        
        if data == "init": 
            return cls.INIT
        elif data == "loading": 
            return cls.LOADING
        elif data == "got qr code": 
            return cls.QR_CODE
        elif data == "authenticated": 
            return cls.AUTHENTICATED
        elif data == "conflict": 
            return cls.CONFLICT
        else: 
            raise Exception("Unknown status: {}".format(data))
        
class WhatsApp(BaseAPI):
    TOKEN = None
    INSTANCE_ID = None

    @staticmethod
    def parse_indian_phone_number(phone):
        from defcon_utils.parser import parse_phone_number
        parsed_phone_number = "91" + parse_phone_number(phone)
        return parsed_phone_number

    def __init__(self, token, instance_id):
        self.INSTANCE_ID = instance_id
        self.TOKEN = token

        self.BASE_URL = "https://api.chat-api.com/" + self.INSTANCE_ID + "/{}?token=" + self.TOKEN

    def get_status(self):
        """
        init:	Initial status
        loading:	The system is still loading, try again in 1 minute
        got qr code:	There is a QR code and you need to take a picture of it in the Whatsapp application by going
                        to Menu -> WhatsApp Web -> Add. QR code is valid for one minute.
                        Example showing base64 images on a page .
                        Manually easier to get QR-code as an image
        authenticated	Authorization passed successfully
        """
        response = self.make_request("status", self.RequestType.GET, full=True)
        data = response.json()
        parsed_status = APIStatus.parse_status(data.get('accountStatus'))
        if parsed_status == APIStatus.LOADING: 
            status_data = data.get('statusData', {})
            reason = status_data.get('reason', "")
            parsed_status = APIStatus.parse_status(reason)
            
        data['parsed_status'] = parsed_status
        
        return data

    def takeover(self):
        response = self.make_request("takeover", self.RequestType.POST)
        return response

    def reboot(self):
        response = self.make_request("reboot", self.RequestType.GET)
        return response

    def get_message_queue(self):
        response = self.make_request("showMessagesQueue", self.RequestType.GET)

        return response.json()

    def send_message(self, phone, message):
        assert phone, "Cannot send message without phone numbers"

        phone = self.parse_indian_phone_number(phone)
        response = self.make_request("sendMessage", self.RequestType.POST, body=message, phone=phone)

        return response

    def send_file(self, phone, file_data, file_name, caption=None):
        """
        phone:	Required if chatId is not set	The same as POST /sendMessage
        file_data:	Required	HTTP link https://upload.wikimedia.org/wikipedia/ru/3/33/NatureCover2001.jpg
                                Or base64-encoded file with mime data, for example data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ...
                                File in form-data input field
        file_name:	Required	File name, for example 1.jpg or hello.xlsx
        caption:	Optional	Text under the photo
        """
        response = self.make_request("sendFile", self.RequestType.POST,
                                     body=file_data, phone=phone, cached=True,
                                     filename=file_name, caption=caption)

        return response


