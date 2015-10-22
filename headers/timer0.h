#ifndef TIMER0_H
#define TIMER0_H

void timer0_init(void);
void timer0_config(unsigned int uiTimeMs);
void timer0_reset(void);
unsigned int timer0_timeLeft(void);

#endif /* TIMER0_H */
