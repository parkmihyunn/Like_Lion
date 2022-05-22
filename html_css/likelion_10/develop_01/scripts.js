const box = document.querySelectorAll('td');

const onBoxClick = (e) => {
    if ((e.target.className !== "box-edit") && e.target.className !== "input-text") {
        e.target.className = "box-edit";
        e.target.innerHTML = `<input class="input-text" type="text" onkeydown="Enter(this)" 
        value="${e.target.innerHTML}"/>`;
    }
    else if(e.target.className != "input-text"){
        let num1 = Math.floor(Math.random() * 256);
        let num2 = Math.floor(Math.random() * 256);
        let num3 = Math.floor(Math.random() * 256);
        e.target.style.backgroundColor = "rgb(" + num1 + "," + num2 + "," + num3 + ", 0.3)";
    }
};

const Enter = (e) => {
    if (event.keyCode == 13) {
    e.parentNode.className = "box";
    e.parentNode.innerHTML = e.value;
    } 
};

box.forEach((target) => target.addEventListener("click", onBoxClick));