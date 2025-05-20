$fn = 150;

difference() {
	translate(v = [-19.0, -19.0, 0]) {
		cube(size = [38.0, 38.0, 3.5]);
	}
	translate(v = [0, 0, 1.0]) {
		cylinder(d = 15.5, h = 3.5);
	}
}
