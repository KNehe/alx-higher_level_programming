#include "lists.h"
/**
 * insert_node - inserts a node in sorted linked list
 * @head: Double pointer to head
 * @number: Number to be inserted in list
 * Return: New node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp, *new;

	current = *head, temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (temp == NULL)
		return (NULL);
	if (temp->n >= number)
	{
		new->n = number;
		new->next = temp;
		*head = new;
		return (new);
	}
	while (current->next)
	{
		current = current->next;
		if (current->n >= number)
		{
			new->n = number;
			new->next = current;
			temp->next = new;
			return (new);
		}
		else
			temp = temp->next;
	}
	return (new);
}
