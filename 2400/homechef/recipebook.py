from recipe import Recipe

class RecipeBook:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self):
        # 추가할 레시피 이름 입력받자
        name = input('>> 레시피 이름을 입력하세요: ')
        # 중복 체크 하자
        for recipe in self.recipe_list:
        # 중복되는 레시피가 있으면
            if name == recipe.name:
            # 중복된다고 알려주자
                print('이미 존재하는 레시피입니다!')
                return
        # 중복되는 레시피가 없으면
        # 레시피 생성하기
        new_recipe = Recipe(name)
        new_recipe.set_recipe()
        # 레시피리스트에 생성한 레시피 추가하기
        self.recipe_list.append(new_recipe)

    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index+1}')
            print(recipe)

    # 레시피북에서 레시피 찾기
    def search_recipe(self):
        searched_recipe = []
        # 레시피 이름을 검색하자(입력받자)
        name = input('>> 원하는 레시피를 검색하세요: ')
        # (반복문 시작) 레시피 리스트를 돌면서 레시피 확인
        for recipe in self.recipe_list:
            # 레시피의 이름이 검색받은 이름과 같다면 (찾았으면)
            if name == recipe.name:
                # 그 레시피 보여주자
                print(recipe)
                searched_recipe.append(recipe)
        # 검색된 레시피가 없다면 (searched_recipe가 비어있다면)
        if len(searched_recipe) == 0:
            # 추가할지 물어보자
            answer = int(input('>> 찾는 레시피가 없습니다. 추가하시겠습니까? (1: 예, 0: 아니오) '))
            # 추가한다고 하면
            if answer == 1:
                # 레시피 추가하기
                self.add_recipe()
            else:
                return








    def __str__(self):
        pass
