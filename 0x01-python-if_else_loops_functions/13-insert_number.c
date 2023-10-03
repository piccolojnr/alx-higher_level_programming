#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a new node at the beginning of a listint_t list.
 * @head: pointer to the head of the list
 * @number: integer to be inserted
 *
 * Return: the address of the new element, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *previous = NULL;
	listint_t *new;

	while (current && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);


	new->n = number;

	new->next = current;

	if (current == *head)
		*head = new;
	else
		previous->next = new;


	return (new);
}
