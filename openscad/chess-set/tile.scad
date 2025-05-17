$fn = 150;

difference() {
	translate(v = [-19.0, -19.0, 0]) {
		cube(size = [38.0, 38.0, 3.25]);
	}
	translate(v = [0, 0, 0.9500000000000002]) {
		cylinder(d = 15.5, h = 3.3);
	}
}
