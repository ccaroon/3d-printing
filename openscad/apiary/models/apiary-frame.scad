$fn = 150;

union() {
	translate(v = [0.0, 0.0, 0]) {
		difference() {
			cylinder($fn = 6, d = 56.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 54.0, h = 3.0);
			}
		}
	}
	translate(v = [41.25, 23.81569860407206, 0]) {
		difference() {
			cylinder($fn = 6, d = 56.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 54.0, h = 3.0);
			}
		}
	}
	translate(v = [82.5, 0.0, 0]) {
		difference() {
			cylinder($fn = 6, d = 56.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 54.0, h = 3.0);
			}
		}
	}
	translate(v = [41.25, -23.81569860407206, 0]) {
		difference() {
			cylinder($fn = 6, d = 56.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 54.0, h = 3.0);
			}
		}
	}
}
