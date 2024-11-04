let xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        let data = this.responseText.split('\n');
        let randomIndex = Math.floor(Math.random() * data.length);
        let randomString = data[randomIndex];
        document.getElementById('random-string').textContent = randomString;
    }
};
xhr.open('GET', 'towns.csv', true);
xhr.send();