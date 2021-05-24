
class Exceptions(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self, message)

class AllFieldsMustBeFilled(Exceptions):
    def __init__(self, message='Todos os campos precisam ser preenchidos'):
        self.message = message
        self.code = 400
        super(AllFieldsMustBeFilled, self).__init__(self.message, self.code)

class EmpregadoNotFound(Exceptions):
    def __init__(self, message='Empregado não localizado'):
        self.message = message
        self.code = 404
        super(EmpregadoNotFound, self).__init__(self.message, self.code)


