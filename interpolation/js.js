'use strict'

/** @const {number} */
const numPoints = 6

/** @const {number} */
const resolution = 1e3

/**
 * The point values (from 0 to 100)
 * @var {Array<number>}
 */
let points = new Array(numPoints).fill(50)

/** @var {HTMLCanvasElement} */
let canvas = null

/** @var {CanvasRenderingContext2D} */
let context = null

/** @var {number} */
let width = 0

/** @var {number} */
let height = 0

/** @var {Array<{name: string, handler: function(Array<number>):Array<number>}>} */
let algorithms = []

/**
 * `null` if no point is being dragged, point
 * position (`i`) otherwise
 * @var {?number}
 */
let dragging = null

/**
 * @var {boolean}
 */
let waitingDraw = false

window.addEventListener('resize', resizeCanvas)
window.addEventListener('load', init)

/**
 * Start the app
 */
function init() {
	canvas = document.getElementById('canvas')
	context = canvas.getContext('2d')
	resizeCanvas()
	canvas.addEventListener('mousedown', handleMouseDown)
	canvas.addEventListener('mousemove', handleMouseMove)
	canvas.addEventListener('mouseup', handleMouseUp)
	timeAlgorithms()
}

/**
 * Handle canvas resizing
 */
function resizeCanvas() {
	width = canvas.width = canvas.clientWidth
	height = canvas.height = canvas.clientHeight
	requestDraw()
}

/**
 * Redraw the canvas content
 */
function draw() {
	waitingDraw = false

	// Reset
	context.clearRect(0, 0, width, height)

	// Draw interpolations
	let result = new Array(resolution)
	algorithms.forEach(({
		name,
		handler,
		color,
		time
	}) => {
		let globalMaxX = 0,
			globalMaxY = 0

		context.beginPath()
		handler(points, result)
		result.forEach((value, i) => {
			let {
				x, y
			} = toCanvasXY(i * (numPoints - 1) / (resolution - 1), value)
			if (i) {
				context.lineTo(x, y)
			} else {
				context.moveTo(x, y)
			}
			if (y > globalMaxY) {
				globalMaxX = x
				globalMaxY = y
			}
		})
		context.strokeStyle = color
		context.stroke()

		context.beginPath()
		context.arc(globalMaxX, globalMaxY, 7, 0, 2 * Math.PI)
		context.stroke()
		context.fillText(name + ' (' + time + 'ms)', globalMaxX + 5, globalMaxY - 5)
	})

	// Draw points
	points.forEach((p, i) => {
		let {
			x, y
		} = toCanvasXY(i, p)
		context.beginPath()
		context.arc(x, y, 5, 0, 2 * Math.PI)
		context.fill()
	})
}

/**
 * Return the i-th point coordinates in canvas space
 * @param {number} i
 * @param {number} value
 * @returns {{x: number, y: number}}
 */
function toCanvasXY(i, value) {
	return {
		x: width / (numPoints + 1) * (i + 1),
		y: height * (0.1 + 0.8 * value / 100)
	}
}

/**
 * Convert from canvas space to point space
 * @param {number} x
 * @param {number} y
 * @returns {{i: number, isNear: boolean, value: number}}
 */
function fromCanvasXY(x, y) {
	let value = 100 * (y / height - 0.1) / 0.8,
		rawI = x / width * (numPoints + 1) - 1,
		nearestI = Math.min(Math.max(0, Math.round(rawI)), numPoints - 1)
	return {
		i: nearestI,
		isNear: Math.abs(nearestI - rawI) < 0.1,
		value: Math.min(Math.max(0, value), 100)
	}
}

/**
 * @param {MouseEvent} event
 */
function handleMouseDown(event) {
	let {
		i, isNear
	} = fromCanvasXY(event.clientX, event.clientY)

	if (!isNear) {
		return
	}

	dragging = i
	handleMouseMove(event)
}

/**
 * @param {MouseEvent} event
 */
function handleMouseMove(event) {
	if (dragging === null) {
		return
	}

	points[dragging] = fromCanvasXY(event.clientX, event.clientY).value
	requestDraw()
}

/**
 * @param {MouseEvent} event
 */
function handleMouseUp(event) {
	handleMouseMove(event)
	dragging = null
}

/**
 * Schedule the drawing
 */
function requestDraw() {
	if (!waitingDraw) {
		waitingDraw = true
		window.requestAnimationFrame(draw)
	}
}

/**
 * Measure execution time for all suplied algorithms
 */
function timeAlgorithms() {
	let result = new Array(1e3 * resolution)
	algorithms.forEach(each => {
		let startTime = Date.now()
		each.handler(points, result)
		each.time = Date.now() - startTime
	})
}