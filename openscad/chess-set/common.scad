$fn = 150;

difference() {
	cylinder(d = 28.0, h = 3.75);
	translate(v = [0, 0, -1]) {
		cylinder(d = 15.5, h = 3.3);
	}
}
