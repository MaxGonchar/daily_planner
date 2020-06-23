import pickle


def db_write(data):
    """"""
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)


def db_read():
    """"""
    with open('data.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
