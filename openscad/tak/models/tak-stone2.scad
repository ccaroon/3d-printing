$fn = 150;

union() {
	cube(size = [30.0, 15.0, 7.5]);
	translate(v = [0, 15.0, 0]) {
		translate(v = [15.0, 0, 0]) {
			cylinder(d = 30.0, h = 7.5);
		}
	}
}
