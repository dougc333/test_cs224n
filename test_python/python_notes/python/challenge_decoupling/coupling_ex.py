

def checkEmailSecurity(e: email):
    if e.header.bearer.invalid():
        raise Exception("invalid email")
    elif e.header.received != email.header.received_spf:
        raise Exception("header mismatch")
    else:
        print("email headder secure")
