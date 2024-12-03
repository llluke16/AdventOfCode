const fs = require('fs');

fs.readFile('3/data.txt', 'utf8', (err, input) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }

function findMultis(match, shouldMultiply, totalSum) {
  if (!shouldMultiply) {
    return totalSum;
  }

  const regex = /mul\((\d{1,3}),(\d{1,3})\)/;
  const [, num1, num2] = regex.exec(match);
  const product = parseInt(num1, 10) * parseInt(num2, 10);
  return totalSum + product; 
}

function findDo(match) {
  return match === "do()";
}

function findDont(match) {
  return match === "don't()";
}

  const combinedRegex = /(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))/g;
  let shouldMultiply = true;
  let totalSum = 0;
  let match;

  while ((match = combinedRegex.exec(input)) !== null) {
    const currentMatch = match[0];

    if (findDont(currentMatch)) {
      shouldMultiply = false;
    } else if (findDo(currentMatch)) {
      shouldMultiply = true;
    } else if (currentMatch.startsWith("mul")) {
      totalSum = findMultis(currentMatch, shouldMultiply, totalSum);
    }
  }

  console.log(totalSum);
});