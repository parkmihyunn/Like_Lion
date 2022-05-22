//Spread

const me = {
    name : "박미현",
    age : 24,
};

const militaryMe = {
    ...me,
    militaryState: false,
};

const animals = ["개", "고양이"];
const anotherAnimals = [...animals, "호랑이", "곰"];

console.log(militaryMe);
console.log(anotherAnimals);
