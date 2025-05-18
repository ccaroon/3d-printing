$fn = 150;

difference() {
	cylinder(d = 30.0, h = 3.8);
	translate(v = [0, 0, -1]) {
		cylinder(d = 15.5, h = 3.3);
	}
}
