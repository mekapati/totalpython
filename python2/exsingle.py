def is_circular_linked_list(self, input_list):
        curr=input_list.head
        if not input_list.head:
            return False
        elif curr.next == input_list.head:
            return True
        else:            
            while(curr):
                curr=curr.next;
                if curr == input_list.head:
                    return True
        return False