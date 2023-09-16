class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
 
        prev, curr = head, head.next
        toInsert = False

        while True:
            
            if prev.val <= insertVal <= curr.val:
                # Case #1. The value of new node sits between the minimal and maximal values of the current list. 
                # As a result, it should be inserted within the list.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. The value of new node goes beyond the minimal and maximal values of the current list, 
                # either less than the minimal value or greater than the maximal value. 
                # In either case, the new node should be added right after the tail node
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break
        # Case #3. all elements in loop larger or smaller than inser val, insert any where woudl be good.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head