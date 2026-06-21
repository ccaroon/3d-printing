$fn = 150;

difference() {
	cylinder(d = 30.0, h = 7.5);
	translate(v = [0, -20.0, 0]) {
		translate(v = [0, 0, 3.75]) {
			cube(center = true, size = [30.0, 15.0, 9.5]);
		}
	}
}
