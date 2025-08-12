$fn = 150;

difference() {
	cube(size = [6.375, 195.5, 6.375]);
	translate(v = [3.1875, 178.5, 2.125]) {
		cylinder(d = 2.125, h = 5.25);
	}
	translate(v = [3.1875, 157.25, 2.125]) {
		cylinder(d = 2.125, h = 5.25);
	}
	translate(v = [3.1875, 129.625, 2.125]) {
		cylinder(d = 2.125, h = 5.25);
	}
	translate(v = [3.1875, 106.25, 2.125]) {
		cylinder(d = 2.125, h = 5.25);
	}
}
