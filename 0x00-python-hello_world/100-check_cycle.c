#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	int i;
	listint_t *temp = list;

	if (list == NULL)
		return (0);
	for (i = 0; temp == NULL; i++)
	{
		temp = list->next;
		if (temp == list)
			return (1);
	}
	return (0);
}
