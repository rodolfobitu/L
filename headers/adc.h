#ifndef ADC_H
#define ADC_H

void adc_init(void);

/*
 * Read the ADC value in the given channel (0 to NUM_OF_SENSORS)
 * Return a value from 0 to 1023 (10 bits)
 */
unsigned int adc_get(char cChannel);

#endif /* ADC_H */