import dataclasses
from dataclasses import asdict
from html.parser import endtagfind
from http.client import responses
from itertools import product
from lib2to3.pgen2.tokenize import endprogs

import pytest
from unicodedata import category

from routes.Routes import Routes
import requests
import json
from payloads.Payload import Payload

class TestProductAPIs:
    @pytest.fixture(autouse=True)
    def init_method(self):
        self.base_url=Routes.BASE_URL
        self.payload=Payload().product_payload()

    def test_get_all_products(self):
        response=requests.get(self.base_url+Routes.GET_ALL_PRODUCTS)
        # print(json.dumps(response.json(),indent=4))
        products=response.json()['products']
        # category=response.json()['products']
        print(len(products))
        categories=[]
        products=response.json()['products']
        for i in range(len(products)-1):
            if products[i]['category'] not in categories:
                categories.append(products[i]['category'])
        print(categories)
        assert response.status_code == 200
        data=response.json()
        assert 'products' in data
        assert isinstance(data['products'], list)
        assert len(data['products']) > 0
        product = data['products'][0]
        assert 'id' in product
        assert 'title' in product
        assert 'price' in product
        assert isinstance(product['price'], (int, float))

    def test_get_single_product(self):
        id='2'
        endpoint=Routes.GET_SINGLE_PRODUCT.format(id=id)
        response=requests.get(f'{self.base_url}{endpoint}')
        # print(json.dumps(response.json(),indent=4))
        data=response.json()
        assert response.status_code==200
        assert data['id'] == int(id)
        assert 'title' in data
        assert 'price' in data

    def test_search_product(self):
        data={
            'q':'phone'
        }
        response=requests.get(self.base_url+Routes.SEARCH_PRODUCT,params=data)
        # print(json.dumps(response.json(),indent=4))
        products=response.json()['products']
        print(len(products))
        assert response.status_code==200

    def test_limit_skip_products(self):
        data={
            'limit':10,
            'skip':10,
            'select':'title,price'
        }

        response = requests.get(self.base_url + Routes.LIMIT_SKIP_PRODUCTS, params=data)
        print(json.dumps(response.json(),indent=4))
        products = response.json()['products']
        print(len(products))
        assert response.status_code == 200

    def test_sort_products(self):
        data={
            'sortBy':'title',
            'order':'asc'
        }

        response=requests.get(self.base_url+Routes.SORT_PRODUCTS,params=data)
        # print(json.dumps(response.json(),indent=4))
        assert response.json()['limit']==30
        assert len(response.json()['products'])==30
        assert response.status_code==200

    def test_get_all_product_categories(self):
        category='categories'
        response=requests.get(f'{self.base_url}{Routes.GET_ALL_PRODUCT_CATEGORIES}/{category}')
        print(json.dumps(response.json(),indent=4))
        assert response.status_code==200

    def test_get_product_category_list(self):
        category='category-list'
        response=requests.get(f'{self.base_url}{Routes.GET_ALL_PRODUCT_CATEGORIES}/{category}')
        print(json.dumps(response.json(),indent=4))
        assert response.status_code==200

    def test_get_product_by_category(self):
        category='category'
        category_selection='smartphones'
        response=requests.get(f'{self.base_url}{Routes.GET_PRODUCTS_BY_CATEGORY}/{category}/{category_selection}')
        # print(json.dumps(response.json(),indent=4))
        products=response.json()['products']
        for i in range(len(products)-1):
            if 'smartphones' in products[i]['category']:
                assert True
        print(response.json()['products'][1]['category'])
        assert response.status_code==200
        print(len(response.json()['products']))
        assert len(response.json()['products'])==16

    def test_add_a_new_product(self):
        response=requests.post(self.base_url+Routes.ADD_NEW_PRODUCT,json=dataclasses.asdict(self.payload))
        print(json.dumps(response.json(),indent=4))

    def test_update_a_product(self):
        data = {
            "title": "Updated Title"
        }
        endpoint=Routes.UPDATE_PRODUCT.format(id=1)
        response=requests.put(self.base_url+endpoint,json=data)
        print(json.dumps(response.json(),indent=4))

    def test_delete_product(self):
        endpoint=Routes.DELETE_A_PRODUCT.format(id=1)
        response=requests.delete(self.base_url+endpoint)
        print(json.dumps(response.json(),indent=4))
        assert response.json()['isDeleted']==True

class TestCartAPIs:
    @pytest.fixture(autouse=True)
    def init_method(self):
        self.base_url=Routes.BASE_URL
        self.cart_payload = Payload().cart_product_details_payload()

    def test_get_all_carts(self):
        response=requests.get(self.base_url+Routes.GET_ALL_CARTS)
        print(json.dumps(response.json(),indent=4))
        assert response.status_code==200

    def test_get_a_single_cart(self):
        endpoint=Routes.GET_SINGLE_CART.format(id=3)
        response=requests.get(self.base_url+endpoint)
        print(json.dumps(response.json(),indent=4))
        assert response.status_code==200

    def test_get_carts_by_user(self):
        endpoint=Routes.GET_CARTS_BY_USER.format(id=5)
        response=requests.get(self.base_url+endpoint)
        assert response.status_code==200
        print(json.dumps(response.json()))

    def test_add_a_new_cart(self):
        response=requests.post(self.base_url+Routes.ADD_A_NEW_CART,json=dataclasses.asdict(self.cart_payload))
        print(json.dumps(response.json(),indent=4))

    def test_update_cart(self):
        data={
            "title": "Updated Title"
        }
        endpoint=Routes.UPDATE_A_CART.format(id=3)
        response=requests.put(self.base_url+endpoint,json=data)
        print(json.dumps(response.json(),indent=4))

    def test_delete_cart(self):
        endpoint=Routes.DELETE_A_CART.format(id=2)
        response=requests.delete(self.base_url+endpoint)
        print(json.dumps(response.json(),indent=4))

class TestRecipesAPIs:

    @pytest.fixture(autouse=True)
    def init_method(self):
        self.base_url=Routes.BASE_URL
        self.recipe=Payload().recipes_payload()

    def test_get_all_recipes(self):
        response=requests.get(self.base_url+Routes.GET_ALL_RECIPES)
        assert response.status_code==200
        print(json.dumps(response.json(),indent=4))

    def test_get_a_single_recipe(self):
        endpoint=Routes.GET_A_SINGLE_RECIPE.format(id=2)
        response=requests.get(self.base_url+endpoint)
        assert response.status_code==200

    def test_search_recipes(self):
        data={
            'q':'Margherita'
        }
        response=requests.get(self.base_url+Routes.SEARCH_RECIPES,params=data)
        print(json.dumps(response.json(),indent=4))
        assert response.status_code==200

    def test_limit_skip_recipes(self):
        data={
            'limit':10,
            'skip':10,
            'select':'name,image'
        }
        response=requests.get(self.base_url+Routes.LIMIT_AND_RECIPES,params=data)
        print(json.dumps(response.json(),indent=4))
        assert response.status_code==200

    def test_sort_recipes(self):
        data={
            'sortBy':'name',
            'order':'asc'
        }
        response=requests.get(self.base_url+Routes.SORT_RECIPES,params=data)
        assert response.status_code==200
        print(json.dumps(response.json(),indent=4))
        response_json = response.json()
        recipes = response_json['recipes']
        recipe_names = [recipe['name'] for recipe in recipes]
        assert recipe_names == sorted(recipe_names), "Recipes are not sorted in ascending order"

    def test_get_all_recipes_tags(self):
        response=requests.get(self.base_url+Routes.GET_ALL_RECIPES_TAGS)
        print(json.dumps(response.json(),indent=4))
        assert response.status_code==200

    def test_get_by_a_tag(self):
        country='Indian'
        response=requests.get(f'{self.base_url}{Routes.GET_RECIPES_BY_A_TAG}/{country}')
        print(json.dumps(response.json(),indent=4))
        assert response.status_code==200

    def test_get_by_a_meal(self):
        endpoint=Routes.GET_RECIPES_BY_A_MEAL.format(meal_name='snack')
        response=requests.get(self.base_url+endpoint)
        assert response.status_code==200

    def test_add_new_recipe(self):
        response=requests.post(self.base_url+Routes.ADD_RECIPE,json=dataclasses.asdict(self.recipe))
        print(json.dumps(response.json(),indent=4))

    def test_update_recipe(self):
        data={
            'name':'the name is updated'
        }
        endpoint=Routes.UPDATE_RECIPE.format(id=2)
        response=requests.put(self.base_url+endpoint,json=data)
        print(json.dumps(response.json(),indent=4))

    def test_delete_recipe(self):
        endpoint=Routes.DELETE_RECIPE.format(id=2)
        response=requests.delete(self.base_url+endpoint)
        print(json.dumps(response.json(),indent=4))

class TestAuthAPIs:
    HEADERS={
        'Content-Type':'application/json'
    }
    accessToken=None
    refreshToken=None

    @pytest.fixture(autouse=True)
    def init_method(self):
        self.base_url=Routes.BASE_URL

    def test_login_user_and_get_tokens(self):
        body={
            'username':'emilys',
            'password':'emilyspass',
            'expiresInMins':30
        }
        response=requests.post(self.base_url+Routes.LOGIN_USER_AND_GET_TOKENS,data=json.dumps(body),headers=self.HEADERS)
        print(json.dumps(response.json(),indent=4))
        data=response.json()
        TestAuthAPIs.accessToken=data['accessToken']
        TestAuthAPIs.refreshToken=data['refreshToken']
        # print(self.accessToken)

    def test_get_current_user(self):
        access_Token=self.accessToken
        print(access_Token)
        headers={
            'Authorization':f'Bearer {access_Token}'
        }
        response=requests.get(self.base_url+Routes.GET_CURRENT_AUTH_USER,headers=headers)
        print(json.dumps(response.json(),indent=4))
        data=response.json()
        assert 'emilys' in data['username']

    def test_refresh_auth_session(self):
        refresh_token=self.refreshToken
        body={
            'refreshToken':f'{refresh_token}',
            'expiresInMins':30
        }
        response=requests.post(self.base_url+Routes.REFRESH_AUTH_SESSION,data=json.dumps(body),headers=self.HEADERS)
        print(json.dumps(response.json(),indent=4))
        data=response.json()
        assert data['accessToken']!=self.accessToken
        assert data['refreshToken']!=refresh_token

class TestUserAPIs:
    accessToken=None
    refreshToken=None

    HEADERS = {
        'Content-Type': 'application/json'
    }

    @pytest.fixture(autouse=True)
    def init_method(self):
        self.base_url=Routes.BASE_URL

    def test_get_all_users(self):
        response=requests.get(self.base_url+Routes.GET_ALL_USERS)
        print(json.dumps(response.json(),indent=4))
        assert response.status_code==200

    def test_login_user_get_tokens(self):
        body={
            'username':'emilys',
            'password':'emilyspass',
            'expiresInMins':30
        }
        response=requests.post(self.base_url+Routes.LOGIN_USER_AND_GET_TOKENS2,data=json.dumps(body),headers=self.HEADERS)
        print(json.dumps(response.json(),indent=4))
        data=response.json()
        TestUserAPIs.accessToken=data['accessToken']
        TestUserAPIs.refreshToken=data['refreshToken']

    def test_get_current_authenticated_user(self):
        access_token=self.accessToken
        header={
            'Authorization':f'Bearer {access_token}'
        }
        response=requests.get(self.base_url+Routes.GET_CURRENT_AUTHENTICATED_USER,headers=header)
        print(json.dumps(response.json(),indent=4))
        data=response.json()
        assert 'Emily' in data['firstName']

    def test_get_a_single_user(self):
        endpoint=Routes.GET_A_SINGLE_USER.format(id=2)
        response=requests.get(self.base_url+endpoint)
        data=response.json()
        print(json.dumps(data,indent=4))
        assert '2' in data['id']

    def test_search_users(self):
        data={
            'q':'John'
        }
        response=requests.get(self.base_url+Routes.SEARCH_USER,params=data)
        print(json.dumps(response.json()))
        assert response.status_code==200

    






