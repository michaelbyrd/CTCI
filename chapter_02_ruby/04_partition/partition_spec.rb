require_relative '../node'
require_relative 'partition'

def valid_partition?(result, x)
  seen_gte = false
  result.each do |val|
    if val >= x
      seen_gte = true
    elsif seen_gte
      return false
    end
  end
  true
end

RSpec.shared_examples 'partition behavior' do
  context 'short input' do
    it 'partitions basic example' do
      result = to_list(fn.call(from_list([3, 5, 8, 5, 10, 2, 1]), 5))
      expect(valid_partition?(result, 5)).to be true
      expect(result.sort).to eq([3, 5, 8, 5, 10, 2, 1].sort)
    end

    it 'handles all values less than x' do
      result = to_list(fn.call(from_list([1, 2, 3]), 5))
      expect(valid_partition?(result, 5)).to be true
      expect(result.sort).to eq([1, 2, 3])
    end

    it 'handles all values greater than x' do
      result = to_list(fn.call(from_list([6, 7, 8]), 5))
      expect(valid_partition?(result, 5)).to be true
      expect(result.sort).to eq([6, 7, 8])
    end

    it 'handles single element less than x' do
      expect(to_list(fn.call(from_list([3]), 5))).to eq([3])
    end

    it 'handles single element equal to x' do
      expect(to_list(fn.call(from_list([5]), 5))).to eq([5])
    end

    it 'handles already partitioned list' do
      result = to_list(fn.call(from_list([1, 2, 5, 6]), 5))
      expect(valid_partition?(result, 5)).to be true
      expect(result.sort).to eq([1, 2, 5, 6])
    end
  end

  context 'medium input' do
    it 'partitions length-50 random list' do
      srand(42)
      vals = Array.new(50) { rand(1..20) }
      result = to_list(fn.call(from_list(vals), 10))
      expect(valid_partition?(result, 10)).to be true
      expect(result.sort).to eq(vals.sort)
    end

    it 'partitions length-100 reversed list' do
      vals = (1..100).to_a.reverse
      result = to_list(fn.call(from_list(vals), 50))
      expect(valid_partition?(result, 50)).to be true
      expect(result.sort).to eq(vals.sort)
    end
  end

  context 'long input', :slow do
    it 'partitions length-1000 reversed list' do
      vals = (1..1000).to_a.reverse
      result = to_list(fn.call(from_list(vals), 500))
      expect(valid_partition?(result, 500)).to be true
      expect(result.sort).to eq(vals.sort)
    end
  end
end

RSpec.describe 'partition' do
  let(:fn) { method(:partition) }
  include_examples 'partition behavior'
end
