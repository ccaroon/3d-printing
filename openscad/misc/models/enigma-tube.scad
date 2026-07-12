$fn = 150;

union() {
	cylinder(d = 70.45, h = 1);
	translate(v = [0, 0, 1]) {
		difference() {
			color(alpha = 1.0, c = "red") {
				cylinder(d = 66.45, h = 203);
			}
			translate(v = [0, 0, -0.5]) {
				cylinder(d = 64.45, h = 204);
			}
		}
	}
	translate(v = [76.45, 0, 0]) {
		union() {
			cylinder(d = 70.45, h = 1);
			translate(v = [0, 0, 1]) {
				difference() {
					color(alpha = 1.0, c = "red") {
						cylinder(d = 64.45, h = 15);
					}
					translate(v = [0, 0, -0.5]) {
						cylinder(d = 62.45, h = 16);
					}
				}
			}
		}
	}
}
