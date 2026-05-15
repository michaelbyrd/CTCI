require_relative '../node'
require_relative 'return_kth_to_last'

RSpec.shared_examples 'return_kth_to_last behavior' do
  context 'short input (length 0-9)' do
    it 'returns last element (k=1)' do
      expect(fn.call(from_list([1, 2, 3, 4, 5]), 1)).to eq(5)
    end

    it 'returns second to last (k=2)' do
      expect(fn.call(from_list([1, 2, 3, 4, 5]), 2)).to eq(4)
    end

    it 'returns third to last (k=3)' do
      expect(fn.call(from_list([1, 2, 3, 4, 5]), 3)).to eq(3)
    end

    it 'returns first element (k=length)' do
      expect(fn.call(from_list([1, 2, 3, 4, 5]), 5)).to eq(1)
    end

    it 'handles single element list' do
      expect(fn.call(from_list([7]), 1)).to eq(7)
    end

    it 'handles two element list' do
      expect(fn.call(from_list([1, 2]), 2)).to eq(1)
    end
  end

  context 'medium input (length 10-99)' do
    it 'returns last element of length-50 list' do
      vals = (0...50).to_a
      expect(fn.call(from_list(vals), 1)).to eq(49)
    end

    it 'returns middle element of length-50 list' do
      vals = (0...50).to_a
      expect(fn.call(from_list(vals), 25)).to eq(24)
    end

    it 'returns first element of length-50 list' do
      vals = (0...50).to_a
      expect(fn.call(from_list(vals), 50)).to eq(0)
    end
  end

  context 'long input (length 100+)', :slow do
    it 'returns last element of length-1000 list' do
      vals = (0...1000).to_a
      expect(fn.call(from_list(vals), 1)).to eq(999)
    end

    it 'returns middle element of length-1000 list' do
      vals = (0...1000).to_a
      expect(fn.call(from_list(vals), 500)).to eq(499)
    end
  end
end

%i[return_kth_to_last_two_pass return_kth_to_last_two_pointers].each do |fn_name|
  RSpec.describe fn_name.to_s do
    let(:fn) { method(fn_name) }
    include_examples 'return_kth_to_last behavior'
  end
end
