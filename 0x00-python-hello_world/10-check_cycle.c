#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
listint_t *slow, *fast;
if (!list || !list->next)
return (0);
slow = list;
fast = list->next;
while (slow != fast)
{
if (!fast || !fast->next)
return (0);
slow = slow->next;
fast = fast->next->next;
}
return (1);
}
