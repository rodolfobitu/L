#ifndef POSITION_H
#define POSITION_H

/*
 * Find the line position, based on IR sensors, normalizing
 * their ADC values using uiSensorLimits
 * Return a value from -1 to 1 (0 = in the middle)
 */
float position_get(void);

#endif /* POSITION_H */