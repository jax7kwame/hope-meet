// current year

let currentDate = new Date();
let currentYear = currentDate.getFullYear();

const currentYearElement = document.getElementById('currentYear');

currentYearElement.textContent = currentYear;