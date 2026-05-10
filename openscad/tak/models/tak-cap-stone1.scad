$fn = 150;

union() {
	cube(size = [10.0, 10.799999999999999, 5]);
	translate(v = [0, 10.799999999999999, 0]) {
		translate(v = [5.0, 0, 0]) {
			cylinder($fn = 6, d = 10.0, h = 5);
		}
	}
}
