$fn = 150;

union() {
	difference() {
		cylinder(d = 28.0, h = 3.9);
		translate(v = [0, 0, -1]) {
			cylinder(d = 15.5, h = 3.5);
		}
	}
	translate(v = [0, 0, 3.9]) {
		cylinder($fn = 10, d1 = 19.88, d2 = 9.24, h = 24.35);
	}
	translate(v = [0, 0, 28.25]) {
		union() {
			cylinder(d1 = 9.24, d2 = 14.0, h = 2);
			translate(v = [0, 0, 2.75]) {
				minkowski() {
					sphere(d = 1.5);
					cylinder(d = 14.0, h = 0.5);
				}
			}
			translate(v = [0, 0, 2.5]) {
				translate(v = [0, 0, 7.0]) {
					sphere(d = 14.0);
				}
			}
		}
	}
}
