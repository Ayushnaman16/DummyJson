class Routes:
    BASE_URL="https://dummyjson.com"

    #products
    GET_ALL_PRODUCTS="/products"
    GET_SINGLE_PRODUCT="/products/{id}"
    SEARCH_PRODUCT="/products/search"
    LIMIT_SKIP_PRODUCTS="/products"
    SORT_PRODUCTS="/products"
    GET_ALL_PRODUCT_CATEGORIES="/products"
    GET_PRODUCT_CATEGORY_LIST="/products"
    GET_PRODUCTS_BY_CATEGORY="/products"
    ADD_NEW_PRODUCT="/products/add"
    UPDATE_PRODUCT="/products/{id}"
    DELETE_A_PRODUCT="/products/{id}"

    #carts
    GET_ALL_CARTS='/carts'
    GET_SINGLE_CART='/carts/{id}'
    GET_CARTS_BY_USER='/carts/user/{id}'
    ADD_A_NEW_CART='/carts/add'
    UPDATE_A_CART='/carts/{id}'
    DELETE_A_CART='/carts/{id}'

    #recipes
    GET_ALL_RECIPES='/recipes'
    GET_A_SINGLE_RECIPE='/recipes/{id}'
    SEARCH_RECIPES='/recipes/search'
    LIMIT_AND_RECIPES='/recipes'
    SORT_RECIPES='/recipes'
    GET_ALL_RECIPES_TAGS='/recipes/tags'
    GET_RECIPES_BY_A_TAG='/recipes/tag'
    GET_RECIPES_BY_A_MEAL='/recipes/meal-type/{meal_name}'
    ADD_RECIPE='/recipes/add'
    UPDATE_RECIPE='/recipes/{id}'
    DELETE_RECIPE="/recipes/{id}"

    #Auth
    LOGIN_USER_AND_GET_TOKENS='/auth/login'
    GET_CURRENT_AUTH_USER='/auth/me'
    REFRESH_AUTH_SESSION='/auth/refresh'

    #users
    GET_ALL_USERS='/users'
    LOGIN_USER_AND_GET_TOKENS2='/user/login'
    GET_CURRENT_AUTHENTICATED_USER='/user/me'
    GET_A_SINGLE_USER='/users/{id}'
    SEARCH_USER='/users/search'
    FILTER_USER='/users/filter'
    LIMIT_AND_SKIP_USERS='/users'
    SORT_AND_ORDER_USERS='/users'
    GET_USER_CARTS_BY_USER_ID='/users/{id}/carts'
    GET_USER_POST_BY_USER_ID='/users/{id}/posts'
    GET_USER_TODOS_BY_USER_ID='/users/{id}/todos'
    ADD_A_NEW_USER='/users/add'
    UPDATE_USER='/users/{id}'
    DELETE_USER='/users/{id}'



