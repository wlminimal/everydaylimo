from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

class HomePage(Page):
	page_text_1 = models.TextField(default="에브리데이 리무진에 오신걸 환영합니다")

	page_text_2 = models.TextField(default="20년 경력의")
	page_text_3_bold = models.TextField(default="최고의")
	page_text_4 = models.TextField(default="리무진 서비스")
	page_text_5 = models.TextField(default="TCP Licensed Limousine Service")

	page_text_6 = models.TextField(default="에브리데이 리무진에 오신걸 환영합니다")
	page_text_7_bold = models.TextField(default="고객 맞춤형")
	page_text_8 = models.TextField(default="서비스")
	page_text_9_bold = models.TextField(default="신속 정확한")
	page_text_10 = models.TextField(default="서비스")
	page_text_11 = models.TextField(default="TCP Licensed Limousine Service")

	# 보유차량
	car_subheading = models.TextField(default="서비스 가능한 차량")
	car_heading = models.TextField(default="보유차량")

	car_image1_eng = models.TextField(default="Chevrolet Suburban")
	car_image1_kor = models.TextField(default="쉐비 서버밴")

	car_image2_eng = models.TextField(default="Cadillac Escalade")
	car_image2_kor = models.TextField(default="캐딜락 에스컬레이드")

	car_image3_eng = models.TextField(default="Benz Splinter 12-15 passenger")
	car_image3_kor = models.TextField(default="벤즈 스플린터 12-15 인승")

	car_image4_eng = models.TextField(default="28 Passenger Bus")
	car_image4_kor = models.TextField(default="28인승 버스")

	car_image5_eng = models.TextField(default="33 Passenger Bus")
	car_image5_kor = models.TextField(default="33인승 버스")

	car_image6_eng = models.TextField(default="40 Passenger Bus")
	car_image6_kor = models.TextField(default="40인승 버스")

	# 소개
	about_subheading = models.TextField(default="Everyday Limousine")
	about_heading = models.TextField(default="에브리데이 리무진에 오신걸 환영합니다.")
	about_desc = RichTextField(default="쾌적하고 편안하고 안전하게 모시는 리무진 서비스")

	# 연락처
	contact_heading = models.TextField(default="연락처")
	contact_phone = models.TextField(default="전화번호")
	contact_phonenumber = models.TextField(default="(213)386-6060")

	contact_kakao = models.TextField(default="카카오톡 아이디")
	contact_kakaoID = models.TextField(default="kakao id")

	menu_phonenumber = models.TextField(default="(213)386-6060")
	menu_kakaoID = models.TextField(default="카카오 ID abc")

	content_panels = Page.content_panels + [

				FieldPanel('menu_phonenumber'),
				FieldPanel('menu_kakaoID'),

        FieldPanel('page_text_1'),
        FieldPanel('page_text_2'),
        FieldPanel('page_text_3_bold'),
        FieldPanel('page_text_4'),
        FieldPanel('page_text_5'),

        FieldPanel('page_text_6'),
        FieldPanel('page_text_7_bold'),
        FieldPanel('page_text_8'),
        FieldPanel('page_text_9_bold'),
        FieldPanel('page_text_10'),
        FieldPanel('page_text_11'),

        # 보유차량
        FieldPanel('car_subheading'),
        FieldPanel('car_heading'),

        FieldPanel('car_image1_eng'),
        FieldPanel('car_image1_kor'),

        FieldPanel('car_image2_eng'),
        FieldPanel('car_image2_kor'),

        FieldPanel('car_image3_eng'),
        FieldPanel('car_image3_kor'),

        FieldPanel('car_image4_eng'),
        FieldPanel('car_image4_kor'),

        FieldPanel('car_image5_eng'),
        FieldPanel('car_image5_kor'),

        FieldPanel('car_image6_eng'),
        FieldPanel('car_image6_kor'),

        # 소개
        FieldPanel('about_subheading'),
        FieldPanel('about_heading'),
        FieldPanel('about_desc'),

        # 연락처
        FieldPanel('contact_heading'),
        FieldPanel('contact_phone'),
        FieldPanel('contact_phonenumber'),

        FieldPanel('contact_kakao'),
        FieldPanel('contact_kakaoID'),
  ]
 

  