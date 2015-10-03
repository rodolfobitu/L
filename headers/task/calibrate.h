#ifndef CALIBRATE_H
#define CALIBRATE_H

/*
 * Run the sensor calibration task, gathering the expected maximum and minimum
 * ADC value for each sensor and store the result in `uiSensorLimits`
 * This is synchronous (will return after the whole calibration is done)
 */
void calibrate_run(void);

#endif /* CALIBRATE_H */