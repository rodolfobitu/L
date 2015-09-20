/*globals algorithms*/
'use strict'

algorithms.push({
	name: 'Cubic Spline',
	color: 'red',
	handler: function (points, result) {
		let n = points.length - 1
		if (n !== 5) {
			throw new Error('I am too lazy now to make this generic. Please use 6 points')
		}

		// From http://mathworld.wolfram.com/CubicSpline.html
		// And using top calc:
		// > n = 6
		// > A = matrix(n, n, i, j, if(i==j, if(i==1||i==n, 2, 4), if(abs(i-j)==1, 1, 0)))
		// > C = matrix(n, 1, i, j, if(i==1, y[1]-y[0], if(i==n, y[n-1]-y[n-2], y[i]-y[i-2])))
		// > simplify(inverse(A)*3*C)
		let y = points,
			D = [-265 / 209 * y[0] + 336 / 209 * y[1] - 90 / 209 * y[2] + 24 / 209 * y[3] - 6 / 209 * y[4] + 1 / 209 * y[5], -97 / 209 * y[0] - 45 / 209 * y[1] + 180 / 209 * y[2] - 48 / 209 * y[3] + 12 / 209 * y[4] - 2 / 209 * y[5], 26 / 209 * y[0] - 156 / 209 * y[1] - 3 / 209 * y[2] + 168 / 209 * y[3] - 42 / 209 * y[4] + 7 / 209 * y[5], -7 / 209 * y[0] + 42 / 209 * y[1] - 168 / 209 * y[2] + 3 / 209 * y[3] + 156 / 209 * y[4] - 26 / 209 * y[5], 2 / 209 * y[0] - 12 / 209 * y[1] + 48 / 209 * y[2] - 180 / 209 * y[3] + 45 / 209 * y[4] + 97 / 209 * y[5], -1 / 209 * y[0] + 6 / 209 * y[1] - 24 / 209 * y[2] + 90 / 209 * y[3] - 336 / 209 * y[4] + 265 / 209 * y[5]]

		// Generate spline coefficients
		// Y[i](t) = a[i] + b[i] * t + c[i] * t^2 + d[i] * t^3
		var a = new Array(n),
			b = new Array(n),
			c = new Array(n),
			d = new Array(n)
		for (let i = 0; i < n; i++) {
			a[i] = y[i]
			b[i] = D[i]
			c[i] = 3 * (y[i + 1] - y[i]) - 2 * D[i] - D[i + 1]
			d[i] = 2 * (y[i] - y[i + 1]) + D[i] + D[i + 1]
		}

		// Generate interpolated values
		let res = result.length,
			iToX = n / (res - 1)
		for (let i = 0; i < res; i++) {
			let x = i * iToX,
				j = i === res - 1 ? n - 1 : Math.floor(x),
				t = x - j

			result[i] = a[j] + (b[j] + (c[j] + d[j] * t) * t) * t
		}
	}
})