#!/usr/bin/node

const num = process.argv[2]; // Get the first command-line argument

// Check if the argument can be converted to an integer
if (Number.isInteger(parseInt(num))) {
  console.log('My number:', parseInt(num));
} else {
  console.log('Not a number');
}
