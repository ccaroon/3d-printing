$fn = 150;

union() {
	cube(size = [10.4, 6.24, 2.6]);
	translate(v = [0, 6.24, 0]) {
		translate(v = [5.2, 0, 0]) {
			cylinder(d = 10.4, h = 2.6);
		}
	}
}
