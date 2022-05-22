//Rest

const me = {
    name : "박미현",
    age : 24,
    militaryState: false,
};

const {militaryState, ...another} = me;

console.log(another);

const numbers = [1, 2, 3, 4, 5, 6];

const [zero, ...rest] = numbers;

console.log(rest);