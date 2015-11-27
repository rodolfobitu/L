#ifndef PID_H
#define PID_H

typedef struct PID {
	float fP, fI, fD;
	float fErrorSum;
	float fLast;
	float fMinU;
	float fMaxU;
} PID;

/* Create a PID instance using MinU and MaxU as saturation limits */
PID pid_init(float fP, float fI, float fD, float fMinU, float fMaxU);

/* 
 * Update the PID state and return the control signal 
 * fMinU <= return <= fMaxU
 */
float pid_update(PID *pid, float fRef, float fSensorValue);

#endif /* PID_H */