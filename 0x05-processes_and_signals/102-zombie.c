#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Creates 5 zombie processes from infinite_while
 * Return: 0
 */
int main(void)
{
	int zombie = 1;
	pid_t child_pid;

	while (zombie <= 5)
	{
		child_pid = fork();
		if (child_pid == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", child_pid);
		zombie++;
	}

	infinite_while();

	return (0);
}
