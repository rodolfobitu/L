/*globals algorithms*/
'use strict'

algorithms.push({
	name: 'Quadratic Spline',
	color: 'green',
	handler: function (points, result) {
		let n = points.length - 1
		if (n !== 5) {
			throw new Error('I am too lazy now to make this generic. Please use 6 points')
		}

		// Using top calc:
		// > n = 6
		// > A = matrix(n, n, i, j, if(i==j||i==j+1, 1, 0))
		// > C = matrix(n, 1, i, j, if(i==1, 0, y[i-1]-y[i-2]))
		// > simplify(inverse(A)*2*C)
		let y = points,
			b = [0, -2 * y[0] + 2 * y[1], 2 * y[0] - 4 * y[1] + 2 * y[2], -2 * y[0] + 4 * y[1] - 4 * y[2] + 2 * y[3], 2 * y[0] - 4 * y[1] + 4 * y[2] - 4 * y[3] + 2 * y[4], -2 * y[0] + 4 * y[1] - 4 * y[2] + 4 * y[3] - 4 * y[4] + 2 * y[5]]

		// Generate spline coefficients
		// Y[i](t) = a[i] + b[i] * t + c[i] * t^2
		var a = new Array(n),
			c = new Array(n)
		for (let i = 0; i < n; i++) {
			a[i] = y[i]
			c[i] = y[i + 1] - y[i] - b[i]
		}

		// Generate interpolated values
		let res = result.length,
			iToX = n / (res - 1)
		for (let i = 0; i < res; i++) {
			let x = i * iToX,
				j = i === res - 1 ? n - 1 : Math.floor(x),
				t = x - j

			result[i] = a[j] + (b[j] + c[j] * t) * t
		}
	}
})