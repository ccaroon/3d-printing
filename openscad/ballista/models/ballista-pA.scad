$fn = 150;

difference() {
	cube(size = [85.0, 21.25, 6.375]);
	translate(v = [17.0, 10.625, -1]) {
		cylinder(d = 8.5, h = 8.375);
	}
	translate(v = [68.0, 10.625, -1]) {
		cylinder(d = 8.5, h = 8.375);
	}
}
