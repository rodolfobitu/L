#include "pid.h"

PID pid_init(float fP, float fI, float fD, float fMinU, float fMaxU) {
	PID pid = {
		fP,
		fI,
		fD,
		0,
		0,
		fMinU,
		fMaxU
	};
	return pid;
}

float pid_update(PID *pid, float fRef, float fSensorValue) {
	float fError, fDiff, fErrorSum, fResult;
	
	/* Update the PID state */
	fError = fRef - fSensorValue;
	fErrorSum = (pid->fErrorSum += fError);
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