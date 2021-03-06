let quotes = [
  {
    quote: "Apis mellifera",
    explain: "- latinsky názov včely medonosnej",
    id: 0
  },
  {
    quote: "Propolis",
    explain: "- včelie lepidlo živicového pôvodu s antibakteriálnymi účinkami",
    id: 1
  },
  {
    quote: "Zavíjač voskový",
    explain: "- húsenice tohto motýľa sa živia včelím dielom",
    id: 2
  },
  {
    quote: "Medový vačok",
    explain: "- priestor do ktorého včela ukladá nektár",
    id: 3
  },
  {
    quote: "Nektár",
    explain: "- vodný roztok cukrov a minerálov, ktorý včeli zbierajú a premieňajú na med",
    id: 4
  },
  {
    quote: "Roztoč Varroa",
    explain: "- včelý parazit, ktorý napáda plod a živý sa hemolymfou včiel",
    id: 5
  },
  {
    quote: "Letáč",
    explain: "- plocha pred úľovým otvorom na ktorú včely dosadajú",
    id: 6
  },
  {
    quote: "Dymák",
    explain: "- zariadenie na výrobu dymu, ktoré slúži na upokojenie a omámenie včiel",
    id: 7
  },
  {
    quote: "Lietavka",
    explain: "- robotnica ktorá vyletuje z úľa a prináša nektár, medovicu, vodu, peľ a propolis",
    id: 8
  },
  {
    quote: "Matka",
    explain: "- najväčšia a najdokonalejšie vyvynutá včela v úľi",
    id: 9
  },
  {
    quote: "Materská kašička",
    explain: "- šťava ktorá je produktom hltanových žliaz včiel kŕmičiek",
    id: 10
  },
  {
    quote: "Robotnica",
    explain: "- včela ktorá od narodenia až do smrti vykonáva najrôznejšie práce v úľi",
    id: 11
  },
  {
    quote: "Mladuška",
    explain: "- včela ktorá sa doteraz nestala lietavkou",
    id: 12
  },
  {
    quote: "Mor včelieho plodu",
    explain: "- závažné ochorenie, ktoré pre ľudí nieje nebezpečné",
    id: 13
  },
  {
    quote: "Včelí vosk",
    explain: "- výlučok voskových žliaz včiel, ktorý slúži na stavbu včelieho diela",
    id: 14
  },
  {
    quote: "Včelie dielo",
    explain: "- voskové plásty",
    id: 15
  },
  {
    quote: "Trúd",
    explain: "- včelí samček",
    id: 16
  },
  {
    quote: "Tykadlá",
    explain: "- ústroje na hlave včiel, ktoré slúžia na dorozumievanie a orientáciu v prostredí",
    id: 17
  }
];


let quoteParagraph = document.getElementById('quote');
let quoteAuthor = document.querySelector('.author');

let newQuote, newAuthor;


//i get random integer number
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

setInterval(() => {
  
  let getRandomQuote = getRandomInt(quotes.length);
  quotes.forEach(quote => {
    //set anim
    quoteParagraph.classList.add('visuallhide');
    quoteAuthor.classList.add('visuallhide');
    

    setTimeout(()=>{
      if (quote.id === getRandomQuote){
        quoteParagraph.innerText = quote.quote;
        quoteAuthor.innerHTML = quote.explain;
        //set anim
        quoteParagraph.classList.remove('visuallhide');
        quoteAuthor.classList.remove('visuallhide');
        
      }
    }, 400)
    

  });
  
}, 5000);
