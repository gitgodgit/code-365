def numUniqueEmails(emails: list[str]) -> int:
    set_of_emails = set()
    for email in emails:
        current_real = ""
        for i in range(email.find('@')):
            if email[i] == '.':
                continue
            elif email[i] == '+':
                break
            else:
                current_real += email[i]
        current_real += email[email.find('@')::]
        set_of_emails.add(current_real)
    return len(set_of_emails)
            
            
