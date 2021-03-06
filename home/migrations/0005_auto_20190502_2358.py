# Generated by Django 2.1.7 on 2019-05-02 23:58

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190502_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_desc',
            field=wagtail.core.fields.RichTextField(default='쾌적하고 편안하고 안전하게 모시는 리무진 서비스'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_heading',
            field=models.TextField(default='에브리데이 리무진에 오신걸 환영합니다.'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_subheading',
            field=models.TextField(default='Everyday Limousine'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_heading',
            field=models.TextField(default='보유차량'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image1_eng',
            field=models.TextField(default='Chevrolet Suburban'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image1_kor',
            field=models.TextField(default='쉐비 서버밴'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image2_eng',
            field=models.TextField(default='Cadillac Escalade'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image2_kor',
            field=models.TextField(default='캐딜락 에스컬레이드'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image3_eng',
            field=models.TextField(default='Benz Splinter 12-15 passenger'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image3_kor',
            field=models.TextField(default='벤즈 스플린터 12-15 인승'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image4_eng',
            field=models.TextField(default='28 Passenger Bus'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image4_kor',
            field=models.TextField(default='28인승 버스'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image5_eng',
            field=models.TextField(default='33 Passenger Bus'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image5_kor',
            field=models.TextField(default='33인승 버스'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image6_eng',
            field=models.TextField(default='40 Passenger Bus'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_image6_kor',
            field=models.TextField(default='40인승 버스'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='car_subheading',
            field=models.TextField(default='서비스 가능한 차량'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_heading',
            field=models.TextField(default='연락처'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_kakao',
            field=models.TextField(default='카카오톡 아이디'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_kakaoID',
            field=models.TextField(default='kakao id'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_phone',
            field=models.TextField(default='전화번호'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_phonenumber',
            field=models.TextField(default='(213)386-6060'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_text_10',
            field=models.TextField(default='서비스'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_text_11',
            field=models.TextField(default='TCP Licensed Limousine Service'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_text_3_bold',
            field=models.TextField(default='최고의'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_text_4',
            field=models.TextField(default='리무진 서비스'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_text_5',
            field=models.TextField(default='TCP Licensed Limousine Service'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_text_6',
            field=models.TextField(default='에브리데이 리무진에 오신걸 환영합니다'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_text_7_bold',
            field=models.TextField(default='고객 맞춤형'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_text_8',
            field=models.TextField(default='서비스'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_text_9_bold',
            field=models.TextField(default='신속 정확한'),
        ),
    ]
