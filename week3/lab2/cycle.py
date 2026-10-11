def hasCycle(self, head: Optional[ListNode], visited_nodes = None) -> bool:
        visited_nodes = set() if not visited_nodes else visited_nodes

        if head is None:
            return False

        if head in visited_nodes:
            return True
        else:
            visited_nodes.add(head)
            return self.hasCycle(head.next, visited_nodes)