# from dis import disco
#
# from faker import Faker
# import random
#
# from unicodedata import category
#
# from datamodels.Images import Images
# from datamodels.Dimensions import Dimensions
# from datamodels.Individual_Review import IndividualReview
# from datamodels.Meta import Meta
# from datamodels.Product_list import Product_list
# from datamodels.Products import Products
# from datamodels.Reviews import Reviews
# from datamodels.Tags import Tags
# from datetime import datetime
#
# class Payload:
#     faker=Faker()
#     categories=['beauty', 'fragrances', 'furniture', 'groceries']
#
#     def product_payload(self) ->Products:
#         product=Product_list(
#             id=random.randint(0,100),
#             title=self.faker.items(),
#             description=self.faker.text(),
#             category=random.choice(self.categories),
#             price=ra,
#             discount=random.randint(0,10)+random.random(),
#             rating=random.randint(0,5)+random.random(),
#             stock=random.randint(0,100),
#             tag1=self.faker.text(),
#             tag2=self.faker.text(),
#             tags=Tags(tag1,tag2),
#         )
#
#
#         product_list = Product_list()
#
#
#
#

from faker import Faker
import random
from datetime import datetime
from typing import List

from Fake_Store_API.datamodels.Dimensions import Dimensions
from Fake_Store_API.datamodels.Individual_Review import IndividualReview
from Fake_Store_API.datamodels.Meta import Meta
from Fake_Store_API.datamodels.Product_list import Product_list
from Fake_Store_API.datamodels.Products import Products
from Fake_Store_API.datamodels.Product_details import Product_details
from Fake_Store_API.datamodels.Cart import Cart
from Fake_Store_API.datamodels.Recipes import Recipes
from Fake_Store_API.datamodels.User import User
from Fake_Store_API.datamodels.Address import Address
from Fake_Store_API.datamodels.Bank import Bank
from Fake_Store_API.datamodels.Company import Company
from Fake_Store_API.datamodels.Coordinates import Coordinate
from Fake_Store_API.datamodels.Crypto import Crypto
from Fake_Store_API.datamodels.Hair import Hair

class Payload:
    faker = Faker()
    categories = ['beauty', 'fragrances', 'furniture', 'groceries']
    difficulties=['easy','medium','hard']
    meal_types=['breakfast','lunch','snacks','dinner']

    def product_payload(self) -> Product_list:
        product = Product_list(
            id=random.randint(1, 1000),
            title=self.faker.word(),
            description=self.faker.text(),
            category=random.choice(self.categories),
            price=round(random.uniform(10, 500), 2),
            discountPercentage=round(random.uniform(1, 20), 2),
            rating=round(random.uniform(1, 5), 2),
            stock=random.randint(1, 100),

            tags=[self.faker.word(), self.faker.word()],

            brand=self.faker.company(),
            sku=self.faker.bothify(text='????####'),
            weight=random.randint(1, 10),

            dimensions=Dimensions(
                width=round(random.uniform(1, 50), 2),
                height=round(random.uniform(1, 50), 2),
                depth=round(random.uniform(1, 50), 2)
            ),

            warrantyInformation="1 month warranty",
            shippingInformation="Ships in 3-5 days",
            availabilityStatus="In Stock",

            reviews=[
                IndividualReview(
                    rating=random.randint(1, 5),
                    comment=self.faker.sentence(),
                    date=datetime.now().isoformat(),
                    reviewerName=self.faker.name(),
                    reviewerEmail=self.faker.email()
                )
                for _ in range(2)
            ],

            returnPolicy="30 days return policy",
            minimumOrderQuantity=random.randint(1, 50),

            meta=Meta(
                createdAt=datetime.now().isoformat(),
                updatedAt=datetime.now().isoformat(),
                barcode=str(random.randint(1000000000, 9999999999)),
                qrCode="dummy_qr_code"
            ),

            thumbnail="https://dummyimage.com/thumbnail.jpg",
            images=[
                "https://dummyimage.com/1.jpg",
                "https://dummyimage.com/2.jpg"
            ]
        )

        return product

    def cart_product_details_payload(self) -> Cart:
        cart_details=Cart(
            id=random.randint(1,10),
            products=[
                Product_details(
                id=random.randint(1,1000),
                title=self.faker.word(),
                price=round(random.uniform(10, 500), 2),
                quantity=random.randint(1,50),
                total=round(random.uniform(10, 500), 2),
                discountPercentage=round(random.uniform(1, 20), 2),
                discountedTotal=round(random.uniform(50, 200), 2),
                thumbnail="https://dummyimage.com/thumbnail.jpg"
        )],
            total=round(random.uniform(1000, 5000), 2),
            discountedTotal=random.randint(1000,5000),
            userId=random.randint(1,20),
            totalProducts=random.randint(1,20),
            totalQuantity=random.randint(1,20)
        )
        return cart_details

    def recipes_payload(self) -> Recipes:
        recipe=Recipes(
            id=random.randint(1,10),
            name=self.faker.word(),
            ingredients=["Pizza dough",
    "Tomato sauce",
    "Fresh mozzarella cheese",
    "Fresh basil leaves",
    "Olive oil",
    "Salt and pepper to taste"],
            instructions=["Preheat the oven to 475°F (245°C).",
    "Roll out the pizza dough and spread tomato sauce evenly.",
    "Top with slices of fresh mozzarella and fresh basil leaves.",
    "Drizzle with olive oil and season with salt and pepper.",
    "Bake in the preheated oven for 12-15 minutes or until the crust is golden brown.",
    "Slice and serve hot."],
            prepTimeMinutes=random.randint(1,20),
            cookTimeMinutes=random.randint(1,20),
            servings=random.randint(1,10),
            difficulty=random.choice(self.difficulties),
            cuisine=self.faker.country(),
            caloriesPerServing=random.randint(100,510),
            tags=["Pizza",
    "Italian"],
            userId=random.randint(1,10),
            image="https://dummyimage.com/thumbnail.jpg",
            rating=round(random.uniform(1, 5), 2),
            reviewCount=random.randint(1,5),
            mealType=[random.choice(self.meal_types)]
        )

        return recipe

    def user_payload(self) ->User:
        address = Address(
            address=self.faker.street_address(),
            city=self.faker.city(),
            state=self.faker.state(),
            stateCode=self.faker.state_abbr(),
            postalCode=self.faker.postcode(),
            coordinates=Coordinate(
                lat=random.uniform(-90, 90),
                lng=random.uniform(-180, 180)
            ),
            country=self.faker.country()
        )

        company = Company(
            department=self.faker.job(),
            name=self.faker.company(),
            title=self.faker.job(),
            address=address  # reuse or create new if needed
        )

        user = User(
            id=random.randint(1, 1000),
            firstName=self.faker.first_name(),
            lastName=self.faker.last_name(),
            maidenName=self.faker.last_name(),
            age=random.randint(18, 60),
            gender=random.choice(["male", "female"]),
            email=self.faker.email(),
            phone=self.faker.phone_number(),
            username=self.faker.user_name(),
            password=self.faker.password(),
            birthDate=str(self.faker.date_of_birth()),
            image="https://dummyimage.com/user.jpg",
            bloodGroup=random.choice(["A+", "B+", "O+", "AB+"]),
            height=round(random.uniform(150, 200), 2),
            weight=round(random.uniform(50, 100), 2),
            eyeColor=random.choice(["Blue", "Green", "Brown"]),
            hair=Hair(
                color=random.choice(["Black", "Brown", "Blonde"]),
                type=random.choice(["Straight", "Curly", "Wavy"])
            ),
            ip=self.faker.ipv4(),
            address=address,
            macAddress=self.faker.mac_address(),
            university=self.faker.company(),
            bank=Bank(
                cardExpire="03/26",
                cardNumber=self.faker.credit_card_number(),
                cardType="Visa",
                currency="USD",
                iban=self.faker.iban()
            ),
            company=company,
            ein=str(random.randint(100, 999)) + "-" + str(random.randint(100, 999)),
            ssn=self.faker.ssn(),
            userAgent=self.faker.user_agent(),
            crypto=Crypto(
                coin="Bitcoin",
                wallet=self.faker.sha256(),
                network="Ethereum (ERC20)"
            ),
            role=random.choice(["admin", "moderator", "user"])
        )

        return user


