$fn = 150;

difference() {
	linear_extrude(height = 6.375) {
		polygon(points = [[0, 0], [0, 6.375], [77.5625, 6.375], [79.6875, 4.25], [79.6875, 2.125], [77.5625, 0]]);
	}
	translate(v = [75.4375, 3.1875, -1]) {
		cylinder(d = 2.125, h = 8.375);
	}
}
