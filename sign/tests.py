from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User
# Create your tests here.

class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1,name="oneplus 3 event",status =True,limit =2000,address='shenzhen',start_time='2019-06-12 02:52:22')
        Guest.objects.create(id=1,event_id=1,realname='alen',phone='13711001101',email='alen@mail.com',sign=False)

    def test_event_models(self):
        result = Event.objects.get(name="oneplus 3 event")
        self.assertEqual(result.address,"shenzhen")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result =Guest.objects.get(phone="13711001101")
        self.assertEqual(result.realname,"alen")
        self.assertFalse(result.sign)

class IndexPageTest(TestCase):
    def test_index_page_renders_index_template(self):
        '''测试index视图'''
        reponse = self.client.get('/index/')
        self.assertEqual(reponse.status_code,200)
        self.assertTemplateUsed(reponse,'index.html')

class LoginActionTest(TestCase):
    '''测试登录动作'''

    def setUp(self):
        User.objects.create_user('admin','admin@mail.com','admin123456')

    def test_add_admin(self):
        '''添加新用户'''
        user = User.objects.get(username='admin')
        self.assertEqual(user.username,'admin')
        self.assertEqual(user.email,'admin@mail.com')

    def test_login_action_username_password_null(self):
        '''用户名密码为空'''
        test_data = {'username':'','password':''}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"username or password error!",response.content)

    def test_login_action_username_password_error(self):
        '''用户名密码错误'''
        test_data = {'username': 'abc', 'password': '123'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content)

    def test_login_action_success(self):
        '''用户登录成功'''
        test_data = {'username': 'admin', 'password': 'admin123456'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)



