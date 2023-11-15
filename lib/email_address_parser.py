import re

class EmailAddressParser:
    def __init__(self, email_addreses):
        self.email_addresses = email_addreses    
    
    def parse(self):
        if not self.email_addresses:
            return []
        
        email_list = re.split(r'[,\s]+', self.email_addresses)
        unique_emails = list(set(email_list))
        unique_emails.sort()
        new_email_list = []
        for email in unique_emails:
            if "@" in email:
                new_email_list.append(email)
        print(new_email_list)
        return new_email_list



