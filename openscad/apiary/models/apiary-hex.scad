difference() {
	cylinder($fn = 6, d = 55.0, h = 3.75);
	translate(v = [0, 0, 2.0]) {
		cylinder($fn = 6, d = 53.0, h = 2.75);
	}
}
