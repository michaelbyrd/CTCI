require_relative '../node'
require_relative 'loop_detection'

def make_loop(before_loop, loop_vals, loop_start_index = 0)
  nodes = (before_loop + loop_vals).map { |v| Node.new(v) }
  nodes.each_cons(2) { |a, b| a.next = b }
  loop_start = nodes[before_loop.length + loop_start_index]
  nodes.last.next = loop_start
  [nodes.first, loop_start]
end

RSpec.shared_examples 'loop_detection behavior' do
  context 'short input' do
    it 'detects loop starting at head' do
      head, loop_start = make_loop([], [1, 2, 3, 4, 5])
      expect(fn.call(head)).to be(loop_start)
    end

    it 'detects loop after a prefix' do
      head, loop_start = make_loop([1, 2], [3, 4, 5])
      expect(fn.call(head)).to be(loop_start)
    end

    it 'detects self-loop (single node)' do
      node = Node.new(1)
      node.next = node
      expect(fn.call(node)).to be(node)
    end

    it 'detects single-node loop after prefix' do
      head, loop_start = make_loop([1, 2, 3], [4])
      expect(fn.call(head)).to be(loop_start)
    end

    it 'returns nil for list with no loop' do
      node = Node.new(1)
      node.next = Node.new(2)
      node.next.next = Node.new(3)
      expect(fn.call(node)).to be_nil
    end
  end

  context 'medium input' do
    it 'detects loop with long prefix and short loop' do
      head, loop_start = make_loop((0...50).to_a, (50...60).to_a)
      expect(fn.call(head)).to be(loop_start)
    end

    it 'detects loop with short prefix and long loop' do
      head, loop_start = make_loop((0...5).to_a, (5...55).to_a)
      expect(fn.call(head)).to be(loop_start)
    end
  end

  context 'long input', :slow do
    it 'detects loop in 1000-node list' do
      head, loop_start = make_loop((0...500).to_a, (500...1000).to_a)
      expect(fn.call(head)).to be(loop_start)
    end

    it 'returns nil for 1000-node list with no loop' do
      nodes = (0...1000).map { |i| Node.new(i) }
      nodes.each_cons(2) { |a, b| a.next = b }
      expect(fn.call(nodes.first)).to be_nil
    end
  end
end

RSpec.describe 'loop_detection' do
  let(:fn) { method(:loop_detection) }
  include_examples 'loop_detection behavior'
end
