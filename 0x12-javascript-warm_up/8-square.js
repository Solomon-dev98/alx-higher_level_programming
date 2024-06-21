#!/usr/bin/node

const num = process.argv[2];

const size = parseInt(num);

if (!isNaN(size) && Number.isInteger(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else if (size < 0) {
// do nothing if size is negative
} else {
  console.log('Missing size');
}
