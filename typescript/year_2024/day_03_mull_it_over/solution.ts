import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';

type RegexMatch = { match: string; index: number; groups: number[] };

// Matches "mul(x, y)" where x and y are 1-3 digit numbers
const MUL_REGEX = /mul\((\d{1,3}),(\d{1,3})\)/g;

// Matches "do()" or "don't()"
const COND_REGEX = /do\(\)|don't\(\)/g;

const findMatches = (input: string, regex: RegExp): RegexMatch[] => {
  return [...input.matchAll(regex)].map((match) => ({
    match: match[0],
    index: match.index ?? -1,
    groups: match.slice(1).map(Number)
  }));
};

export const partOne = (puzzleInput: string[]) => {
  const instructions = puzzleInput.join('');
  const result = findMatches(instructions, MUL_REGEX).reduce((acc, { groups: [a, b] }) => (acc += a * b), 0);
  return result.toString();
};

export const partTwo = (puzzleInput: string[]) => {
  const instructions = puzzleInput.join('');

  const multiplications = findMatches(instructions, MUL_REGEX);
  const conditions = findMatches(instructions, COND_REGEX);

  let conditionPointer = 0;

  const result = multiplications.reduce((sum, { groups: [a, b], index }) => {
    while (conditionPointer < conditions.length && conditions[conditionPointer].index < index) {
      conditionPointer++;
    }
    const condition = conditions[conditionPointer - 1];

    if (!condition || condition.match === 'do()') {
      sum += a * b;
    }
    return sum;
  }, 0);

  return result.toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE_2));
  runPuzzle('03', 'mull_it_over', partOne, partTwo, puzzleInput);
}

// 0.000972 seconds without pointer
// 0.000320 seconds with pointer
