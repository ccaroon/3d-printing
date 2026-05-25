$fn = 150;

union() {
	cube(size = [30.0, 17.25, 7.5]);
	translate(v = [0, 17.25, 0]) {
		translate(v = [15.0, 0, 0]) {
			cylinder($fn = 6, d = 30.0, h = 7.5);
		}
	}
}
