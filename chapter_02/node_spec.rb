require_relative 'node'

RSpec.describe 'list_length' do
  it 'returns 0 for nil' do
    expect(list_length(nil)).to eq(0)
  end

  it 'returns 1 for single element' do
    expect(list_length(from_list([42]))).to eq(1)
  end

  it 'returns correct length for short list' do
    expect(list_length(from_list([1, 2, 3, 4, 5]))).to eq(5)
  end

  it 'returns correct length for medium list' do
    expect(list_length(from_list((0...50).to_a))).to eq(50)
  end

  it 'returns correct length for long list' do
    expect(list_length(from_list((0...1000).to_a))).to eq(1000)
  end
end
