class Evaluator:

    #  @staticmethod
    def _ceck(coefs, words):
        if len(coefs) != len(words):
            print("-1")
            exit(-1)

    #@staticmethod
    def zip_evaluate(coefs, words):
        Evaluator._ceck(coefs, words)
        resp = 0
        for c, w in zip(coefs, words):
            resp += c * len(w)
        return resp

    #@staticmethod
    def enumerate_evaluate(coefs, words):
        Evaluator._ceck(coefs, words)
        resp = 0
        for c, w in enumerate(words):
           resp += coefs[c] * len(w)
        return resp

if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))

    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words))

