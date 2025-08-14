union() {
	translate(v = [0.0, 0.0, 0]) {
		difference() {
			cylinder($fn = 6, d = 55.0, h = 3.75);
			translate(v = [0, 0, 2.0]) {
				cylinder($fn = 6, d = 53.0, h = 2.75);
			}
		}
	}
	translate(v = [40.5, 23.38268590217984, 0]) {
		difference() {
			cylinder($fn = 6, d = 55.0, h = 3.75);
			translate(v = [0, 0, 2.0]) {
				cylinder($fn = 6, d = 53.0, h = 2.75);
			}
		}
	}
	translate(v = [81.0, 0.0, 0]) {
		difference() {
			cylinder($fn = 6, d = 55.0, h = 3.75);
			translate(v = [0, 0, 2.0]) {
				cylinder($fn = 6, d = 53.0, h = 2.75);
			}
		}
	}
	translate(v = [40.5, -23.38268590217984, 0]) {
		difference() {
			cylinder($fn = 6, d = 55.0, h = 3.75);
			translate(v = [0, 0, 2.0]) {
				cylinder($fn = 6, d = 53.0, h = 2.75);
			}
		}
	}
}
