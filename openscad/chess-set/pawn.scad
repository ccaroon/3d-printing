$fn = 150;

union() {
	difference() {
		cylinder(d = 28.0, h = 3.8);
		translate(v = [0, 0, -1]) {
			cylinder(d = 15.5, h = 3.3);
		}
	}
	translate(v = [0, 0, 3.8]) {
		union() {
			cube(center = true, size = [16.8, 16.8, 5]);
			cylinder(d1 = 14.0, d2 = 7.0, h = 24.35);
		}
	}
	translate(v = [0, 0, 28.150000000000002]) {
		sphere(d = 16.0);
	}
}
