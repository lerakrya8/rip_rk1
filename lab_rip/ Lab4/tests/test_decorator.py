from decorator import *
import unittest


class DecoratorsTests(unittest.TestCase):
    def test_send_to_email(self):

        for i in range(0, 10):
            with self.subTest(i=i):
                notification = Notification('test' + str(i), 'email' + str(i))
                self.assertEqual('Отправлена на почту: email' + str(i),
                                 notification.send_notification())

    def test_send_to_whatsup(self):

        for i in range(0, 10):
            with self.subTest(i=i):
                notification = Notification('test' + str(i), 'email' + str(i))
                notification_whats_up = SendToWhatsUp(notification, 'nickname' + str(i))
                self.assertEqual('Отправлена на WhatsUp: nickname' + str(i),
                                 notification_whats_up.send_notification())

    def test_send_to_slack(self):

        for i in range(0, 10):
            with self.subTest(i=i):
                notification = Notification('test' + str(i), 'email' + str(i))
                notification_whats_up = SendToWhatsUp(notification, 'nickname' + str(i))
                notification_slack = SendToSlack(notification_whats_up, 'nickname' + str(i))
                self.assertEqual('Отправлена на Slack: nickname' + str(i),
                                 notification_slack.send_notification())


    def test_notify_all_users(self):
        client1 = Client('434f@dsf', ['Slack', 'Telegram'], 'client1')
        client2 = Client('fdsafd@dsf', ['WhatsUp', 'VK'], 'client2')
        client3 = Client('fdsjreio3432i@dsf', ['WhatsUp', 'VK', 'Slack'], 'client3')

        clients = list()
        clients.append(client1)
        clients.append(client2)
        clients.append(client3)
        notifay_all(create_notifaers(clients))


if __name__ == '__main__':
    unittest.main()