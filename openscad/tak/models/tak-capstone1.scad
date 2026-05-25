$fn = 150;

union() {
	cylinder(d = 30.0, h = 3.0);
	translate(v = [0, 0, 3.0]) {
		cylinder($fn = 8, d1 = 30.0, d2 = 15.0, h = 24.375);
	}
	translate(v = [0, 0, 31.2421875]) {
		sphere($fn = 8, d = 15.468750000000002);
	}
}
