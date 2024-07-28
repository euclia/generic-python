from base64 import b64decode
import pickle


def decode(rawModel):
    print('decoding')
    model = b64decode(rawModel)
    print('decoded base64')
    print('loading pickle')
    p_mod = pickle.loads(model)
    print('pickle loaded', model)
    return p_mod
    # raw = b64encode(p_mod)
    # raw_model = raw.decode(self.ENCODING)
    # ENCODING = 'utf-8'
