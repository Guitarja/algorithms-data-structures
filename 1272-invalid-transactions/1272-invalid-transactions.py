class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        r = {}
                
        inv = []        
        for i in transactions:
            split = i.split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            if time not in r:
                r[time] = {
                    name: set([city]) # use set instead of list
                }
            else:
                if name not in r[time]:
                    r[time][name]=set([city]) # use set instead of list
                else:
                    r[time][name].add(city)
                    
        
        for i in transactions:
            split = i.split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            
            if amount > 1000:
                inv.append(i)
                continue
            
            for j in range(time-60, time+61):
                if j not in r:
                    continue
                if name not in r[j]:
                    continue
                if len(r[j][name]) > 1 or (next(iter(r[j][name])) != city): # check if larger than 2 or the only one is differ
                    inv.append(i)
                    break
                                        
        return inv 

# time and space n