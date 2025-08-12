$fn = 150;

difference() {
	linear_extrude(height = 6.375) {
		polygon(points = [[3.1875, 0], [0, 8.5], [0, 17.0], [12.75, 17.0], [12.75, 8.5], [9.5625, 0]]);
	}
	translate(v = [-1, 8.5, 3.1875]) {
		rotate(a = [0, 90, 0]) {
			cylinder(d = 1.59375, h = 14.75);
		}
	}
	translate(v = [-1, 4.25, 3.1875]) {
		rotate(a = [0, 90, 0]) {
			cylinder(d = 1.59375, h = 14.75);
		}
	}
	translate(v = [6.375, 17.0, -1]) {
		cylinder(h = 8.375, r = 3.1875);
	}
}
