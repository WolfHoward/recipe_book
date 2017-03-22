# Wolf wants to build a recipe book that will tell him how much it costs him
# to produce an infusion given the ingredients and amounts used

# First he builds his recipe book by adding each of his drink recipes to his
# Database of products.

## He starts a new recipe by pressing the 'add recipe' button.
def add_recipe():
    title = input('Title: ')

    state = True
    while state == True:
        ingredient = input('Enter an ingredient for the recipe: ')

        if ingredient == 'n':
            state = False
            return(recipe)

        amount = input('Amount: ')
        unit = input('Units: ')
        recipe = "In the middle."

    recipe = "What's a testing goat?"
    return(recipe)

operation = int(input('''Press 1 to add recipe:
>   '''))

if operation == 1:
    recipe_ret = add_recipe()
    print(recipe_ret)




## The first item on the page is a box with the word 'TITLE'.
## Wolf clicks the box and the 'TITLE' placeholder disappears.
## He types 'Blackberry Gin'.

## There is a heading for 'INGREDIENTS', with an outline of a box and a '+'
## to add a new ingredient. There are empty columns across the top.
## They read: 'Amount', 'Ingredient', 'Cost per Unit', & 'Cost per Production'
## Below this, there's a 'DIRECTIONS' heading, with an outline fo a box and a
## '+' in case the user wants to add directions to the recipe.

## Wolf chooses to add an ingredient, a 750 mL bottle of Regatta Bay Gin.
## When he touches the '+' button, a template appears.

## There is an 'Amount' column, which has an empty text box and a dropdown of possible units.

## The next column is 'Ingredient', which has a dropdown option and allows
## the user to type any ingredient they would like. The box autofills
## as the user types if there is a partial match to an ingredient already used in the
## recipe book or in the native database. Otherwise, it adds the ingredient
## to the user's local database.

## At the far right of the box is a 'check mark' button and an 'x' button.
## Touching the 'check' will place the ingredient in the list.
## Touching the 'x' cancels the addition.

## Wolf fills in '750' and selects 'mL'. He types 'Regatta Bay', which is a new addition.
## He pressess the check mark. The item is added under the 'INGREDIENTS' heading.

## The 'Cost per Unit' column autofills with the price of 'Regatta Bay' per mL.
## The 'Cost per Production' column autofills with the cost per unit multiplied
## by the unit used.

## He touches the button again. This time he adds '2' 'pint' of 'Blackberries'.

## With a third touch, he adds 'Sugar', though he isn't sure how much he used.
## He inputs '2' 'Tbsp' as an estimate.


## Wolf moves on to the (optional) directions column, which he fills in with step by step
## instructions for the process he uses to make the recipe. He finishes each new step
## by clicking another check mark and pressing the next '+' button in the ordered list.

## Once he has all of his recipe information in, he saves the recipe to his book


## The recipe appears on his 'My Recipes' page, which has the following columns:
    ## 'Title',
    ## 'Date Last Prepped'
    ## 'Amount Last Prepped'
    ## 'Expected Yield'
    ## 'Cost of Last Production'
    ## 'Average Cost per Production'
    ## 'Average Amount per Production'
