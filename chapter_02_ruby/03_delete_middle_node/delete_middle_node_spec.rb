require_relative '../node'
require_relative 'delete_middle_node'

def get_node(head, index)
  index.times { head = head.next }
  head
end

RSpec.shared_examples 'delete_middle_node behavior' do
  context 'short input' do
    it 'deletes middle of three' do
      head = from_list([1, 2, 3])
      fn.call(get_node(head, 1))
      expect(to_list(head)).to eq([1, 3])
    end

    it 'deletes second node of five' do
      head = from_list([1, 2, 3, 4, 5])
      fn.call(get_node(head, 1))
      expect(to_list(head)).to eq([1, 3, 4, 5])
    end

    it 'deletes third node of five' do
      head = from_list([1, 2, 3, 4, 5])
      fn.call(get_node(head, 2))
      expect(to_list(head)).to eq([1, 2, 4, 5])
    end

    it 'deletes fourth node of five' do
      head = from_list([1, 2, 3, 4, 5])
      fn.call(get_node(head, 3))
      expect(to_list(head)).to eq([1, 2, 3, 5])
    end

    it 'works with non-integer values' do
      head = from_list(['a', 'b', 'c', 'd', 'e'])
      fn.call(get_node(head, 2))
      expect(to_list(head)).to eq(['a', 'b', 'd', 'e'])
    end
  end

  context 'medium input' do
    it 'deletes middle node of length-50 list' do
      vals = (0...50).to_a
      head = from_list(vals)
      fn.call(get_node(head, 25))
      expect(to_list(head)).to eq(vals[0...25] + vals[26..])
    end

    it 'deletes near-end node of length-50 list' do
      vals = (0...50).to_a
      head = from_list(vals)
      fn.call(get_node(head, 48))
      expect(to_list(head)).to eq(vals[0...48] + vals[49..])
    end
  end

  context 'long input', :slow do
    it 'deletes middle node of length-1000 list' do
      vals = (0...1000).to_a
      head = from_list(vals)
      fn.call(get_node(head, 500))
      expect(to_list(head)).to eq(vals[0...500] + vals[501..])
    end
  end
end

RSpec.describe 'delete_middle_node' do
  let(:fn) { method(:delete_middle_node) }
  include_examples 'delete_middle_node behavior'
end
