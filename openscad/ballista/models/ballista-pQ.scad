$fn = 150;

difference() {
	linear_extrude(height = 6.375) {
		polygon(points = [[0, 0], [10.0625, 6.375], [20.1875, 6.375], [20.1875, 0]]);
	}
	translate(v = [15.9375, 3.1875, -1]) {
		cylinder(d = 2.125, h = 8.375);
	}
}
