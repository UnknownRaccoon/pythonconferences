from datetime import datetime
import json
from channels import Group
from channels.sessions import channel_session
from chat.models import Message
from custom_auth.models import Profile


@channel_session
def ws_connect(message):
    print(message['path'])
    try:
        get_dict = {param.split('=')[0]: param.split('=')[1] for param in message['query_string'].split('&')}
        users = sorted([get_dict[k] for k in ('user', 'companion') if k in get_dict])
        if not message['path'].startswith('/chat') and 'companion' not in get_dict.keys():
            Group('notifications-user' + get_dict['user'],
                  channel_layer=message.channel_layer).add(message.reply_channel)
            message.channel_session['notifications'] = 'user' + get_dict['user']
        else:
            Profile.objects.get(pk=get_dict['user'])
            Profile.objects.get(pk=get_dict['companion'])
            label = ''.join([users[0], 'q', users[1]])
            print(label)
            Group('chat-' + label, channel_layer=message.channel_layer).add(message.reply_channel)
            message.channel_session['room'] = label
    except ValueError:
        return
    except Profile.DoesNotExist:
        return


@channel_session
def ws_receive(message):
    try:
        label = message.channel_session['room']
    except KeyError:
        return
    try:
        data = json.loads(message['text'])
    except ValueError:
        return

    if set(data.keys()) != {'message', 'sender', 'recipient'}:
        return
    if data:
        m = Message.objects.create(text=data['message'], sender=Profile.objects.get(pk=data['sender']),
                                   recipient=Profile.objects.get(pk=data['recipient']), date=datetime.now())
        Group('chat-' + label, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})
        print(str(m.recipient.id), str(m.sender.id))
        Group('notifications-user' + str(m.recipient.id),
              channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})


@channel_session
def ws_disconnect(message):
    try:
        notifications = message.channel_session['notifications']
        chat = message.channel_session['room']
        Group('chat-' + chat, channel_layer=message.channel_layer).discard(message.reply_channel)
        Group('notifications-user' + notifications, channel_layer=message.channel_layer).discard(message.reply_channel)
    except KeyError:
        pass
