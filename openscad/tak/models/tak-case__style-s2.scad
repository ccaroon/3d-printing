$fn = 150;

difference() {
	union() {
		difference() {
			union() {
				difference() {
					union() {
						difference() {
							union() {
								difference() {
									cube(size = [212.25, 212.25, 34.0]);
									translate(v = [0, 0, -1]) {
										translate(v = [0, 36.5, 0]) {
											translate(v = [36.5, 0, 0]) {
												cube(size = [139.25, 139.25, 36.0]);
											}
										}
									}
								}
								translate(v = [0.0, 0.0, 0]) {
									cube(size = [20.3, 20.3, 34.0]);
								}
							}
							translate(v = [10.15, 10.15, 32.7]) {
								cylinder(d = 10.3, h = 1.55);
							}
						}
						translate(v = [191.95, 0.0, 0]) {
							cube(size = [20.3, 20.3, 34.0]);
						}
					}
					translate(v = [202.1, 10.15, 32.7]) {
						cylinder(d = 10.3, h = 1.55);
					}
				}
				translate(v = [0.0, 191.95, 0]) {
					cube(size = [20.3, 20.3, 34.0]);
				}
			}
			translate(v = [10.15, 202.1, 32.7]) {
				cylinder(d = 10.3, h = 1.55);
			}
		}
		translate(v = [191.95, 191.95, 0]) {
			cube(size = [20.3, 20.3, 34.0]);
		}
	}
	translate(v = [202.1, 202.1, 32.7]) {
		cylinder(d = 10.3, h = 1.55);
	}
	translate(v = [0, 20.3, 0]) {
		translate(v = [0, 0, 2]) {
			translate(v = [2, 0, 0]) {
				cube(size = [32.5, 171.65, 33.0]);
			}
		}
	}
	translate(v = [0, 20.3, 0]) {
		translate(v = [0, 0, 2]) {
			translate(v = [177.75, 0, 0]) {
				cube(size = [32.5, 171.65, 33.0]);
			}
		}
	}
	translate(v = [0, 0, 2]) {
		translate(v = [20.3, 0, 0]) {
			translate(v = [0, 177.75, 0]) {
				cube(size = [171.65, 32.5, 33.0]);
			}
		}
	}
	translate(v = [20.3, 0, 0]) {
		translate(v = [0, 0, 2]) {
			translate(v = [0, 2, 0]) {
				cube(size = [171.65, 32.5, 33.0]);
			}
		}
	}
}
