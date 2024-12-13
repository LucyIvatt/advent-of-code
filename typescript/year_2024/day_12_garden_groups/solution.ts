import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { runPuzzle } from '../../utils/runPuzzle';
import { Coord, DIAGONAL_DIRECTIONS, Direction, Grid, rotate, STRAIGHT_DIRECTIONS } from '../../utils/grid';

class Region {
  plantType: string;
  startLocation: Coord;
  locations: Coord[] = [];
  perimeter: number = 0;
  corners: number = 0;

  constructor(plantType: string, startLocation: Coord) {
    this.plantType = plantType;
    this.startLocation = startLocation;
    this.locations.push(startLocation);
  }

  getArea = () => this.locations.length;
  getFencePrice = () => this.getArea() * this.perimeter;
  getDiscountPrice = () => this.getArea() * this.corners;
}

// Rotate directions by 45 degrees and find the common direction
const getDiagonalDirectionForLShape = (directions: Direction[]): Direction => {
  const [dir1, dir2] = directions;
  const diagonals1 = [rotate(dir1, 45), rotate(dir1, -45)];
  const diagonals2 = [rotate(dir2, 45), rotate(dir2, -45)];

  return diagonals1.find((d) => diagonals2.includes(d))!;
};

// Finds middle direction for T shape and provides diagonal directions 45 degrees either side of it
const getDiagonalDirectionsForTShape = (directions: Direction[]): Direction[] => {
  const middle = directions.find(
    (dir) => directions.includes(rotate(dir, 90)) && directions.includes(rotate(dir, -90))
  )!;

  return [rotate(middle, 45), rotate(middle, -45)];
};

const coordEquals = (a: Coord, b: Coord): boolean => a[0] === b[0] && a[1] === b[1];
const coordInList = (coord: Coord, list: Coord[]): boolean => list.some((c) => coordEquals(c, coord));

const findOpenSides = (i: number, j: number, grid: Grid<string>, region: Region) => {
  const openSides: Coord[] = [];
  const plantType = grid.array[i][j];
  const openDirections: Direction[] = [];
  let perimeter = 0;
  let corners = 0;

  for (const direction of STRAIGHT_DIRECTIONS) {
    try {
      const { value, position } = grid.getAdjacent(i, j, direction);

      if (value !== plantType) perimeter += 1;
      else {
        if (!region.locations.some((coord) => coordEquals(coord, position))) openSides.push(position);
        openDirections.push(direction);
      }
    } catch {
      perimeter += 1;
    }
  }

  switch (openDirections.length) {
    case 0:
      corners = 4;
      break;
    case 1:
      corners = 2;
      break;

    case 2:
      if (openDirections[0] !== rotate(openDirections[1], 180)) {
        const diagonal = getDiagonalDirectionForLShape(openDirections);
        try {
          const { value } = grid.getAdjacent(i, j, diagonal);
          if (value === plantType)
            corners = 1; // valid position directly diagonal from L shape corner (no addtional corner needed)
          else corners = 2; // corner direction diagonal from L shape corner
        } catch {
          corners = 2; // corner direction diagonal from L shape corner
        }
      }
      break;
    case 3: {
      const diagonalDirections = getDiagonalDirectionsForTShape(openDirections);
      const invalidDiags = diagonalDirections.filter((direction) => {
        try {
          const { value } = grid.getAdjacent(i, j, direction);
          return value !== plantType;
        } catch {
          return true;
        }
      }).length;
      corners = invalidDiags;
      break;
    }
    case 4:
      corners = DIAGONAL_DIRECTIONS.filter((direction) => {
        try {
          const { value } = grid.getAdjacent(i, j, direction);
          return value !== plantType;
        } catch {
          return true;
        }
      }).length;
      break;
  }

  return { openSides, perimeter, corners };
};
const findRegions = (plants: Grid<string>) => {
  const processedCoords: Coord[] = [];
  const regions: Region[] = [];

  plants.array.forEach((line, i) => {
    line.forEach((plant, j) => {
      if (!coordInList([i, j], processedCoords)) {
        const region = new Region(plant, [i, j]);
        regions.push(region);

        const coordsToProcess: Coord[] = [[i, j]];
        processedCoords.push([i, j]);

        while (coordsToProcess.length > 0) {
          const coordToProcess = coordsToProcess.shift()!;

          const { openSides, perimeter, corners } = findOpenSides(coordToProcess[0], coordToProcess[1], plants, region);

          region.perimeter += perimeter;
          region.corners += corners;
          region.locations.push(...openSides);
          coordsToProcess.push(...openSides);
          processedCoords.push(coordToProcess);
        }
      }
    });
  });
  return regions;
};

export const partOne = (puzzleInput: string[]) => {
  return findRegions(new Grid(puzzleInput.map((row) => row.split(''))))
    .reduce((acc, region) => acc + region.getFencePrice(), 0)
    .toString();
};

export const partTwo = (puzzleInput: string[]) => {
  return findRegions(new Grid(puzzleInput.map((row) => row.split(''))))
    .reduce((acc, region) => acc + region.getDiscountPrice(), 0)
    .toString();
};

if (require.main === module) {
  const puzzleInput = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));
  runPuzzle('12', 'garden_groups', partOne, partTwo, puzzleInput);
}