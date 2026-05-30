$fn = 150;

union() {
	cylinder(d = 20.0, h = 1.0);
	color(alpha = 1.0, c = "grey") {
		translate(v = [0, 0, 1.0]) {
			cylinder($fn = 3, d = 18.0, h = 1.0);
		}
	}
}
