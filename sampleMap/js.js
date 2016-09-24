var cars = [
	{name: "Goshko", colour: "cherven"},
	{name: "Ivanco", colour: "zelen"},
	{name: "Peshko", colour: "zelen"},
	{name: "Goshko", colour: "gaden"},
];
console.log(cars);

var names = cars.map(function(car){
	return car.name;
});

console.log(names);