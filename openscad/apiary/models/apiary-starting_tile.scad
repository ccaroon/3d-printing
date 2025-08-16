$fn = 150;

difference() {
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
		translate(v = [0.0, 47.63139720814412, 0]) {
			difference() {
				cylinder($fn = 6, d = 56.0, h = 3.0);
				translate(v = [0, 0, 1.0]) {
					cylinder($fn = 6, d = 54.0, h = 3.0);
				}
			}
		}
	}
	translate(v = [13.75, 23.824673200287624, 1.0]) {
		cylinder(d = 55.0, h = 3.5);
	}
}
