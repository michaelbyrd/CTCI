require_relative '../node'
require_relative 'remove_dups'

RSpec.shared_examples 'remove_dups behavior' do
  context 'short input (length 0-9)' do
    it 'handles empty list' do
      expect(to_list(fn.call(nil))).to eq([])
    end

    it 'handles single element' do
      expect(to_list(fn.call(from_list([1])))).to eq([1])
    end

    it 'handles no duplicates' do
      expect(to_list(fn.call(from_list([1, 2, 3])))).to eq([1, 2, 3])
    end

    it 'removes adjacent duplicate' do
      expect(to_list(fn.call(from_list([1, 1, 2])))).to eq([1, 2])
    end

    it 'removes non-adjacent duplicates' do
      expect(to_list(fn.call(from_list([1, 2, 3, 2, 1])))).to eq([1, 2, 3])
    end

    it 'handles all same values' do
      expect(to_list(fn.call(from_list([5, 5, 5, 5])))).to eq([5])
    end

    it 'removes duplicate at end' do
      expect(to_list(fn.call(from_list([1, 2, 3, 3])))).to eq([1, 2, 3])
    end
  end

  context 'medium input (length 10-99)' do
    it 'handles length-20 list with no dups' do
      vals = (0...20).to_a
      expect(to_list(fn.call(from_list(vals)))).to eq(vals)
    end

    it 'handles length-20 list with dups' do
      vals = (0...10).to_a * 2
      expect(to_list(fn.call(from_list(vals)))).to eq((0...10).to_a)
    end

    it 'handles length-50 list with dups' do
      vals = (0...10).to_a * 5
      expect(to_list(fn.call(from_list(vals)))).to eq((0...10).to_a)
    end
  end

  context 'long input (length 100+)', :slow do
    it 'handles length-1000 list with dups' do
      vals = (0...100).to_a * 10
      expect(to_list(fn.call(from_list(vals)))).to eq((0...100).to_a)
    end

    it 'handles length-10000 list with dups' do
      vals = (0...100).to_a * 100
      expect(to_list(fn.call(from_list(vals)))).to eq((0...100).to_a)
    end
  end
end

%i[remove_dups remove_dups_no_buffer].each do |fn_name|
  RSpec.describe fn_name.to_s do
    let(:fn) { method(fn_name) }
    include_examples 'remove_dups behavior'
  end
end
