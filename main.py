from whats import Whats

whats = Whats("firefox", "owner name", headless=True, verbose=True)

while True:
    (chat, last_message) = whats.check_new_message()
    if last_message != "":
        whats.send_message("No chat {} foi dito:\n{}".format(chat, last_message), "outro chat")

whats.close()