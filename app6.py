# url_for('static',filename='파일_이름')
# 플라스크 애플리케이션 내에서 정적 파일(이미지,css,자바스크립트 파일 등)의 URL을 생성할 때 사용된다.
# 플라스크는 기본적으로 'static' 폴더 내의 파일들을 정적 파일로 서비스한다.

from flask import url_for

css_url = url_for('static',filename='css/style.css')

