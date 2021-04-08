import sumNumbers from '../example.js'

it('sums numbers', () => {
  expect(sumNumbers(1, 2)).toEqual(3)
  expect(sumNumbers(2, 2)).toEqual(4)
})
