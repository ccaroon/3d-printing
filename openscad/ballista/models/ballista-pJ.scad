$fn = 150;

difference() {
	union() {
		cube(size = [21.25, 10.625, 6.375]);
		translate(v = [10.625, 10.625, 0]) {
			cylinder(d = 21.25, h = 6.375);
		}
	}
	translate(v = [10.625, 4.25, -1]) {
		cylinder(d = 2.125, h = 8.375);
	}
}
