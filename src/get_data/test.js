let charttime;
let previousOptionValue = "option1";
let previousOptionValue1 = "option1";

let chart1
var optionMenu = document.getElementById("option-menu");
var optionMenu1 = document.getElementById("option-menu1");
var optionMenu2 = document.getElementById("option-menu2");
var next = document.getElementById("next-button");
var prev = document.getElementById("prev-button");
let date;

async function handleOptionChange() {
  try {
    var selectedYear = optionMenu.value;
    date = await new Promise((resolve) => {
      setTimeout(function() {
        resolve(optionMenu1.value);
      }, 20);
    })
    path = 'test_sort/market_data_' + selectedYear + '/' + date+'/';
    // console.log(path)
    const response = await fetch(path);
    const data = await response.text();
    var parser = new DOMParser();
    var doc = parser.parseFromString(data, 'text/html');
    var fileLinks = doc.querySelectorAll('#files .name');
    ce_name = [];
    
    fileLinks.forEach(function (link) {
      var filename = link.textContent.trim();
      var name = path + "/" + filename;
      // console.log(filename);
      if (filename.includes("CE")) {
        ce_name.push(name);
      } else if (filename.includes("PE")) {
        PEFunction(name);
      } else if (filename.includes("-I")) {
        futFunction(name);
      } else if (filename.includes("BANKNIFTY") && !filename.includes("ce") && !filename.includes("pe") && !filename.includes("-I")) {
        indexFunction(name); // Call indexFunction only when "banknifty" is present and other substrings are not present.
      }
    });

    reverse_ce = ce_name.reverse();
    for (const ceFileName of reverse_ce) {
      await CEFunction(ceFileName);
    }

    // Now that all the asynchronous operations are completed, call setValue()
    setvalue();
    
  } catch (error) {
    console.error('Error:', error);
  }
}


optionMenu.addEventListener("change", handleOptionChange);
optionMenu1.addEventListener("change", handleOptionChange);
optionMenu2.addEventListener("change", handleOptionChange);
next.addEventListener("click", handleOptionChange);
prev.addEventListener("click", handleOptionChange);

// Function to handle arrow key presses
function handleArrowKeyPress(event) {
  const button = document.getElementById("myButton");

  // Check if the pressed key is an arrow key
  if (event.key === "ArrowLeft" || event.key === "ArrowUp"   ) {
    // Trigger a click event on the button
    console.log("hiii");
    event.preventDefault();

    prev.click();
  }else if (event.key == "ArrowRight" || event.key === "ArrowDown" ) {
    // Trigger a click event on the button
    next.click();
    event.preventDefault();

  }
}
document.addEventListener("keydown", handleArrowKeyPress);


setTimeout(handleOptionChange, 70);