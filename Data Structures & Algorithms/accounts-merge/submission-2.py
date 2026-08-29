class DSU: 
    def __init__(self, cap):
        self.cap = cap
        self.arr = [i for i in range(cap)] 
    
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b: 
            self.arr[parent_b] = parent_a

    def find(self, a): 
        child = a
        parent = self.arr[a]
        while(parent != child):
            child = parent 
            parent = self.arr[child]
        return parent
            
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        mail_account = dict() 

        dsu = DSU(len(accounts))

        for i, l in enumerate(accounts):
            account = l[0]
            for mail in l[1:]:
                if mail in mail_account:
                    dsu.union(i, mail_account[mail])
                else: 
                    mail_account[mail] = i 
        
        res = dict()

        for mail, account in mail_account.items():
            root = dsu.find(account)
            
            if root not in res:
                res[root] = []
            res[root].append(mail)
        
        result = []
        for root, emails in res.items():
            emails.sort()
            result.append([accounts[root][0]] + emails)
        
        return result




        
        