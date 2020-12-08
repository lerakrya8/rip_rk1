class Notification:
    def __init__(self, notification, email):
        self.notification = notification
        self.email = email

    def send_notification(self):
        print('Уведомление: ' + self.notification)
        print('Отправлена на почту: ' + self.email)
        return 'Отправлена на почту: ' + self.email


class SendToWhatsUp:
    def __init__(self, notifaer, whatsup_nickname):
        self.notifaer = notifaer
        self.whatsup_nickname = whatsup_nickname

    def send_notification(self):
        self.notifaer.send_notification()
        print('Отправлена на WhatsUp: ' + self.whatsup_nickname)
        return 'Отправлена на WhatsUp: ' + self.whatsup_nickname


class SendToTelegram:
    def __init__(self, notifaer, telegram_nickname):
        self.notifaer = notifaer
        self.telegram_nickname = telegram_nickname

    def send_notification(self):
        self.notifaer.send_notification()
        print('Отправлена на Telegram: ' + self.telegram_nickname)
        return 'Отправлена на Telegram: ' + self.telegram_nickname


class SendToVK:
    def __init__(self, notifaer, vk_nickname):
        self.notifaer = notifaer
        self.Vk_nickname = vk_nickname

    def send_notification(self):
        self.notifaer.send_notification()
        print('Отправлена в Vk: ' + self.Vk_nickname)
        return 'Отправлена в Vk: ' + self.Vk_nickname


class SendToSlack:
    def __init__(self, notifaer, slack_nickname):
        self.notifaer = notifaer
        self.slack_nickname = slack_nickname

    def send_notification(self):
        self.notifaer.send_notification()
        print('Отправлена на Slack: ' + self.slack_nickname)
        return 'Отправлена на Slack: ' + self.slack_nickname


class Client:
    def __init__(self, email, notifications_platforms, nickname=''):
        self.email = email
        self.notifications_platforms = notifications_platforms
        self.nickname = nickname


def create_notifaers(clients):
    notifaers = list()

    i = 1
    for client in clients:
        notifaer = Notification('message' + str(i), client.email)

        if 'Slack' in client.notifications_platforms:
            notifaer = SendToSlack(notifaer, client.nickname)

        if 'VK' in client.notifications_platforms:
            notifaer = SendToVK(notifaer, client.nickname)

        if 'WhatsUp' in client.notifications_platforms:
            notifaer = SendToWhatsUp(notifaer, client.nickname)

        if 'Telegram' in client.notifications_platforms:
            notifaer = SendToTelegram(notifaer, client.nickname)

        notifaers.append(notifaer)
        i += 1
    return notifaers


def notifay_all(notifaers):
    for notifaer in notifaers:
        notifaer.send_notification()
        print()
    # [lambda i: i.send_notification() for i in notifaers]


if __name__ == '__main__':
    client1 = Client('434f@dsf', ['Slack', 'Telegram'], 'client1')
    client2 = Client('fdsafd@dsf', ['WhatsUp', 'VK'], 'client2')
    client3 = Client('fdsjreio3432i@dsf', ['WhatsUp', 'VK', 'Slack'], 'client3')

    clients = list()
    clients.append(client1)
    clients.append(client2)
    clients.append(client3)
    notifay_all(create_notifaers(clients))
