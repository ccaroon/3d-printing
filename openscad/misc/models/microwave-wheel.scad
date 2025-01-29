$fn = 150;

difference() {
	cylinder(d = 14.9, h = 7.9);
	translate(v = [0, 0, 5.9]) {
		cylinder(d = 10.5, h = 3);
	}
	translate(v = [0, 0, -2.5]) {
		cylinder(d = 7.5, h = 12.9);
	}
}
