class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        count = 0
        for c, w in zip(coefs, words):
            count += len(w) * c
        return count

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        count = 0
        for idxc, c in enumerate(coefs):
            for idxw, w in enumerate(words):
                if (idxc == idxw):
                    count += len(w) * c
        return count

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))