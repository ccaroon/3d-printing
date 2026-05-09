$fn = 150;

difference() {
	union() {
		rotate(a = [-90, 0, 0]) {
			cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
		}
		rotate(a = [90, 0, 0]) {
			cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
		}
		rotate(a = [90, 0, 90]) {
			cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
		}
		rotate(a = [90, 0, -90]) {
			cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
		}
	}
	translate(v = [0, -10.0, 0]) {
		translate(v = [-10.0, 0, 0]) {
			translate(v = [0, 0, -4.0]) {
				cube(size = [20.0, 20.0, 4.0]);
			}
		}
	}
}
