$fn = 150;

difference() {
	cylinder(d = 30.0, h = 3.9);
	translate(v = [0, 0, -1]) {
		cylinder(d = 20.3, h = 2.3);
	}
}
