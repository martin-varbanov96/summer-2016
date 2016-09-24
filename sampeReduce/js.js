var cars = [
	{name: "Goshko", colour: "cherven"},
	{name: "Ivanco", colour: "zelen"},
	{name: "Peshko", colour: "zelen"},
	{name: "Goshko", colour: "gaden"},
];

var names = cars.reduce(function(names, car){
	names.push(car.name);
	return names;
}, []);

console.log(names);