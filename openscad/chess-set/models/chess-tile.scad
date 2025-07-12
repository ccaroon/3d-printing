$fn = 150;

difference() {
	translate(v = [-19.0, -19.0, 0]) {
		cube(size = [38.0, 38.0, 2.75]);
	}
	translate(v = [0, 0, 1.0]) {
		cylinder(d = 20.6, h = 2.75);
	}
}
