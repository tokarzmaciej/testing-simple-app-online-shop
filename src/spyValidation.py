class SpyValidationEmail(object):
    def __init__(self, status=True):
        self.accept_email = status
        self.check_email = []

    def validEmail(self, email):
        self.check_email.append(email)
        return self.accept_email
