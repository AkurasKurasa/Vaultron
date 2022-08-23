import csv

class Storage:
    data = []
    searchacc = []

    def __init__(self, account, password, *sites):
        #assert account is str
        assert '@' in account
        #assert password is str
        #assert sites is list

        self.account = account
        self.password = password
        self.sites = sites

        Storage.data.append([self.account, self.password])
        Storage.searchacc.append([self.account, self.sites])

    @classmethod
    def mem(cls):
        with open('db.csv', 'r') as f:
            reader = csv.reader(f)
            for item in reader:
                cls(item[0], item[1], item[2:])
        cls.data = sorted(cls.data)
        cls.searchacc = sorted(cls.searchacc)
