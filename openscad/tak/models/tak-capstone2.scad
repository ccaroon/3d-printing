$fn = 150;

union() {
	cylinder(d = 10.4, h = 3.0);
	translate(v = [0, 0, 3.0]) {
		cylinder(d1 = 10.4, d2 = 5.2, h = 8.450000000000001);
	}
	translate(v = [0, 0, 12.790625000000002]) {
		sphere(d = 5.362500000000001);
	}
}
