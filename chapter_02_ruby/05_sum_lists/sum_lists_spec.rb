require_relative '../node'
require_relative 'sum_lists'

RSpec.shared_examples 'sum_lists behavior' do
  context 'short input' do
    it 'adds 617 + 295 = 912' do
      l1 = from_list([7, 1, 6])
      l2 = from_list([5, 9, 2])
      expect(to_list(fn.call(l1, l2))).to eq([2, 1, 9])
    end

    it 'handles carry: 99 + 1 = 100' do
      l1 = from_list([9, 9])
      l2 = from_list([1])
      expect(to_list(fn.call(l1, l2))).to eq([0, 0, 1])
    end

    it 'adds single digits: 3 + 4 = 7' do
      l1 = from_list([3])
      l2 = from_list([4])
      expect(to_list(fn.call(l1, l2))).to eq([7])
    end

    it 'adds single digits with carry: 9 + 9 = 18' do
      l1 = from_list([9])
      l2 = from_list([9])
      expect(to_list(fn.call(l1, l2))).to eq([8, 1])
    end

    it 'handles different lengths: 100 + 99 = 199' do
      l1 = from_list([0, 0, 1])
      l2 = from_list([9, 9])
      expect(to_list(fn.call(l1, l2))).to eq([9, 9, 1])
    end

    it 'handles zeros: 0 + 0 = 0' do
      l1 = from_list([0])
      l2 = from_list([0])
      expect(to_list(fn.call(l1, l2))).to eq([0])
    end
  end

  context 'medium input' do
    it 'adds 999999999 + 1 = 1000000000' do
      l1 = from_list([9] * 9)
      l2 = from_list([1])
      expect(to_list(fn.call(l1, l2))).to eq([0] * 9 + [1])
    end

    it 'adds two 50-digit numbers of all 5s' do
      l1 = from_list([5] * 50)
      l2 = from_list([5] * 50)
      expect(to_list(fn.call(l1, l2)).length).to eq(51)
    end
  end

  context 'long input', :slow do
    it 'adds 1000-digit number of 9s + 1' do
      l1 = from_list([9] * 1000)
      l2 = from_list([1])
      expect(to_list(fn.call(l1, l2))).to eq([0] * 1000 + [1])
    end
  end
end

RSpec.describe 'sum_lists' do
  let(:fn) { method(:sum_lists) }
  include_examples 'sum_lists behavior'
end
