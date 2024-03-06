// var a =5;
// var fact =1
// for(let i =1;i<=a;i++){
//     fact=fact*i
// }
// console.log(fact)

// 153, it's an Armstrong number because 1^3 + 5^3 + 3^3 equals 153.
// 1634      1253

// user = prompt("enter 4 digit number");
// len=user.length;
// console.log(len)
// answer=1;
// armstrong=0;
// for(let i =0;i<user.length;i++){
//     answer = user[i]**len;
//     armstrong=armstrong+answer;
// }
// console.log(armstrong)
// if(user==armstrong){
// console.log("The number is armstrong");
// }
// else{
//     console.log("The number is not armstrong");
// }

// nationality = prompt("enter your nationality");
// nationality =nationality.charAt(0).toUpperCase()+nationality.slice(1);
// console.log(nationality)
// age=prompt("enter your age:")
// if (age>=18 && nationality=="Indian"){
//     console.log("you are eligible for voting")
// }else{
//     console.log("you are not eligible")
// }
console.log("amaan")
const from = document.getElementById('from');
const to = document.getElementById('to');
const amount = document.getElementById('amount');
const result = document.getElementById('result');
const convert = document.getElementById('convert');
convert.addEventListener("click", function(){
    let fromCurrency = from.value;
    let toCurrency = to.value;
     let amt = amount.value;
     fetch(`https://api.exchangerate-api.com/v4/latest/${fromCurrency}`)
     .then(res=>res.json())
     .then(data=>{
        let rate = data.rates[toCurrency];
        let total = rate*amt;
        result.innerHTML="total: "+total;
        console.log(total);
})
})
//  const fromCurrency='USD';
// fetch(`https://v6.exchangerate-api.com/v6/1d2c499c07b7916c9a3bceed/latest/${fromCurrency}`)
// .then(res=>res.json())
// .then(json=>console.log(json))