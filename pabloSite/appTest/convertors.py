class ABConvertor:
    regex = "[0-9]{1,20}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)