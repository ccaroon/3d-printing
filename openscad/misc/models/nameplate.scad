$fn = 150;

union() {
	difference() {
		cube(size = [77.7875, 39.6875, 1.5]);
		translate(v = [12.964583333333332, 19.84375, 0.5]) {
			cylinder(d = 10.25, h = 2);
		}
		translate(v = [64.82291666666666, 19.84375, 0.5]) {
			cylinder(d = 10.25, h = 2);
		}
	}
	translate(v = [0, 44.6875, 0]) {
		difference() {
			cube(size = [77.7875, 14.25, 1.5]);
			translate(v = [12.964583333333332, 7.0, 0.5]) {
				cylinder(d = 10.25, h = 2);
			}
			translate(v = [64.82291666666666, 7.0, 0.5]) {
				cylinder(d = 10.25, h = 2);
			}
		}
	}
}
