

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if no cycle, 1 if cycle is present
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

