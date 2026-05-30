$fn = 150;

union() {
	cylinder(d = 20.0, h = 1.0);
	color(alpha = 1.0, c = "grey") {
		translate(v = [-1.5, -9.0, 1.0]) {
			cube(size = [3, 18.0, 1.0]);
		}
	}
}
