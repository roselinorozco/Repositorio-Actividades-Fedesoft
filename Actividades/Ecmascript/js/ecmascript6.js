/*ECMASCRIPT 6*/
let template1 = "Hola";
let template2 = "Mundo";

console.log(`${template1} 
${template2}`);

/*ECMASCRIPT 5*/

console.log(`Hola`+`\n`+`Mundo EcmaScript5`);

/*Arrays*/
var alumnos=['Fabio','Javier','Roselin','Francisco'];
console.log(alumnos[2]);

/*Destructuring - ECMASCRIPT6*/

var [a,b] = ["Hola","Mundo"];
console.log(a);

var persona = {nombre:"pepito",apellido:"perez"};
var {nombre,apellido} = persona;

console.log(nombre);

var funcion = function(){
    return ["175","75"];
};

var [estatura,peso] = funcion();

console.log(estatura);

/*ECMASCRIPT6 - valores por defecto */
function suma(numero1=0,numero2=0){
    return numero1+numero2;
}
//suma();
//suma(1);

var arreglo = [0,1,2,3,4,5,6,7,8,9,10];

for(var i=10;i>=5;i--){
   console.log(arreglo[i]);
}