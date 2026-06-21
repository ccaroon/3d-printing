$fn = 150;

difference() {
	cylinder(d = 115.0, h = 5.0);
	translate(v = [0, 0, 2]) {
		cylinder(d = 111.0, h = 5.0);
	}
}
