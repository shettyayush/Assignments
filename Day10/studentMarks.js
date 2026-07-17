let marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 49];

let passed = 0;
let failed = 0;

let highest = marks[0];
let lowest = marks[0];
let highestStudent = 1;
let lowestStudent = 1;

for (let i = 0; i < marks.length; i++) {
    if (marks[i] >= 50) {
        console.log(`Student ${i + 1}: ${marks[i]} - Pass`);
        passed++;
    } else {
        console.log(`Student ${i + 1}: ${marks[i]} - Fail`);
        failed++;
    }

    if (marks[i] > highest) {
        highest = marks[i];
        highestStudent = i + 1;
    }

    if (marks[i] < lowest) {
        lowest = marks[i];
        lowestStudent = i + 1;
    }
}

console.log("========================");
console.log(`Total Passed: ${passed}`);
console.log(`Total Failed: ${failed}`);
console.log(`Highest Score: ${highest} (Student ${highestStudent})`);
console.log(`Lowest Score: ${lowest} (Student ${lowestStudent})`);