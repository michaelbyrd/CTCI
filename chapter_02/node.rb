# Shared Node class for Chapter 2 — Linked Lists

Node = Struct.new(:val, :next)

def to_list(node)
  result = []
  while node
    result << node.val
    node = node.next
  end
  result
end

def from_list(values)
  return nil if values.empty?
  head = Node.new(values[0])
  current = head
  values[1..].each do |val|
    current.next = Node.new(val)
    current = current.next
  end
  head
end

def list_length(node)
  count = 0
  while node
    count += 1
    node = node.next
  end
  count
end
