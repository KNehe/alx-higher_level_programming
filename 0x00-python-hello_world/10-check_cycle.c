#include "lists.h"
/**
 * check_cycle - Detects a cycle in a linked list
 * @list: Pointer to head
 * Return: 1 if true else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *S = list, *F = list;

	if (!list)
		return (0);

	while (S && F && F->next)
	{
		S = S->next;
		F = F->next->next;
		if (F == S)
			return (1);
	}
	return (0);
}


