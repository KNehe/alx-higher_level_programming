#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks is linked list is a palindrome
 * @head: Double pointer to head
 * Return: 1 if true else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *c1, *c2;
	unsigned int len = 0, i = 0;
	int arr[1024];

	/* if head is null hence no list, no palindrome */
	if (head == NULL)
		return (0);
	/* if head is empty then palindrome */
	if (*head == NULL)
		return (1);
	c1 = *head;
	c2 = *head;
	/* find length of linked list */
	while (c1 != NULL)
	{
		c1 = c1->next;
		len++;
	}
	/* one item is panlindrome */
	if (len == 1)
		return (1);
	/* assign numbers to array */
	for (i = 0; c2 != NULL; i++)
	{
		arr[i] = c2->n;
		c2 = c2->next;
	}
	/* compare start of array with end of array */
	len = len - 1;
	for (i = 0; i <= len / 2; i++)
	{
		if (arr[i] != arr[len - i])
			return (0);
	}
	return (1);
}
