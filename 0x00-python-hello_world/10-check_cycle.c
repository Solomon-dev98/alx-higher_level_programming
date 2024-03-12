#include "lists.h"

/**
 * check_cycle - a function that checks if a LL has a cycle
 * @list: a ptr var of type of listint_t
 * Return: 0 if no cycle is found or 1 if cycle is found
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
