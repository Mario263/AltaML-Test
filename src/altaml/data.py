class Data:
    def __init__(self, database):
        print("Connecting to database")
        
    def beginTran(self):
        print("Beginning a transaction")
        
    def commit(self):
        print("Committing transaction")
        
    def rollback(self):
        print("Rolling back transaction")
        
    def insert(self, table, object):
        print("Inserting {0} into table {1}".format(object.getName(), table))