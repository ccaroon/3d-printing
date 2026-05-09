$fn = 150;

difference() {
	cube(size = [112, 112, 3]);
	translate(v = [0, 0, 2]) {
		union() {
			translate(v = [0, 3, 0]) {
				translate(v = [3, 0, 0]) {
					union() {
						cube(size = [106, 1, 2]);
						translate(v = [0, 21, 0]) {
							cube(size = [106, 1, 2]);
						}
						translate(v = [0, 42, 0]) {
							cube(size = [106, 1, 2]);
						}
						translate(v = [0, 63, 0]) {
							cube(size = [106, 1, 2]);
						}
						translate(v = [0, 84, 0]) {
							cube(size = [106, 1, 2]);
						}
						translate(v = [0, 105, 0]) {
							cube(size = [106, 1, 2]);
						}
					}
				}
			}
			translate(v = [0, 3, 0]) {
				translate(v = [3, 0, 0]) {
					union() {
						cube(size = [1, 106, 2]);
						translate(v = [21, 0, 0]) {
							cube(size = [1, 106, 2]);
						}
						translate(v = [42, 0, 0]) {
							cube(size = [1, 106, 2]);
						}
						translate(v = [63, 0, 0]) {
							cube(size = [1, 106, 2]);
						}
						translate(v = [84, 0, 0]) {
							cube(size = [1, 106, 2]);
						}
						translate(v = [105, 0, 0]) {
							cube(size = [1, 106, 2]);
						}
					}
				}
			}
		}
	}
}
