//declarative function
function fooBar(param1,param2,dst){
// function body
}

//anonymous function
const fooBar = function (param1,param2,dst){
    // function body
}

// pemanggilan function
fooBar('abc',123,'etc');

//arrow function
const fooBar = (param1,param2,dst) => {
    // function body
}

// pemanggilan function
fooBar('abc',123,'etc');

//arrow function jika langsung memberikan return value
const penjumlahan = (bil1, bil2);

// setara dengan
function penjumlahan(bil1, bil2){
    return bil1 + bil2;
}

//required parameter
const halo = nama => 'Halo ${nama}!';
// halo('Umam') --> Halo Umam!

const penjumlahan = (a,b) => a+b;
// penjumlahan(5,4) --> 9

const luasLingkaran = radius => {
    const PI = 22/7;

    return PI * radius ** 2;
}
// luasLingkaran(7) --> 154

//optional parameter
const penjumlahan = (a, b=0) => a+b;
// penjumlahan(5,4) --> 9
// penjumlahan(5) --> 5

//callback function
const tampilkanHasil = (hasil) => alert(`Hasil = ${hasil}`);
const penjumlahan1 = (a, b, display) => {
    let hasil = a + b;
    display(hasil); // callback function
};

penjumlahan1(9, 6, tampilkanHasil); 
// Hasil = 15
penjumlahan1(9, 6, (hasil) => alert(`Wah, hasilnya adalah ${hasil}`)); 
// Wah, hasilnya adalah 15

//overflow argument
const penjumlahan = (a,b) => a + b;
let hasil = penjumlahan(3,4,5,6);

alert('Hasil penjumlahan = ${hasil');
// Hasil penjumlahan = 7

//rest parameters
function jumlahkanSemuanya (...bilangan){
    let total = 0;

    for(let bil of bilangan)
        total += bil;

    return total;
}

let hasil1 = jumlahkanSemuanya(1,2,3,4,5,6);
let hasil2 = jumlahkanSemuanya(9,8,7);

alert(hasil1);
// 21

alert(hasil2);
// 24
