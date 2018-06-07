class NetworkError(RuntimeError):
    def __init__(self, arg) :
        self.args =arg

try:
    raise NetworkError("Bad hostname")
except NetworkError as e:
    print(e.args)


