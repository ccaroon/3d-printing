$fn = 150;

union() {
	cylinder(d = 71.07324530188258, h = 2);
	translate(v = [0, 0, 2]) {
		difference() {
			color(alpha = 1.0, c = "red") {
				cylinder(d = 69.07324530188258, h = 20);
			}
			translate(v = [0, 0, -0.5]) {
				cylinder(d = 67.07324530188258, h = 21);
			}
		}
	}
	translate(v = [79.07324530188258, 0, 0]) {
		union() {
			cylinder(d = 71.07324530188258, h = 2);
			translate(v = [0, 0, 2]) {
				difference() {
					color(alpha = 1.0, c = "red") {
						cylinder(d = 67.07324530188258, h = 3.0);
					}
					translate(v = [0, 0, -0.5]) {
						cylinder(d = 65.07324530188258, h = 4.0);
					}
				}
			}
		}
	}
}
