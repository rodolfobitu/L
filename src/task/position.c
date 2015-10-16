#include "L.h"
#include "adc.h"

extern unsigned int uiSensorLimits[NUM_OF_SENSORS][2];

float position_get(void) {
	unsigned int uiRawValue;
	char cChannel;
	float fValue,
		fValues[NUM_OF_SENSORS],
		fD[NUM_OF_SENSORS],
		fMinValue = 100,
		fMinPos;
	
	/* Read each ADC and normalize the result */
	for (cChannel = 0; cChannel < NUM_OF_SENSORS; cChannel++) {
		float fMin = (float)uiSensorLimits[cChannel][0],
			fMax = (float)uiSensorLimits[cChannel][1];
		uiRawValue = adc_get(cChannel);
		fValue = ((float)uiRawValue - fMin) / (fMax - fMin);
		if (fValue > 1) {
			fValue = 1;
		} else if (fValue < 0) {
			fValue = 0;
		}
		fValues[cChannel] = fValue;
	}
	
	/*
	 * Apply the spline algorithm
	 * From http://mathworld.wolfram.com/CubicSpline.html
	 * And using top calc (http://sitegui.com.br/topCalc):
	 * > n = 6
	 * > A = matrix(n, n, i, j, if(i==j, if(i==1||i==n, 2, 4), if(abs(i-j)==1, 1, 0)))
	 * > C = matrix(n, 1, i, j, if(i==1, y[1]-y[0], if(i==n, y[n-1]-y[n-2], y[i]-y[i-2])))
	 * > simplify(inverse(A)*3.0*C)
	 */
	
	/*
	 * Find the derivate in each point
	 */
	fD[0] = -1.267943 * fValues[0] +
		1.607656 * fValues[1] -
		0.430622 * fValues[2] +
		0.1148325 * fValues[3] -
		0.02870813 * fValues[4] +
		0.004784689 * fValues[5];
	fD[1] = -0.4641148 * fValues[0] -
		0.215311 * fValues[1] +
		0.861244 * fValues[2] -
		0.2296651 * fValues[3] +
		0.05741627 * fValues[4] -
		0.009569378 * fValues[5];
	fD[2] = 0.1244019 * fValues[0] -
		0.7464115 * fValues[1] -
		0.01435407 * fValues[2] +
		0.8038278 * fValues[3] -
		0.2009569 * fValues[4] +
		0.03349282 * fValues[5];
	fD[3] = -0.03349282 * fValues[0] +
		0.2009569 * fValues[1] -
		0.8038278 * fValues[2] +
		0.01435407 * fValues[3] +
		0.7464115 * fValues[4] -
		0.1244019 * fValues[5];
	fD[4] = 0.009569378 * fValues[0] -
		0.05741627 * fValues[1] +
		0.2296651 * fValues[2] -
		0.861244 * fValues[3] +
		0.215311 * fValues[4] +
		0.4641148 * fValues[5];
	fD[5] = -0.004784689 * fValues[0] +
		0.02870813 * fValues[1] -
		0.1148325 * fValues[2] +
		0.430622 * fValues[3] -
		1.607656 * fValues[4] +
		1.267943 * fValues[5];

	/*
	 * Generate spline coefficients and find minimum value and position
	 * Y[i](t) = fC0[i] + fC1[i] * t + fC2[i] * t^2 + fC3[i] * t^3
	 * Where fC0 = fValues, fC1 = D and fC2, fC3 depend on fValues and D
	 */
	for (cChannel = 0; cChannel < NUM_OF_SENSORS; cChannel++) {
		float fC0 = fValues[cChannel],
			fC1 = fD[cChannel],
			fC2 = 3 * (fValues[cChannel + 1] - fC0) - 2 * fC1 - fD[cChannel + 1],
			fC3 = 2 * (fC0 - fValues[cChannel + 1]) + fC1 + fD[cChannel + 1],
			fT;
		
		for (fT = 0; fT <= 1; fT += 0.01) {
			fValue = fC0 + (fC1 + (fC2 + fC3 * fT) * fT) * fT;
			if (fValue < fMinValue) {
				fMinValue = fValue;
				fMinPos = ((float)cChannel + fT) / 3.0 - 1.0;
			}
		}
	}
	
	return fMinPos;
}