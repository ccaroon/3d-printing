$fn = 150;

difference() {
	%cube(size = [25.4, 25.4, 25.4]);
	translate(v = [1, 1, 1]) {
		color(alpha = 1.0, c = "green") {
			cube(size = [23.4, 23.4, 23.4]);
		}
	}
}
