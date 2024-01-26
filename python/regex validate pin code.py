# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot
# contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    tam = len(pin)
    if tam != 4 and tam != 6 or pin.isnumeric() == False:
        return False
    return True