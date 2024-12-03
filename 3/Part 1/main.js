const fs = require('fs');

fs.readFile('3/data.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }

  const regex = /mul\((\d{1,3}),(\d{1,3})\)/g;

  let match;
  let totalSum = 0;

  // Iterate
  while ((match = regex.exec(data)) !== null) {
    const num1 = parseInt(match[1], 10); // First digit set
    const num2 = parseInt(match[2], 10); // Second digit set
    const product = num1 * num2; // multi

    totalSum += product; 
  }

  console.log(`Total sum of products: ${totalSum}`);
});