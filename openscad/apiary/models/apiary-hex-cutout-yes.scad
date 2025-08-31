$fn = 150;

difference() {
	cylinder($fn = 6, d = 56.0, h = 3.0);
	translate(v = [0, 0, 1.0]) {
		cylinder($fn = 6, d = 54.0, h = 3.0);
	}
	translate(v = [0, 0, -1]) {
		cylinder($fn = 6, d = 39, h = 3.0);
	}
}
