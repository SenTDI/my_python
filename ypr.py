message = ["Тебе нужно быть сегодня в 9 дома !","На столе лежат яблоки."]
sent_message = []
def send_message(message,sent_message):
  while message:
    message_1 = message.pop()
    sent_message.append(message_1)
send_message(message[:],sent_message)
print(message)
print(sent_message)
