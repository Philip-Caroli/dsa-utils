class Field:
    name = ""
    value = None
    type = None
    
    def load(self, data):
        self.name = data['name']
        self.value = data['value']
        self.type = data['type']

    def store(self):
        return {'name': self.name, 'value': self.value, 'type': self.type}

    def gen_html(self, edit=False):
        pass

    def evaluate(self, form):
        self.value = form.get(self.name)


class Text(Field):
    type = 'text'

    def gen_html(self, edit=False):
        return '''
        <h4>%s</h4><br>
        <input type="text" name="%s value="%s"">
        '''.format(self.name, self.name, self.value)

    def evaluate(self, form):
        self.value = form.get(self.name)
