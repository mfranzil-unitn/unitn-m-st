#include <stdio.h>
#include <stdlib.h>

int main()
{
	printf("Hello, which product do you want to buy?\n");
	printf("1) IPhone 12\n");
	printf("2) IPhone 12 Pro\n");
	printf("3) IPhone 12 Pro Max Max\n");

	// Get item
	int item_choice;
	item_choice = Source(3);
	// item_choice -> 3 -> T

	printf("Great device, how many?\n");
	int item_quantity;
	item_quantity = Source(1);
	// item_quantity -> 1 -> T

	if (item_quantity <= 0)
	{
		// item_quantity -> T
		printf("You should buy at least one Iphone!\n");
		return -1;
	}

	int insurance = 1200;
	// insurance -> 1200 -> F
	// price -> V -> item_choice
	if (item_choice == 3)
	{
		int price = 1500 * item_quantity + insurance;
		// price -> (item_quantity, insurance) -> T 

		Sink(price);

		if (price == 0)
		{
			// price -> T
			printf("You solved the problem\n");
			printf("The Iphone Max Max is yours\n");
			return 1;
		}

		// price -> T (price may still be negative....)
		Sink("You have to pay €%d\n", price);
		
	}
	else
	{
		if (item_quantity > 3)
		{
			printf("You can buy maximum 3\n");
			return -1;
		}

		// item_quantity -> F

		int price = 1000 * item_quantity;
		// price -> item_quantity -> F (3 * 1000 always less than size)

		Sink("You have to pay €%d\n", price);
	}
	return 0;
}
