## Py-WhatsApp: Unofficial python package for [chat-api.com](https://chat-api.com)

### Chat-API

It is a multifunctional rest api for WhatsApp accounts working on top of WhatsApp web. They offer a 3-day free trial to allow you to use the service before buying and this python package allows you to interface with most of its services directly.

### Installing

You can use the command `pip install whatsapp-api` to install the latest stable version from PyPi.

### Usage

Before using any of the available functions below you need to create an instance of the `Whatsapp` class object and needs to supply your `instanceId` and `token` which you can get from your [chat-api.com](https://chat-api.com) account. 

```python
from whatsapp import WhatsApp

token = "xxxxxxx"
instance_id = "instancexxx"

object = WhatsApp(token, instance_id)
```

Following are the currently supported functions with examples. We will use this `object` directly for the rest of the examples. 

1. **Send a text message**
To send a message the mobile number must me in the international format with approriate country code. For eg. if you want to send a message to an Indian mobile number (country code - +91) with number 1234512345 you need to use `911234512345` as phone number in the argument.
Default whatsapp message formatting will work as usual. Like \_This text will be in italics_. 

    ```python
    phone_number = "911234512345"
    message = "This is a sample text message. *This will be bold*"
    response = object.send_message(phone_number, message)
    ```

2. **Send a file**
You can either send a file from a URL or in base64 encoded format. You can also optionally add a caption to the file which will be added below the message.

    ```python
    phone_number = "911234512345"
    file_data = """
                HTTP link https://upload.wikimedia.org/wikipedia/ru/3/33/NatureCover2001.jpg
                Or base64-encoded file with mime data, for example data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ...
                File in form-data input field
                """
    file_name = "Name of the file"
    caption = "This is a file caption" # Optional
    response = object.send_file(phone, file_data, file_name, caption)
    ```

3. **Get current status**
Returns the current overall status as a dictionary.

    ```python
    status = object.get_status()
    ```

4. **Logout**
Logs you out of the whatsapp web instance and `object.get_status()` will now return with the QR code data which you can scan to log in to another whatsapp account.

    ```python
    response = object.logout()
    ```

5. **Get waiting message queue**
Sometimes there is a delay in sending message mostly due to limited connectivity on the mobile phone running the whatsapp application. During this time, the messages are queued and retried at a later time. This function returns the list of all waiting messages in queue as python object. 
**Note: Atmost 400 messages can be present in a queue at a time, post that message sending will fail.**

    ```python
    queue = object.get_message_queue()
    ```

6. **Reboot**
Reboots the chat-api instance.

    ```python
    response = object.reboot()
    ```

7. **Takeover instance**
As you might be aware that currently whatsapp web can only be active on a single browser. Hence, you should not use whatsapp web anywhere else if you are using chat-api. But if opened it somewhere else, you can use the  takeover function to make chat-api instance active again.

    ```python
    response = object.takeover()
    ```

### Building

- Clone the repository `git clone https://github.com/DefCon-007/py-whatsapp`
- Create a new python3 virtual environment in the newly created directory. `cd py-whatsapp` and then `python3 -m venv`
- To create a new distribution package, increase the `VERSION` in `setup.py` file and then run `python setup.py sdist bdist_wheel`. This will create a new distribution package for the new version in dist directory.

- **Installing newly crated distribution package in a local python environment**

  - Use the command `pip install whatsapp-api --no-index --find-links file://<path_to_py-whatsapp_directory>/dist  --no-cache-dir` to install the newly generated distribution.

### TODOs

- [ ] Parse the HTTP responses into custom objects for better usability. 
- [ ] Add remaining API functions.
