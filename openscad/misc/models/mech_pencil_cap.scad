$fn = 150;

difference() {
	cylinder(d = 7.75, h = 12.5);
	translate(v = [0, 0, 2]) {
		cylinder(d = 6.75, h = 12.5);
	}
}
