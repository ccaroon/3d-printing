$fn = 150;

difference() {
	union() {
		rotate(a = [-90, 0, 0]) {
			cylinder($fn = 4, h = 3.25, r1 = 0.9100000000000001, r2 = 0);
		}
		rotate(a = [90, 0, 0]) {
			cylinder($fn = 4, h = 3.25, r1 = 0.9100000000000001, r2 = 0);
		}
		rotate(a = [90, 0, 90]) {
			cylinder($fn = 4, h = 3.25, r1 = 0.9100000000000001, r2 = 0);
		}
		rotate(a = [90, 0, -90]) {
			cylinder($fn = 4, h = 3.25, r1 = 0.9100000000000001, r2 = 0);
		}
	}
	translate(v = [0, -3.25, 0]) {
		translate(v = [-3.25, 0, 0]) {
			translate(v = [0, 0, -0.9100000000000001]) {
				cube(size = [6.5, 6.5, 0.9100000000000001]);
			}
		}
	}
}
