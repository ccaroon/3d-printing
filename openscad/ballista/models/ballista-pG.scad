$fn = 150;

difference() {
	linear_extrude(height = 6.375) {
		polygon(points = [[0, 0], [0, 4.25], [4.25, 6.375], [38.25, 6.375], [42.5, 4.25], [42.5, 0]]);
	}
	translate(v = [29.75, 3.1875, -1]) {
		cylinder(d = 2.125, h = 8.375);
	}
}
