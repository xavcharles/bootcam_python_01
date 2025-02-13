class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return -1
        zipp = list(zip(coefs, words))
        res = sum(zipp[i][0] * len(zipp[i][1]) for i in range(len(coefs)))
        return res
    
    def enumerate_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return -1
        enum = enumerate(words)
        res = sum(coefs[i] * len(val) for i, val in enum)
        return res