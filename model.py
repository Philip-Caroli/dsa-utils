import field

class Model:
    fields = []
    name = ""

    def print(self):
        out = "Model " + self.name + ": "
        for field in self.fields:
            out += field.name + ": " + field.value + ", "
        print(out)

    def get_html(self):
        out = ''