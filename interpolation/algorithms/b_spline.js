/*globals algorithms*/
'use strict'

algorithms.push({
	name: 'B-Spline',
	color: 'blue',
	handler: function (points, result) {
		// Generate interpolated values
		let temp = new Array(points.length - 1),
			res = result.length
		for (let i = 0; i < res; i++) {
			let t = i / (res - 1),
				t2 = 1 - t,
				n = points.length - 1

			for (let j = 0; j < n; j++) {
				temp[j] = t * points[j + 1] + t2 * points[j]
			}
			while (n > 1) {
				for (let j = 0; j < n - 1; j++) {
					temp[j] = t * temp[j + 1] + t2 * temp[j]
				}
				n--
			}

			result[i] = temp[0]
		}
	}
})