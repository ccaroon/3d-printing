$fn = 150;

union() {
	difference() {
		union() {
			difference() {
				union() {
					difference() {
						union() {
							difference() {
								union() {
									difference() {
										cube(size = [212.25, 212.25, 33.0]);
										translate(v = [5.625, 5.625, 5.625]) {
											cube(size = [201.0, 201.0, 33.0]);
										}
									}
									translate(v = [0.0, 0.0, 0]) {
										cube(size = [20.3, 20.3, 33.0]);
									}
								}
								translate(v = [10.15, 10.15, 31.7]) {
									cylinder(d = 10.3, h = 1.8);
								}
							}
							translate(v = [191.95, 0.0, 0]) {
								cube(size = [20.3, 20.3, 33.0]);
							}
						}
						translate(v = [202.1, 10.15, 31.7]) {
							cylinder(d = 10.3, h = 1.8);
						}
					}
					translate(v = [0.0, 191.95, 0]) {
						cube(size = [20.3, 20.3, 33.0]);
					}
				}
				translate(v = [10.15, 202.1, 31.7]) {
					cylinder(d = 10.3, h = 1.8);
				}
			}
			translate(v = [191.95, 191.95, 0]) {
				cube(size = [20.3, 20.3, 33.0]);
			}
		}
		translate(v = [202.1, 202.1, 31.7]) {
			cylinder(d = 10.3, h = 1.8);
		}
	}
	translate(v = [30.875, 5.8125, 0]) {
		color(alpha = 1.0, c = "white") {
			difference() {
				cube(size = [37.625, 200.625, 33.0]);
				translate(v = [2.8125, 2.8125, 2.8125]) {
					cube(size = [32.0, 195.0, 33.0]);
				}
			}
		}
	}
	translate(v = [65.6875, 59.390625, 0]) {
		color(alpha = 1.0, c = "white") {
			difference() {
				cube(size = [37.625, 93.46875, 33.0]);
				translate(v = [2.8125, 2.8125, 2.8125]) {
					cube(size = [32.0, 87.84375, 33.0]);
				}
			}
		}
	}
	translate(v = [143.75, 5.8125, 0]) {
		color(alpha = 1.0, c = "grey") {
			difference() {
				cube(size = [37.625, 200.625, 33.0]);
				translate(v = [2.8125, 2.8125, 2.8125]) {
					cube(size = [32.0, 195.0, 33.0]);
				}
			}
		}
	}
	translate(v = [108.9375, 59.390625, 0]) {
		color(alpha = 1.0, c = "grey") {
			difference() {
				cube(size = [37.625, 93.46875, 33.0]);
				translate(v = [2.8125, 2.8125, 2.8125]) {
					cube(size = [32.0, 87.84375, 33.0]);
				}
			}
		}
	}
}
