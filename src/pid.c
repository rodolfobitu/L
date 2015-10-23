#include "pid.h"

PID pid_init(float fP, float fI, float fD, float fMinU, float fMaxU) {
	PID pid = {
		fP,
		fI,
		fD,
		0,
		0,
		fMinU,
		fMaxU,
		(fMaxU - fMinU)/fI
	};
	return pid;
}

float pid_update(PID *pid, float fRef, float fSensorValue) {
	float fError, fDiff, fErrorSum, fResult;
	
	/* Update the PID state */
	fError = fRef - fSensorValue;
	fErrorSum = (pid->fErrorSum += fError);
/*	if (fErrorSum > pid->fMaxAbsErrorSum) {
		fErrorSum = pid->fErrorSum = pid->fMaxAbsErrorSum;
	} else if (fErrorSum < -pid->fMaxAbsErrorSum) {
		fErrorSum = pid->fErrorSum = -pid->fMaxAbsErrorSum;
	}*/
	fDiff = fSensorValue - pid->fLast;
	pid->fLast = fSensorValue;
	
	fResult = (pid->fP * fError) + (pid->fI * fErrorSum) + (pid->fD * fDiff);
	if (fResult < pid->fMinU) {
		fResult = pid->fMinU;
	} else if (fResult > pid->fMaxU) {
		fResult = pid->fMaxU;
	}

	return fResult;
}