import { functionTimer } from './time';

/**
 * Runs the puzzle for a given day and logs the results for both parts.
 *
 * @param dayNum - The day number of the puzzle.
 * @param dayName - The name of the puzzle for the given day.
 * @param partOne - The function to solve part one of the puzzle. It takes an array of strings as input and returns a string as the answer.
 * @param partTwo - The function to solve part two of the puzzle. It takes an array of strings as input and returns a string as the answer.
 * @param puzzleInput - The input data for the puzzle as an array of strings.
 */
export const runPuzzle = async (
  dayNum: string,
  dayName: string,
  partOne: (input: string[]) => string | Promise<string>,
  partTwo: (input: string[]) => string | Promise<string>,
  puzzleInput: string[]
): Promise<void> => {
  const { output: p1_output, time: p1_time } = await functionTimer(partOne, puzzleInput);
  const { output: p2_output, time: p2_time } = await functionTimer(partTwo, puzzleInput);

  console.log('--------------------------------------');
  console.log(`Day ${dayNum}: ${dayName}`);
  console.log('--------------------------------------');
  console.log(`Part One Answer: ${p1_output} - [${p1_time} seconds]`);
  console.log(`Part Two Answer: ${p2_output} - [${p2_time} seconds]`);
  console.log('--------------------------------------');
};
