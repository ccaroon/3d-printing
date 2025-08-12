$fn = 150;

difference() {
	union() {
		cube(size = [12.75, 68.0, 6.375]);
		translate(v = [6.375, 68.0, 0]) {
			cylinder(d = 12.75, h = 6.375);
		}
	}
	translate(v = [6.375, 70.125, -1]) {
		cylinder(d = 2.125, h = 8.375);
	}
}
