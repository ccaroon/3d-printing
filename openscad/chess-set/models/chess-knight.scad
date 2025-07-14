$fn = 150;

union() {
	difference() {
		cylinder(d = 30.0, h = 3.9);
		translate(v = [0, 0, -1]) {
			cylinder(d = 20.6, h = 2.75);
		}
	}
	translate(v = [0, 0, 3.9]) {
		union() {
			scale(v = [1.0, 0.75]) {
				cylinder($fn = 6, d = 25, h = 3.4);
			}
			translate(v = [0.5, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 3.4]) {
						cylinder($fn = 6, d = 24.0, h = 3.4);
					}
				}
			}
			translate(v = [1.0, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 6.8]) {
						cylinder($fn = 6, d = 23.0, h = 3.4);
					}
				}
			}
			translate(v = [1.5, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 10.2]) {
						cylinder($fn = 6, d = 22.0, h = 3.4);
					}
				}
			}
			translate(v = [2.0, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 13.6]) {
						cylinder($fn = 6, d = 21.0, h = 3.4);
					}
				}
			}
			translate(v = [2.5, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 17.0]) {
						cylinder($fn = 6, d = 20.0, h = 3.4);
					}
				}
			}
			translate(v = [3.0, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 20.4]) {
						cylinder($fn = 6, d = 19.0, h = 3.4);
					}
				}
			}
			translate(v = [3.5, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 23.8]) {
						cylinder($fn = 6, d = 18.0, h = 3.4);
					}
				}
			}
			translate(v = [4.0, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 27.2]) {
						cylinder($fn = 6, d = 17.0, h = 3.4);
					}
				}
			}
			translate(v = [4.5, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 30.599999999999998]) {
						cylinder($fn = 6, d = 16.0, h = 3.4);
					}
				}
			}
		}
	}
	translate(v = [5, 0, 27.9]) {
		translate(v = [-18.7, 2.0, 0]) {
			rotate(a = [90, 0, 0]) {
				union() {
					resize(newsize = [28.05, 28.729999999999997, 0]) {
						linear_extrude(height = 4) {
							import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
						}
					}
					color(alpha = 1.0, c = "grey") {
						translate(v = [2.8049999999999997, 2.8729999999999993, 4]) {
							scale(v = [0.8, 0.8, 0.8]) {
								resize(newsize = [28.05, 28.729999999999997, 0]) {
									linear_extrude(height = 4) {
										import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
									}
								}
							}
						}
					}
					color(alpha = 1.0, c = "grey") {
						translate(v = [2.8049999999999997, 2.8729999999999993, -3.2]) {
							scale(v = [0.8, 0.8, 0.8]) {
								resize(newsize = [28.05, 28.729999999999997, 0]) {
									linear_extrude(height = 4) {
										import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
									}
								}
							}
						}
					}
					color(alpha = 1.0, c = "black") {
						translate(v = [4.207500000000001, 4.3095, 4]) {
							scale(v = [0.7, 0.7, 0.7]) {
								union() {
									resize(newsize = [28.05, 28.729999999999997, 0]) {
										linear_extrude(height = 4) {
											import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
										}
									}
									color(alpha = 1.0, c = "grey") {
										translate(v = [2.8049999999999997, 2.8729999999999993, 4]) {
											scale(v = [0.8, 0.8, 0.8]) {
												resize(newsize = [28.05, 28.729999999999997, 0]) {
													linear_extrude(height = 4) {
														import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
													}
												}
											}
										}
									}
									color(alpha = 1.0, c = "grey") {
										translate(v = [2.8049999999999997, 2.8729999999999993, -3.2]) {
											scale(v = [0.8, 0.8, 0.8]) {
												resize(newsize = [28.05, 28.729999999999997, 0]) {
													linear_extrude(height = 4) {
														import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
													}
												}
											}
										}
									}
								}
							}
						}
					}
					color(alpha = 1.0, c = "black") {
						translate(v = [4.207500000000001, 4.3095, -2.8]) {
							scale(v = [0.7, 0.7, 0.7]) {
								union() {
									resize(newsize = [28.05, 28.729999999999997, 0]) {
										linear_extrude(height = 4) {
											import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
										}
									}
									color(alpha = 1.0, c = "grey") {
										translate(v = [2.8049999999999997, 2.8729999999999993, 4]) {
											scale(v = [0.8, 0.8, 0.8]) {
												resize(newsize = [28.05, 28.729999999999997, 0]) {
													linear_extrude(height = 4) {
														import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
													}
												}
											}
										}
									}
									color(alpha = 1.0, c = "grey") {
										translate(v = [2.8049999999999997, 2.8729999999999993, -3.2]) {
											scale(v = [0.8, 0.8, 0.8]) {
												resize(newsize = [28.05, 28.729999999999997, 0]) {
													linear_extrude(height = 4) {
														import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
