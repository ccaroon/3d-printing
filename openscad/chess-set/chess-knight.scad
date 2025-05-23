$fn = 150;

union() {
	difference() {
		cylinder(d = 30.0, h = 3.9);
		translate(v = [0, 0, -1]) {
			cylinder(d = 15.5, h = 3.5);
		}
	}
	translate(v = [0, 0, 3.9]) {
		rotate(a = [0, 0, 180]) {
			linear_extrude(height = 18.262500000000003, scale = [1, 1.5], twist = 90) {
				circle($fn = 5, d = 30.0);
			}
		}
	}
	translate(v = [0, 0, 40.425000000000004]) {
		sphere(d = 22.5);
	}
}
