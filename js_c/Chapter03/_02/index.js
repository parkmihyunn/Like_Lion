const me = {
    name : "박미현",
    age : 24,
    gender: 'female'
};

const someone = {
    name : "김아무개",
    age : 26,
    gender: 'male'
};

function addMilitaryStateIfMale(person){
    if(person.gender === 'male'){
        person.militaryState = false;
    }
}

addMilitaryStateIfMale(me);
addMilitaryStateIfMale(someone);

function parseBoolean(value){
    if(value === true){
        return "참";
    } else if (value === false){
        return "거짓";
    }
}

// if(me.militaryState !== undefined){
//     console.log(parseBoolean(me.militaryState));
// } 아래와 동일한 의미
me.militaryState !== undefined && console.log(parseBoolean(me.militaryState));

someone.militaryState !== undefined && console.log(parseBoolean(someone.militaryState));