#!/usr/bin/node

const x = process.argv[2];

if (Number.isInteger(parseInt(x))) {
  for (let i = x; i !== 0; i--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occcurrences');
}
