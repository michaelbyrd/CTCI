require_relative '../node'
require_relative 'palindrome'

RSpec.shared_examples 'palindrome behavior' do
  context 'short input' do
    it 'single element is a palindrome' do
      expect(fn.call(from_list([1]))).to be true
    end

    it 'two same elements is a palindrome' do
      expect(fn.call(from_list([1, 1]))).to be true
    end

    it 'two different elements is not a palindrome' do
      expect(fn.call(from_list([1, 2]))).to be false
    end

    it 'odd-length palindrome' do
      expect(fn.call(from_list([1, 2, 1]))).to be true
    end

    it 'odd-length non-palindrome' do
      expect(fn.call(from_list([1, 2, 3]))).to be false
    end

    it 'even-length palindrome' do
      expect(fn.call(from_list([1, 2, 2, 1]))).to be true
    end

    it 'even-length non-palindrome' do
      expect(fn.call(from_list([1, 2, 3, 4]))).to be false
    end

    it 'longer palindrome' do
      expect(fn.call(from_list([1, 2, 3, 2, 1]))).to be true
    end

    it 'longer non-palindrome' do
      expect(fn.call(from_list([1, 2, 3, 4, 5]))).to be false
    end
  end

  context 'medium input' do
    it 'length-50 palindrome' do
      vals = (0...25).to_a + (0...25).to_a.reverse
      expect(fn.call(from_list(vals))).to be true
    end

    it 'length-50 non-palindrome' do
      expect(fn.call(from_list((0...50).to_a))).to be false
    end

    it 'length-100 palindrome' do
      vals = (0...50).to_a + (0...50).to_a.reverse
      expect(fn.call(from_list(vals))).to be true
    end
  end

  context 'long input', :slow do
    it 'length-1000 palindrome' do
      vals = (0...500).to_a + (0...500).to_a.reverse
      expect(fn.call(from_list(vals))).to be true
    end

    it 'length-1000 non-palindrome' do
      expect(fn.call(from_list((0...1000).to_a))).to be false
    end

    it 'length-10000 palindrome' do
      vals = (0...5000).to_a + (0...5000).to_a.reverse
      expect(fn.call(from_list(vals))).to be true
    end
  end
end

RSpec.describe 'palindrome' do
  let(:fn) { method(:palindrome) }
  include_examples 'palindrome behavior'
end
