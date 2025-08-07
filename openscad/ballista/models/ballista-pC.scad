$fn = 150;

hull() {
	cube(size = [6.375, 25.5, 6.375]);
	translate(v = [9.5625, 0, 3.1875]) {
		rotate(a = [-90, 0, 0]) {
			cylinder(d = 6.375, h = 25.5);
		}
	}
}
