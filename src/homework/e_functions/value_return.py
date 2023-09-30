#
def get_hour(epoch_seconds):
    return epoch_seconds//3600

def get_minutes(epoch_seconds):
    mins = epoch_seconds//60
    mins_mod = mins % 60
    return mins_mod

def get_seconds(epoch_seconds):
    secs = (epoch_seconds%3600) % 60
    return secs

