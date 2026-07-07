$fn = 150;

union() {
	cylinder(d = 69.5, h = 1);
	translate(v = [0, 0, 1]) {
		difference() {
			color(alpha = 1.0, c = "red") {
				cylinder(d = 65.5, h = 20);
			}
			translate(v = [0, 0, -0.5]) {
				cylinder(d = 63.5, h = 21);
			}
		}
	}
	translate(v = [75.5, 0, 0]) {
		union() {
			cylinder(d = 69.5, h = 1);
			translate(v = [0, 0, 1]) {
				difference() {
					color(alpha = 1.0, c = "red") {
						cylinder(d = 63.5, h = 3);
					}
					translate(v = [0, 0, -0.5]) {
						cylinder(d = 61.5, h = 4);
					}
				}
			}
		}
	}
}
