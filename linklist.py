
'''
# 1, Middle of the Linked List 
# 2, Reverse Linked List - iterative, recursive

'''


# 1, Middle of the Linked List 
def middleNode(head):
	tmp = head
	while tmp and tmp.next:
		head = head.next
		tmp = tmp.next.next
	return head

	# set two pointers, one is head with one step each iteration 
	# the other is tmp, with two steps each iteration 
	# when tmp reach the end, head just reaches the half of it 

def middleNode01(head):
	if head == None:
		return head
	if head.next == None:
		return head
	p = head
	q = head
	while q.next:
		p = p.next
		q = q.next
		if q.next != None:
			q = q.next
	return p

# 2, Reverse Linked List
def reverseList(self, head):
	prev,cur = None, head
	while cur: 
		prev,cur,cur.next = cur.nect, prev, cur
	return prev 

def reverseList01(self, head):
	prev = None
	if not head: return prev 
	cur, head.next = head.next, prev 
	return self.reverseList(curr, head)
