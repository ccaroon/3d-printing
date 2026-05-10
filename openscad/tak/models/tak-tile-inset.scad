$fn = 150;

difference() {
	union() {
		rotate(a = [-90, 0, 0]) {
			cylinder($fn = 4, h = 5.0, r1 = 1.4000000000000001, r2 = 0);
		}
		rotate(a = [90, 0, 0]) {
			cylinder($fn = 4, h = 5.0, r1 = 1.4000000000000001, r2 = 0);
		}
		rotate(a = [90, 0, 90]) {
			cylinder($fn = 4, h = 5.0, r1 = 1.4000000000000001, r2 = 0);
		}
		rotate(a = [90, 0, -90]) {
			cylinder($fn = 4, h = 5.0, r1 = 1.4000000000000001, r2 = 0);
		}
	}
	translate(v = [0, -5.0, 0]) {
		translate(v = [-5.0, 0, 0]) {
			translate(v = [0, 0, -1.4000000000000001]) {
				cube(size = [10.0, 10.0, 1.4000000000000001]);
			}
		}
	}
}
