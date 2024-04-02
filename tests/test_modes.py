from django.test import TestCase
from bbs.models import Board, Category, Client_Request
from django.contrib.auth.models import User

class BbsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(code= "test01",name="테스트 카테고리")
        user = User.objects.create(username="테스트 사용자")
        Board.objects.create(title="테스트 제목", content="테스트 내용", category=category, author=user)

    def test_title_content(self):
        board = Board.objects.get(id=1)
        expected_object_name = board.title
        self.assertEquals(expected_object_name, "테스트 제목")

    def test_content_content(self):
        board = Board.objects.get(id=1)
        expected_object_name = board.content
        self.assertEquals(expected_object_name, "테스트 내용")

    def test_category_content(self):
        board = Board.objects.get(id=1)
        expected_object_name = board.category.name
        self.assertEquals(expected_object_name, "테스트 카테고리")

    def test_user_info(self):
        board = Board.objects.get(id=1)
        expected_object_name = board.author.username
        self.assertEquals(expected_object_name, "테스트 사용자")

    def test_str_board(self):
        board = Board.objects.get(id=1)
        expected_str = f"Board title = {board.title}, content = {board.content}, author = {board.author}"
        self.assertEqual(str(board), expected_str)

    def test_str_category(self):
        category = Category.objects.get(id=1)
        expected_str = f"Category for {category.code} by {category.name}"
        self.assertEqual(str(category), expected_str)


