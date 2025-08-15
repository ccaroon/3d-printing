union() {
	translate(v = [0.0, 0.0, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.75);
			translate(v = [0, 0, 2.0]) {
				cylinder($fn = 6, d = 55.0, h = 2.75);
			}
		}
	}
	translate(v = [42.0, 24.24871130596428, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.75);
			translate(v = [0, 0, 2.0]) {
				cylinder($fn = 6, d = 55.0, h = 2.75);
			}
		}
	}
	translate(v = [84.0, 0.0, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.75);
			translate(v = [0, 0, 2.0]) {
				cylinder($fn = 6, d = 55.0, h = 2.75);
			}
		}
	}
	translate(v = [42.0, -24.24871130596428, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.75);
			translate(v = [0, 0, 2.0]) {
				cylinder($fn = 6, d = 55.0, h = 2.75);
			}
		}
	}
}
