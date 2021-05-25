from recipe import Recipe

class Recipebook:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self):
        # 추가할 레시피 이름을 입력받자
        recipe_name = input('>> 레시피 이름을 입력하세요: ')
        # 중복을 체크하자
        for recipe in self.recipe_list:
        # 중복되는 레시피가 있으면
            if recipe_name == recipe.name:
            # 이미 있다고 알려주자
                print('이미 존재하는 레시피입니다! ')
                return
        # 중복되는 레시피가 없으면
        # 새 레시피 생성하자
        new_recipe = Recipe(recipe_name)
        new_recipe.set_recipe()
        # 레시피리스트에 추가하자
        self.recipe_list.append(new_recipe)

    def show_all_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'\n{index+1}번.')
            print(recipe)

    def search_recipe(self):
        # 찾을 레시피 이름을 입력받자
        recipe_name = input('>> 원하는 레시피를 검색하세요: ')
        searched_recipe = []
        # (반복문시작) 레시피 리스트를 돌면서 레시피 있는지 확인하자
        for recipe in self.recipe_list:
            # 찾는 레시피 이름이 있다면
            if recipe_name in recipe.name:  # if '부대' in '부대찌개' -> 찾을 수 있음
                # 그 레시피 보여주자
                print(recipe)
                searched_recipe.append(recipe)
        # (반복문 종료)
        # 찾는 레시피 이름이 없다면
        if len(searched_recipe) == 0:   # 못 찾음
            # 추가할지 물어보자
            choice = input('>> 원하는 레시피가 없습니다. 추가하시겠습니까? (1: 예, 0: 아니오)')
            # 추가한다고 하면
            if choice == '1':
                # 레시피 추가하자
                self.add_recipe()
            # 추가 안 한다고 하면
            else:
                return



    def __str__(self):
        pass

