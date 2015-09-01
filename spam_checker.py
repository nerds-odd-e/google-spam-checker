import gmail_client
import argparse
import sys

parser = argparse.ArgumentParser(description='Spam Checker')
parser.add_argument('--username', dest="username",
                           help='gmail username, e.g. my.mail@gmail.com')
parser.add_argument('--password', dest="password",
                           help='gmail password')
parser.add_argument('--subject', dest="subject",
                           help='the key to find the subject the email just sent (by another programmer, or you sent it manually.)')


class GmailSpamChecker:
    def __init__(self, gmail, subject):
        self.gmail = gmail
        self.subject = subject

    def check_box(self, mailbox, label, message, condition):
        emails = self.gmail.mailbox(mailbox).mail(unread=True, label=label, subject=self.subject)
        for email in emails:
            email.mark_read()
        if condition(len(emails)):
            print(message)
            return -1
        return 0


def main():
    args = parser.parse_args()
    gmail = gmail_client.login(args.username, args.password)
    checker = GmailSpamChecker(gmail, args.subject)
    exit_code = sum(checker.check_box(mb, l, msg, c) for mb, l, msg, c in [
        ["INBOX", "^smartlabel_promo", "ERROR: The email is marked as promotion.", lambda x:x>0],
        ["INBOX", "", "ERROR: No email received in the inbox.", lambda x:x==0],
        ["[Gmail]/Spam", "", "ERROR: The email has been marked as Spam!!!", lambda x:x>0],
        ])
    gmail.logout()
    sys.exit(exit_code)
