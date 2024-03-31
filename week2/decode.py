def decode(message_file: str):
    message_dict = {}

    with open(message_file) as f:
        messages = f.readlines()
    
    for message in messages:
        message = message.strip().split(' ')
        message_dict[int(message[0])] = message[1]

    curr_message_id = 1
    step = 2

    decoded_message = ''
    while curr_message_id in message_dict:
        decoded_message += message_dict[curr_message_id] + ' '
        curr_message_id += step
        step += 1

    return decoded_message.strip()


print(decode('prac.txt'))
print(decode('coding_qual_input.txt'))