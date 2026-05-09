$fn = 150;

difference() {
	cube(size = [212.0, 212.0, 3]);
	translate(v = [0, 0, 2]) {
		union() {
			translate(v = [0, 3, 0]) {
				translate(v = [3, 0, 0]) {
					union() {
						cube(size = [206.0, 1, 2]);
						translate(v = [0, 41.0, 0]) {
							cube(size = [206.0, 1, 2]);
						}
						translate(v = [0, 82.0, 0]) {
							cube(size = [206.0, 1, 2]);
						}
						translate(v = [0, 123.0, 0]) {
							cube(size = [206.0, 1, 2]);
						}
						translate(v = [0, 164.0, 0]) {
							cube(size = [206.0, 1, 2]);
						}
						translate(v = [0, 205.0, 0]) {
							cube(size = [206.0, 1, 2]);
						}
					}
				}
			}
			translate(v = [0, 3, 0]) {
				translate(v = [3, 0, 0]) {
					union() {
						cube(size = [1, 206.0, 2]);
						translate(v = [41.0, 0, 0]) {
							cube(size = [1, 206.0, 2]);
						}
						translate(v = [82.0, 0, 0]) {
							cube(size = [1, 206.0, 2]);
						}
						translate(v = [123.0, 0, 0]) {
							cube(size = [1, 206.0, 2]);
						}
						translate(v = [164.0, 0, 0]) {
							cube(size = [1, 206.0, 2]);
						}
						translate(v = [205.0, 0, 0]) {
							cube(size = [1, 206.0, 2]);
						}
					}
				}
			}
		}
	}
	#translate(v = [0, 3.5, 0]) {
		translate(v = [3.5, 0, 0]) {
			translate(v = [0, 0, 2]) {
				union() {
					difference() {
						union() {
							rotate(a = [-90, 0, 0]) {
								cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
							}
							rotate(a = [90, 0, 0]) {
								cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
							}
							rotate(a = [90, 0, 90]) {
								cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
							}
							rotate(a = [90, 0, -90]) {
								cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
							}
						}
						translate(v = [0, -10.0, 0]) {
							translate(v = [-10.0, 0, 0]) {
								translate(v = [0, 0, -4.0]) {
									cube(size = [20.0, 20.0, 4.0]);
								}
							}
						}
					}
					translate(v = [0, 0.0, 0]) {
						translate(v = [0.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 0.0, 0]) {
						translate(v = [41.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 0.0, 0]) {
						translate(v = [82.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 0.0, 0]) {
						translate(v = [123.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 0.0, 0]) {
						translate(v = [164.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 0.0, 0]) {
						translate(v = [205.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 41.0, 0]) {
						translate(v = [0.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 41.0, 0]) {
						translate(v = [41.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 41.0, 0]) {
						translate(v = [82.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 41.0, 0]) {
						translate(v = [123.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 41.0, 0]) {
						translate(v = [164.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 41.0, 0]) {
						translate(v = [205.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 82.0, 0]) {
						translate(v = [0.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 82.0, 0]) {
						translate(v = [41.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 82.0, 0]) {
						translate(v = [82.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 82.0, 0]) {
						translate(v = [123.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 82.0, 0]) {
						translate(v = [164.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 82.0, 0]) {
						translate(v = [205.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 123.0, 0]) {
						translate(v = [0.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 123.0, 0]) {
						translate(v = [41.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 123.0, 0]) {
						translate(v = [82.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 123.0, 0]) {
						translate(v = [123.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 123.0, 0]) {
						translate(v = [164.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 123.0, 0]) {
						translate(v = [205.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 164.0, 0]) {
						translate(v = [0.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 164.0, 0]) {
						translate(v = [41.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 164.0, 0]) {
						translate(v = [82.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 164.0, 0]) {
						translate(v = [123.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 164.0, 0]) {
						translate(v = [164.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 164.0, 0]) {
						translate(v = [205.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 205.0, 0]) {
						translate(v = [0.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 205.0, 0]) {
						translate(v = [41.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 205.0, 0]) {
						translate(v = [82.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 205.0, 0]) {
						translate(v = [123.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 205.0, 0]) {
						translate(v = [164.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
										}
									}
								}
							}
						}
					}
					translate(v = [0, 205.0, 0]) {
						translate(v = [205.0, 0, 0]) {
							difference() {
								union() {
									rotate(a = [-90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 0]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, 90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
									rotate(a = [90, 0, -90]) {
										cylinder($fn = 4, h = 10.0, r1 = 4.0, r2 = 0);
									}
								}
								translate(v = [0, -10.0, 0]) {
									translate(v = [-10.0, 0, 0]) {
										translate(v = [0, 0, -4.0]) {
											cube(size = [20.0, 20.0, 4.0]);
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
