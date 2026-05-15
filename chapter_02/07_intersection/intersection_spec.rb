require_relative '../node'
require_relative 'intersection'

def make_intersecting(a_vals, b_vals, shared_vals)
  shared = from_list(shared_vals)

  head_a = a_vals.empty? ? shared : from_list(a_vals)
  unless a_vals.empty?
    node = head_a
    node = node.next while node.next
    node.next = shared
  end

  head_b = b_vals.empty? ? shared : from_list(b_vals)
  unless b_vals.empty?
    node = head_b
    node = node.next while node.next
    node.next = shared
  end

  [head_a, head_b, shared]
end

RSpec.shared_examples 'intersection behavior' do
  context 'short input' do
    it 'finds the intersecting node' do
      a, b, shared = make_intersecting([1, 2, 3], [4, 5], [7, 8])
      expect(fn.call(a, b)).to be(shared)
    end

    it 'returns nil for no intersection' do
      a = from_list([1, 2, 3])
      b = from_list([4, 5, 6])
      expect(fn.call(a, b)).to be_nil
    end

    it 'returns head when both lists are the same object' do
      a = from_list([1, 2, 3])
      expect(fn.call(a, a)).to be(a)
    end

    it 'returns the shared node when both point to it' do
      shared = Node.new(1)
      expect(fn.call(shared, shared)).to be(shared)
    end

    it 'handles different-length lists that intersect' do
      a, b, shared = make_intersecting([1, 2, 3, 4], [5], [6, 7])
      expect(fn.call(a, b)).to be(shared)
    end

    it 'returns nil for two nil lists' do
      expect(fn.call(nil, nil)).to be_nil
    end

    it 'returns nil when one list is nil' do
      a = from_list([1, 2, 3])
      expect(fn.call(a, nil)).to be_nil
    end
  end

  context 'medium input' do
    it 'finds intersection in long lists' do
      a, b, shared = make_intersecting((0...25).to_a, (25...50).to_a, (50...75).to_a)
      expect(fn.call(a, b)).to be(shared)
    end

    it 'returns nil for two non-intersecting long lists' do
      a = from_list((0...50).to_a)
      b = from_list((50...100).to_a)
      expect(fn.call(a, b)).to be_nil
    end
  end

  context 'long input', :slow do
    it 'finds intersection in 1000-node lists' do
      a, b, shared = make_intersecting((0...500).to_a, (500...750).to_a, (750...1000).to_a)
      expect(fn.call(a, b)).to be(shared)
    end
  end
end

RSpec.describe 'intersection' do
  let(:fn) { method(:intersection) }
  include_examples 'intersection behavior'
end
