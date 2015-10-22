#ifndef UTIL_H
#define UTIL_H

/* Wait a multiple of 1ms, up to 10ms */
void util_genDelay1MS(char cN);

/* Wait a multiple of 10ms, up to 100ms */
void util_genDelay10MS(char cN);

/* Wait a multiple of 100ms, up to 1000ms */
void util_genDelay100MS(char cN);

#endif /* UTIL_H */