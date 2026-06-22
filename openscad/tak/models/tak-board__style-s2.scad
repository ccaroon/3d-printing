$fn = 150;

difference() {
	cube(size = [58.25, 58.25, 5.625]);
	color(alpha = 1.0, c = "#777777") {
		translate(v = [0, 9.875, 0]) {
			translate(v = [9.875, 0, 0]) {
				translate(v = [0, 0, 5.725]) {
					union() {
						rotate(a = [0, 180, 0]) {
							cylinder($fn = 6, h = 2.0625, r = 7.5);
						}
						translate(v = [0, 0.0, 0]) {
							translate(v = [0.0, 0, 0]) {
								rotate(a = [0, 180, 0]) {
									cylinder($fn = 6, h = 2.0625, r = 7.5);
								}
							}
						}
						translate(v = [0, 0.0, 0]) {
							translate(v = [38.5, 0, 0]) {
								rotate(a = [0, 180, 0]) {
									cylinder($fn = 6, h = 2.0625, r = 7.5);
								}
							}
						}
						translate(v = [0, 38.5, 0]) {
							translate(v = [0.0, 0, 0]) {
								rotate(a = [0, 180, 0]) {
									cylinder($fn = 6, h = 2.0625, r = 7.5);
								}
							}
						}
						translate(v = [0, 38.5, 0]) {
							translate(v = [38.5, 0, 0]) {
								rotate(a = [0, 180, 0]) {
									cylinder($fn = 6, h = 2.0625, r = 7.5);
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [0, 0, 4.625]) {
		union() {
			translate(v = [0, 9.375, 0]) {
				translate(v = [9.375, 0, 0]) {
					union() {
						cube(size = [39.5, 1, 2]);
						translate(v = [0, 38.5, 0]) {
							cube(size = [39.5, 1, 2]);
						}
					}
				}
			}
			translate(v = [0, 9.375, 0]) {
				translate(v = [9.375, 0, 0]) {
					union() {
						cube(size = [1, 39.5, 2]);
						translate(v = [38.5, 0, 0]) {
							cube(size = [1, 39.5, 2]);
						}
					}
				}
			}
		}
	}
	translate(v = [10.15, 10.15, -0.5]) {
		cylinder(d = 10.3, h = 1.8);
	}
	translate(v = [48.1, 10.15, -0.5]) {
		cylinder(d = 10.3, h = 1.8);
	}
	translate(v = [10.15, 48.1, -0.5]) {
		cylinder(d = 10.3, h = 1.8);
	}
	translate(v = [48.1, 48.1, -0.5]) {
		cylinder(d = 10.3, h = 1.8);
	}
}
