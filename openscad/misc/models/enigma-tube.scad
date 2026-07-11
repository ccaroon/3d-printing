$fn = 150;

union() {
	cylinder(d = 70.4, h = 1);
	translate(v = [0, 0, 1]) {
		difference() {
			color(alpha = 1.0, c = "red") {
				cylinder(d = 66.4, h = 10);
			}
			translate(v = [0, 0, -0.5]) {
				cylinder(d = 64.4, h = 11);
			}
		}
	}
}
